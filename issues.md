# Issues

### 1. AWS Beanstalk Deployment Issue
- **Status:** Investigating 🔍
- **Description:**
  - Deployed the web application on AWS Beanstalk.
  - Encountering error: "Failed to launch environment."
  - Error message indicates: "The instance profile aws-elasticbeanstalk-ec2-role associated with the environment does not exist."
- **Action Taken:**
  - Investigation pending; further analysis needed to address this issue.

### 2. JSON Decode Error During AWS EC2 Deployment
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

### 3. Library Installation Issue with llm-agent
- **Status:** Resolved ✅
- **Description:**
  - llm-agent can't install any libraries during QnA process.
  - Before running or using the app, it's recommended to install all required libraries and tools mentioned in the requirements.txt file.
- **Example:**
  - If a required library like matplotlib is not installed, and the agent is asked to plot a chart, it will try to import the library. If the import fails, it will attempt to install the library. However, since the agent can't install libraries, this process will fail continuously until the agent stops due to iteration or time limit.
