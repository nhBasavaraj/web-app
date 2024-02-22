import streamlit as st
import os
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor
import requests
import pandas as pd
import json
import csv
import gzip
from datetime import datetime
from typing import Sequence
from langchain_core.tools import BaseTool


# Function to fetch data from Facebook Ads API and save to CSV
def fetch_and_save_data(fb_api_url, access_token):
    # Define the API endpoint URL
    endpoint = f'{fb_api_url}/insights'

    # Specify parameters for the request
    params = {
        'access_token': access_token,
        'time_range[since]': '2023-11-20',
        'time_range[until]': '2023-11-30',
        'time_increment': 1,
        'limit': 5000,
        'level': 'ad',
        'breakdowns': 'age,gender',
        'fields': 'campaign_name,campaign_id,adset_name,adset_id,ad_name,ad_id,reach,frequency,impressions,spend,clicks,cpc,ctr,cpp,cpm',
    }

    # Set the 'Accept-Encoding' header to handle different compression methods
    headers = {'Accept-Encoding': 'gzip, deflate, br'}

    # Make the API request
    response = requests.get(endpoint, params=params, headers=headers)

    # Check if the request was successful
    response.raise_for_status()

    # Access the decoded content
    response_content = response.json()

    # Extract the list of dictionaries from the 'data' key
    data_to_write = response_content.get('data', [])
    

    # Extract header from the keys of the dictionaries
    header = set().union(*(d.keys() for d in data_to_write))

    # Specify the CSV file path
    csv_file_path = 'output.csv'

    # Writing to CSV file
    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=header)

        # Write the header
        csv_writer.writeheader()

        # Write the data
        csv_writer.writerows(data_to_write)

    print(f'CSV file saved to: {csv_file_path}')

# Function to create and run the CSV agent
def create_and_run_agent(csv_data_path, question, llm_model_api_key):
    # Create the CSV agent using the specified language model
    if llm_model_api_key.startswith("sk-"):
        # OpenAI API key
        llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo", api_key=llm_model_api_key)
    elif llm_model_api_key.startswith("AIza"):
        # Gemini-Pro API key
        os.environ["GOOGLE_API_KEY"] = llm_model_api_key
        llm = ChatGoogleGenerativeAI(temperature=0, model="gemini-pro", convert_system_message_to_human=True,)
    else:
        # Handle other cases or raise an error based on your requirements
        raise ValueError("Invalid LLM API key specified")

    agent = create_csv_agent(
        llm=llm,
        path=csv_data_path,
        verbose=True,
    )

    # Run the agent with the user's question
    response = agent.run(question)

    return response


# Reset conversation function
def reset_conversation():
    st.session_state.conversation_history = []

# Streamlit app
def main():
    # Initialize csv_file_path
    csv_file_path = None
    excel_file_path = None
    csv_excel_file = None

    # Initialize session state if not already done
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []

    st.set_page_config(page_title="Chat with your Data")
    st.title("Chat with your Data")

    col1, col2 = st.columns([3, 1])

    selected_option = st.sidebar.radio("Select an Option to Load Dataset", ["Upload CSV File", "Upload Excel File", "Fetch Data using API"], key="selected_option")

    with col1:
        st.sidebar.title("Inputs")

        if selected_option == "Upload CSV File":
            csv_file = st.sidebar.file_uploader("Upload CSV File:", type=["csv"])
            if csv_file is not None:
                csv_file_path = 'uploaded_file.csv'
                with open(csv_file_path, 'wb') as f:
                    f.write(csv_file.getvalue())
            excel_file = None
            fb_api_url = None
        elif selected_option == "Upload Excel File":
            excel_file = st.sidebar.file_uploader("Upload Excel File:", type=["xlsx"])
            if excel_file is not None:
                if excel_file.name.endswith('.xlsx'):
                    # Load the Excel file and list sheet names
                    excel_file = pd.ExcelFile(excel_file)
                    sheet_names = excel_file.sheet_names

                    # Create dropdown menu for selecting sheet
                    selected_sheet = st.sidebar.selectbox("Select Sheet", sheet_names)

                    # Read the selected sheet
                    excel_df = pd.read_excel(excel_file, sheet_name=selected_sheet)
                    csv_file_path = 'output.csv'
                    excel_df.to_csv(csv_file_path, index=False)
                    #st.sidebar.success("Excel file converted and saved as CSV successfully!")
            fb_api_url = None
        elif selected_option == "Fetch Data using API":
            csv_excel_file = None
            fb_api_url = st.sidebar.text_input("Enter Facebook API URL:")
            access_token = st.sidebar.text_input("Enter Access Token:")

            if st.sidebar.button("Fetch and Save Data"):
                fetch_and_save_data(fb_api_url, access_token)
                st.sidebar.success("Data fetched and saved successfully!")

    with col1:
        st.sidebar.title("LLM Configuration")
        llm_model = st.sidebar.selectbox("Select Language Model", ["OpenAI", "Gemini-Pro"])
        llm_model_api_key = st.sidebar.text_input("Enter LLM API Key:")

    with col2:
        st.markdown(
            """
            <style>
                .stMarkdown {
                    font-size: 18px !important;
                    line-height: 1.6 !important;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )

    # Use st.text_area for user input
    question = st.chat_input(placeholder="Type your question...", key="user_question")

    # Check if the necessary fields are provided before processing the user's question
    if (csv_excel_file is not None or "output.csv" in os.listdir()) and llm_model_api_key and question:
        if csv_file_path is not None:
            # Use the uploaded CSV file path
            csv_data_path = csv_file_path
        # elif excel_file_path is not None:
        #     # Convert Excel file to CSV
        #     excel_df = pd.read_excel(excel_file_path)
        #     csv_data_path = 'converted_file.csv'
        #     excel_df.to_csv(csv_data_path, index=False)
        else:
            # Use the existing CSV file
            csv_data_path = "output.csv"

        # Your logic for processing the user's question
        response = create_and_run_agent(
            csv_data_path=csv_data_path,
            question=question,
            llm_model_api_key=llm_model_api_key,
        )

        # Update conversation history in session state
        st.session_state.conversation_history.append({
            'user_question': question,
            'agent_response': response
        })

    # Display conversation history
    for entry in st.session_state.conversation_history:
        st.chat_message("user").write(entry['user_question'])
        st.chat_message("assistant", avatar="./fig logo-04.png").write(entry['agent_response'])

    # Button to clear conversation history using on_click
    st.button("Clear Conversation", on_click=reset_conversation)

if __name__ == "__main__":
    main()
