# Chat with PDF using Multiple Language Models

This project enables users to ask questions based on the content of a PDF file and receive responses from two different language models simultaneously for easy comparison and confirmation.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/your_repository.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:

    Create a `.env` file in the project directory and add the following:

    ```plaintext
    GOOGLE_API_KEY=your_google_api_key_here
    ```

    Replace `your_google_api_key_here` with your actual Google API key.

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run PDF-QnA-gemini-palm-2.py
    ```

2. Upload a PDF file:

    - Click on the "Upload PDF File" button.
    - Select a PDF file to upload.

3. Process the uploaded file:

    - Click on the "Process" button to extract text from the uploaded PDF file.
    - Once processing is complete, you can ask questions related to the content of the PDF file.

4. Ask a question:

    - Type your question in the text input field labeled "Ask a Question from the PDF File".
    - Press Enter or click outside the input field to submit the question.

5. View responses:

    - Two different language models (LLMs) will provide responses based on the same question and context from the PDF file.
    - Responses from both LLMs will be displayed side by side for easy comparison.

## Configuration

- The Google API key is required for using Google's language models. Make sure to set it up in the `.env` file.

## File Structure

- `PDF-QnA-gemini-palm-2.py`: Main Streamlit application script.
- `requirements.txt`: List of Python dependencies.
- `README.md`: Project documentation.
- `.env`: Environment variable configuration file (not included in the repository).
- `Sample-output-X.png`: sample responses screenshots
- `cricket-data-5-page.pdf` & ``: The file that is used to test the chatbot.

# Summary of the chatbot's performance

- Successfully fetches and provides information from cricket and ads datasets.
- Efficiently handles fetch and provide type questions.
- Encounter challenges with mathematical calculations, resulting in inaccurate answers.
- Gemini LLM outperforms PaLM-2, providing more accurate responses and better handling of missing data scenarios.

