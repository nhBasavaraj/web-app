# Chat with your Data

Chat with your Data is a Streamlit application designed to facilitate interactive exploration of data stored in various formats, including CSV files, Excel files, and data fetched from APIs. It integrates a language model-based chatbot that enables users to ask questions about the data, providing insights and analysis in a conversational manner.

## Features

- **Data Interaction**: Users can upload CSV files, fetch data from the Facebook Ads API, or even upload Excel files, allowing flexibility in data source.
- **Natural Language Interaction**: Utilizes a language model-based chatbot to interpret user questions and provide insightful responses about the data.
- **Dynamic Visualization**: Offers dynamic visualizations and summaries of the data based on user queries, enhancing data exploration and understanding. (Note: May not work as expected, still under development)
- **Customizable Language Models**: Users can choose between different language models, such as OpenAI and Gemini-Pro, and configure API keys for seamless integration.
- **Conversation History**: Maintains a conversation history, enabling users to review past interactions with the chatbot.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repository.git
    cd your-repository
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure API keys:
   - **OpenAI:**
     - Generate your OpenAI API key [here](https://platform.openai.com/api-keys).
       
   - **Gemini:**
     - Generate your Gemini API key from [Google Maker Suite](https://makersuite.google.com/app/apikey).

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run web-app-code.py
    ```

2. Select an option to load dataset:
    - Upload a CSV file
    - Upload an Excel file
    - Fetch data using the Facebook API

3. Choose a language model for the chatbot and enter the corresponding API key.

4. Interact with the chatbot by typing questions about the data.

## Note ⚠️⚠️

Please note that currently, our app is not efficient at generating chart-based responses within the chat_message frame. Charts are displayed at the top of the web app and may be overwritten when new chart questions are asked. We are actively working on improving this feature.

## Dependencies

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)


