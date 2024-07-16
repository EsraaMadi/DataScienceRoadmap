import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st
import os
import json

# credentials_dict = {
#   "TYPE": os.getenv("TYPE"),
#   "PROJECT_ID": os.getenv("PROJECT_ID"),
#   "PRIVATE_KEY_ID": os.getenv("PRIVATE_KEY_ID"),
#   "PRIVATE_KEY": os.getenv("PRIVATE_KEY"),
#   "CLIENT_EMAIL": os.getenv("CLIENT_EMAIL"),
#   "CLIENT_ID": os.getenv("CLIENT_ID"),
#   "AUTH_URI": os.getenv("AUTH_URI"),
#   "TOKEN_URI": os.getenv("TOKEN_URI"),
#   "AUTH_PROVIDER_X509_CERT_URL": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
#   "CLIENT_X509_CERT_URL": os.getenv("CLIENT_X509_CERT_URL"),
#   "UNIVERSE_DOMAIN": os.getenv("UNIVERSE_DOMAIN")
# }


# Read the secret JSON from the environment variable
google_credentials_json = os.getenv('GOOGLE_CREDENTIALS')

if google_credentials_json is None:
    raise ValueError("No Google credentials found in environment variables.")

# Parse the JSON string into a dictionary
credentials_dict = json.loads(google_credentials_json)


# Define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# Add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, scope)

# Authorize the clientsheet 
client = gspread.authorize(creds)




def load_roadmap(file_name):

    # Open the spreadhseet
    sheet = client.open(file_name)
    
    # Get the first sheet of the Spreadsheet
    worksheet = sheet.get_worksheet(0)
    
    # Get all the records of the data
    data = worksheet.get_all_records()
    
    # Convert to a DataFrame
    df = pd.DataFrame(data)
    return df

def load_champian(week_no ):
    # Open the spreadhseet
    sheet = client.open_by_key('19Ft_cQgzZu4V1xh_OtFfnLgGEPslqmHjP2z8yKcLG8w')
    
    # Initialize a dictionary to hold dataframes
    dataframes = {}

    # Loop through each worksheet in the spreadsheet
    for worksheet in sheet.worksheets():
        if 'Week' in worksheet.title and int(worksheet.title.split(' ')[1]) < week_no:
            data = worksheet.get_all_values()
            headers = data[10]      
            data = [row[1:] for row in data[11:] if len(row[1])> 2] # delete first column 
            df = pd.DataFrame(data, columns=headers[1:])
            # Store the DataFrame in a dictionary with the worksheet title as the key
            dataframes[worksheet.title] = df
    return dataframes


def _clean_df(df):
    duplicated_columns = set()
    
    for col in df.columns[1:]:
        df[col] = df[col].astype(int)
        if '_' in col:
            duplicated_columns.add(col.split('_')[0])
            
    df_new = df.copy()
    
    for col in duplicated_columns:
        # Use the filter method to select columns
        selected_columns = df_new.filter(like=col)
        
        # Sum the selected columns and create a new column for the sum
        df_new[col] = selected_columns.sum(axis=1)

        # Drop the original columns
        df_new = df_new.drop(selected_columns.columns, axis=1)
    return df_new
    
def _clean_week(df_dict):
    for k , df in df_dict.items():
        df_dict[k] = _clean_df(df)
    return df_dict
                
def _aggregate_data(df_dict):
    idx = 0
    agg_df = pd.DataFrame()
    for k, df in df_dict.items():
        if idx == 0:
            agg_df = df
        else:
            agg_df = pd.merge(agg_df, df, on='Name', how='inner')
        idx += 1
    return agg_df
            
        
    
def get_champions(df_dict):
    students_dict = {}
    student_result = {}
    df_dict_clean = _clean_week(df_dict)
    agg_df = _aggregate_data(df_dict_clean)
    agg_df_clean = _clean_df(agg_df)
    return agg_df_clean
  
