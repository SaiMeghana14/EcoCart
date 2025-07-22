# helpers/google_rewards.py

import gspread
import streamlit as st
from google.oauth2.service_account import Credentials

def get_gsheet_client():
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=scopes
    )
    return gspread.authorize(creds)

def get_sheet(sheet_name="Rewards"):
    client = get_gsheet_client()
    spreadsheet = client.open(st.secrets["spreadsheet_name"])  # You store "EcoCart Rewards"
    return spreadsheet.worksheet(sheet_name)

def get_rewards(sheet):
    return sheet.get_all_records()

def update_rewards(sheet, user, new_points):
    records = sheet.get_all_records()
    usernames = [record["Name"] for record in records]

    if user in usernames:
        row_index = usernames.index(user) + 2  # header offset
        try:
            current_points = int(sheet.cell(row_index, 2).value)
        except ValueError:
            current_points = 0
        updated_points = current_points + new_points
        sheet.update_cell(row_index, 2, updated_points)
    else:
        sheet.append_row([user, new_points])
