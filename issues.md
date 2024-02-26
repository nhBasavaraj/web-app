# Issues
----------------
### 1. AWS Beanstalk Deployment Issue
- **Status:** Investigating 🔍
- **Description:**
  - Deployed the web application on AWS Beanstalk.
  - Encountering error: "Failed to launch environment."
  - Error message indicates: "The instance profile aws-elasticbeanstalk-ec2-role associated with the environment does not exist."
- **Action Taken:**
  - Investigation pending; further analysis needed to address this issue.
---------------
### 2. Library Installation Issue with llm-agent
- **Status:** Resolved ✅
- **Description:**
  - llm-agent can't install any libraries during QnA process.
  - Before running or using the app, it's recommended to install all required libraries and tools mentioned in the requirements.txt file.
- **Example:**
  - If a required library like matplotlib is not installed, and the agent is asked to plot a chart, it will try to import the library. If the import fails, it will attempt to install the library. However, since the agent can't install libraries, this process will fail continuously until the agent stops due to iteration or time limit.

--------------------

### JSONDecode Error Handling (as I worked on)
- **Description:**
  - **Error Occurrence Scenarios:**
    - **SageMaker Notebook Development:** JSONDecode error occurs when developing the fetch and save functionality in a SageMaker Notebook file (.ipynb).
    - **Python File Development:** use simple request methods to fetch and save data in a Python file (.py). as mentioned in issue-4.
    - **AWS EC2 Deployment:** use simple request methods to fetch and save data in a Python file (.py). as mentioned in issue-4.
  - **Solution:** If JSONDecode error occurs in SageMaker Notebook development, implement the solution as described in Issue 3.
  - **Solution:** If JSONDecode error occurs when developing in a Python file and deploying in aws EC2 implement the solution as described in Issue 3.

### 3. JSONDecode Error Resolved in SageMaker Notebook
- **Status:** Resolved ✅
- **Description:**
  - Encountered JSONDecode error when fetching data from the source using API in SageMaker Notebook.
- **Issue Resolution:**
  - **Encoding Setup**: 
    - Implemented the `Accept-Encoding` header in the request with parameters `'gzip, deflate, br'`. 
    - This header informs the server about the client's ability to handle different compression methods.
    - By specifying accepted encodings, it allows the server to compress its response accordingly, reducing data transfer size and potential errors during decoding.
  - **Correct Handling of Response**: 
    - Utilized the `response.json()` method to decode the response content.
    - This method ensures that the response is correctly parsed as JSON format, preventing JSONDecode errors.
  - **Data Extraction and Saving**: 
    - Extracted the relevant data from the decoded JSON response using appropriate data manipulation techniques.
    - Saved the extracted data to a CSV file named 'output.csv' for further analysis or use.
  - **Confirmation Message**: 
    - Printed a confirmation message indicating the successful saving of the CSV file along with its file path.
   
  --------------------
### 4. JSON Decode Error During when developing in a Python file and AWS EC2 Deployment 
- **Status:** Resolved ✅
- **Description:**
  - Successfully deployed the web application on AWS EC2.
  - Functionality operational; web app running smoothly.
  - Previously encountered JSON Decode error when fetching and saving data from an API.
- **Resolution:**
  - Implemented a simple method to fetch and save data as CSV.
- **API Request Setup:**
  - Constructed API endpoint URL and defined parameters.
- **Data Retrieval and Saving:**
  - Sent GET request to API endpoint using `requests.get()` method with defined parameters.
  - Processed received data into a DataFrame using pandas if response status code was 200 (OK).
  - Saved DataFrame as CSV named 'output.csv' without index using UTF-8 encoding.
