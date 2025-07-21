import gspread
import streamlit as st
from google.oauth2.service_account import Credentials

# --- Google Sheets Setup ---
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SHEET_NAME = "EcoCart_Rewards"  # You can rename this as needed

def get_sheet():
    """Authorize and return Google Sheet worksheet."""
    credentials = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=SCOPES
    )
    client = gspread.authorize(credentials)
    
    try:
        sheet = client.open(SHEET_NAME).sheet1
    except gspread.exceptions.SpreadsheetNotFound:
        st.error(f"Spreadsheet '{SHEET_NAME}' not found. Make sure it exists in your Google Drive.")
        st.stop()
    
    return sheet

def get_rewards(sheet, user_id):
    """Get the current reward points for a user."""
    try:
        records = sheet.get_all_records()
        for row in records:
            if row.get("user_id") == user_id:
                return row.get("points", 0)
    except Exception as e:
        st.error(f"Failed to read sheet: {e}")
    
    return 0

def update_rewards(sheet, user_id, points_to_add):
    """Update reward points for a user."""
    try:
        cell = sheet.find(user_id)
        current = int(sheet.cell(cell.row, cell.col + 1).value)
        sheet.update_cell(cell.row, cell.col + 1, current + points_to_add)
    except gspread.exceptions.CellNotFound:
        # New user – add to sheet
        sheet.append_row([user_id, points_to_add])
    except Exception as e:
        st.error(f"Failed to update rewards: {e}")
