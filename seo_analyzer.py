import os
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import config


SCOPES = ['[https://www.googleapis.com/auth/webmasters.readonly](https://www.googleapis.com/auth/webmasters.readonly)']

# Initialize credentials and service (using values from config.py)
credentials = ServiceAccountCredentials.from_json_keyfile_name(config.CREDENTIALS_FILE, scopes=SCOPES)
service = build('webmasters', 'v3', credentials=credentials)

# Request data from Google Search Console
request = {
    'startDate': config.START_DATE,
    'endDate': config.END_DATE,
    'dimensions': ['query', 'page', 'country'], 
    'rowLimit': 25000  # Adjust as needed
}
response = service.searchanalytics().query(siteUrl=config.SITE_URL, body=request).execute()

# Process the data into a DataFrame
rows = response['rows']
data = pd.DataFrame(rows)

# Rename columns for clarity
data = data.rename(columns={
    'keys': 'Metrics',
    'clicks': 'Clicks',
    'impressions': 'Impressions',
    'ctr': 'CTR',
    'position': 'Position'
})

# Split the 'Metrics' column into 'Query', 'Page', and 'Country'
data[['Query', 'Page', 'Country']] = pd.DataFrame(data['Metrics'].tolist(), index=data.index)

# Drop the original 'Metrics' column
data.drop(columns=['Metrics'], inplace=True)

# Print the data
print(data)