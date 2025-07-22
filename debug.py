import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# ✅ Check keys present in secrets
st.sidebar.header("🔍 Debug: Google Sheets Access Test")
st.sidebar.write("Secrets Keys:", list(st.secrets.keys()))

# ✅ Debugging Client Access
def get_client():
    credentials = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=[
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
    )
    return gspread.authorize(credentials)

try:
    client = get_client()
    st.sidebar.success("✅ Auth OK")

    # List accessible spreadsheets
    files = client.list_spreadsheet_files()
    st.sidebar.write("Available Sheets:", [f["name"] for f in files])

    # Access EcoCart Rewards
    sheet = client.open("EcoCart Rewards").worksheet("Leaderboard")
    st.sidebar.success("✅ Found worksheet 'Leaderboard'")

except Exception as e:
    st.sidebar.error(f"❌ Error: {e}")

st.stop()
