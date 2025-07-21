# helpers/google_rewards.py

import gspread
import streamlit as st
from oauth2client.service_account import ServiceAccountCredentials

def get_gsheet_client():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["gcp_service_account"], scope)
    client = gspread.authorize(creds)
    return client

def get_sheet(sheet_name="Rewards"):
    client = get_gsheet_client()
    sheet = client.open(st.secrets["private_gsheets_url"]).worksheet(sheet_name)
    return sheet

def get_rewards(sheet):
    records = sheet.get_all_records()
    return records

def update_rewards(sheet, user, new_points):
    records = sheet.get_all_records()
    usernames = [record["Name"] for record in records]

    if user in usernames:
        row_index = usernames.index(user) + 2  # 1-based index + header row
        current_points = int(sheet.cell(row_index, 2).value)
        updated_points = current_points + new_points
        sheet.update_cell(row_index, 2, updated_points)
    else:
        sheet.append_row([user, new_points])
