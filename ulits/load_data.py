import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st

credentials_dict = {
  "type": st.secrets["type"],
  "project_id": st.secrets["project_id"],
  "private_key_id": st.secrets["private_key_id"],
  "private_key": st.secrets["private_key"],
  "client_email": st.secrets["client_email"],
  "client_id": st.secrets["client_id"],
  "auth_uri": st.secrets["auth_uri"],
  "token_uri": st.secrets["token_uri"],
  "auth_provider_x509_cert_url": st.secrets["auth_provider_x509_cert_url"],
  "client_x509_cert_url": st.secrets["client_x509_cert_url"],
  "universe_domain": st.secrets["universe_domain"]
}

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

def load_champian(Week_no ):
    # Open the spreadhseet
    sheet = client.open_by_key('19Ft_cQgzZu4V1xh_OtFfnLgGEPslqmHjP2z8yKcLG8w')
    
    # Initialize a dictionary to hold dataframes
    dataframes = {}

    # Loop through each worksheet in the spreadsheet
    for worksheet in sheet.worksheets():
        if 'Week' in worksheet.title and worksheet.title.split(' ')[1]<Week_no:
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
    




    