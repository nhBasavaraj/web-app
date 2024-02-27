# Bug: Inconsistent Response when Requesting Sample Data in Tabular Form

## Description
When requesting a sample of few rows of data in tabular form from the LLM (Large Language Model) within the web app, the response is inconsistent. Sometimes the LLM provides the table data response as expected, while other times it gives a generic response such as "see above" or "this is the sample of few rows of data".

## Steps to Reproduce
1. Open the web app.
2. Upload CSV/Excel/data fetched from API.
3. Request a sample of few rows of data in tabular form.
4. Observe the response from the LLM.

## Expected Behavior
The LLM should consistently provide the sample data in tabular form when requested.

## Actual Behavior
The LLM response is inconsistent, sometimes providing the expected table data and other times giving a generic response.

## Solution
After experimenting with different prompts, it was found that modifying the prompt helped achieve the desired response consistently. Here's the trial and error process:

### Prompt 1:
- Prompt: "Provide me the sample of five rows of data in a table or tabular form."
- Response from LLM: "See above."

### Prompt 2:
- Prompt: "Provide me the sample of five rows of data in a table form."
- Response from LLM: "This is the sample of three rows of data in a table form."

### Prompt 3:
- Prompt: "Provide me the sample of five rows of data in a table form, print the table in the final answer."
- Response from LLM: It gave three rows of data in a paragraph form.

### Prompt 4:
- Prompt: "Provide me the sample of three rows of data in a table form, display the table in the final answer."
- Response from LLM: It gave a list of three rows of data with columns names in paragraph form.

### Prompt 5 (Solution):
- Prompt: "Provide me the sample of three rows of data in a table form, display the table in the final answer as table form."
- Response from LLM: The LLM now consistently provides the response in table form.

By using Prompt 5, the LLM generates the desired response consistently, displaying the table data in the final answer in tabular form.

## Proposed Solution
Continue to use Prompt 5 to ensure consistent and accurate responses from the LLM when requesting sample data in tabular form within the web app.
