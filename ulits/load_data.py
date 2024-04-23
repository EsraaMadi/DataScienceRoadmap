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

def read_worksheet(worksheet):
    # Get all the records of the data
    data = worksheet.get_all_records()
    
    # Convert to a DataFrame
    df = pd.DataFrame(data)
    return df


def load_roadmap(file_name, all_sheets=False):
    # Define the scope
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    
    # Add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, scope)
    
    # Authorize the clientsheet 
    client = gspread.authorize(creds)
    
    # Open the spreadhseet
    spreadsheet = client.open(file_name)
    sheets = spreadsheet.worksheets()

    df_sheets = []
    for sheet in sheets:
        df_sheets.append(read_worksheet(worksheet))
    
    # Get the first sheet of the Spreadsheet
    if all_sheets:
        return df_sheets
    else:
        return df_sheets[0]