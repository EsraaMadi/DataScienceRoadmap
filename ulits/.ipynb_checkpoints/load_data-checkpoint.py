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

def load_champian():
    # Open the spreadhseet
    sheet = client.open_by_key('19Ft_cQgzZu4V1xh_OtFfnLgGEPslqmHjP2z8yKcLG8w')
    
    # Initialize a dictionary to hold dataframes
    dataframes = {}

    # Loop through each worksheet in the spreadsheet
    for worksheet in sheet.worksheets():
        
        data = worksheet.get_all_values()
        headers = data[10] 
        df = pd.DataFrame(data[11:], columns=headers)
        # # Get all the records of the data
        # data = worksheet.get_all_records()

        # # Convert to a DataFrame
        # df = pd.DataFrame(data)

        # Store the DataFrame in a dictionary with the worksheet title as the key
        dataframes[worksheet.title] = df

    return dataframes