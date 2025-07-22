import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

st.title("🔍 EcoCart Google Sheets Debugger")

# ✅ Check secrets keys
st.subheader("1️⃣ Secrets Loaded")
st.write("Secrets keys available:", list(st.secrets.keys()))

# ✅ Setup Google Sheets Client
try:
    scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scopes)
    client = gspread.authorize(creds)
    st.success("✅ Google Sheets client initialized!")
except Exception as e:
    st.error(f"❌ Error initializing Sheets client: {e}")
    st.stop()

# ✅ Check Spreadsheet Name
spreadsheet_name = st.secrets.get("spreadsheet_name", None)
if not spreadsheet_name:
    st.error("❌ `spreadsheet_name` is missing in secrets.")
    st.stop()
else:
    st.info(f"📄 Spreadsheet Name: **{spreadsheet_name}**")

# ✅ Open Spreadsheet
try:
    sheet = client.open(spreadsheet_name).worksheet("Leaderboard")
    st.success("✅ Connected to 'Leaderboard' worksheet!")
except Exception as e:
    st.error(f"❌ Error accessing worksheet: {e}")
    st.stop()

# ✅ Display first few rows
try:
    records = sheet.get_all_records()
    st.subheader("📊 Preview Sheet Records:")
    st.dataframe(records[:10])  # show first 10 rows
except Exception as e:
    st.error(f"❌ Error fetching records: {e}")
