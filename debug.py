import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

st.title("🔍 EcoCart Google Sheets Debugger")

# ✅ 1️⃣ Secrets Check
st.subheader("1️⃣ Secrets Loaded")
st.write("Secrets keys available:", list(st.secrets.keys()))

# ✅ 2️⃣ Setup Google Sheets Client
try:
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"], scopes=scopes
    )
    client = gspread.authorize(creds)
    st.success("✅ Google Sheets client initialized!")
except Exception as e:
    st.error(f"❌ Error initializing Sheets client: {e}")
    st.stop()

# ✅ 3️⃣ Retrieve Spreadsheet Name
spreadsheet_name = st.secrets["global"].get("spreadsheet_name")
st.info(f"📄 Retrieved Spreadsheet Name: **{spreadsheet_name}**")

# ✅ 4️⃣ Open Spreadsheet and Worksheet
worksheet_name = "Leaderboard"  # Adjust if your sheet tab has a different name
try:
    sheet = client.open(spreadsheet_name).worksheet(worksheet_name)
    st.success(f"✅ Connected to worksheet: **{worksheet_name}**")
except Exception as e:
    st.error(f"❌ Error accessing worksheet: {e}")
    st.stop()

# ✅ 5️⃣ Preview Sheet Records
try:
    records = sheet.get_all_records()
    st.subheader("📊 Preview Sheet Records (Top 10):")
    st.dataframe(records[:10])
except Exception as e:
    st.error(f"❌ Error fetching records: {e}")
