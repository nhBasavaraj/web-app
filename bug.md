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


