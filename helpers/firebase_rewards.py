import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scope)
client = gspread.authorize(creds)

sheet = client.open("RewardsLeaderboard").worksheet("Rewards")

def get_rewards(user_id):
    data = sheet.get_all_records()
    for row in data:
        if row['user_id'] == user_id:
            return row['points']
    return 0

def update_rewards(user_id, points):
    data = sheet.get_all_records()
    for idx, row in enumerate(data):
        if row['user_id'] == user_id:
            sheet.update_cell(idx+2, 2, points)  # Assuming column 2 = points
            return True
    sheet.append_row([user_id, points])
    return True

def get_leaderboard():
    data = pd.DataFrame(sheet.get_all_records())
    return data.sort_values(by='points', ascending=False)

# ✅ Demo UI
user = st.text_input("Enter User ID")
if st.button("Show Rewards"):
    st.write(f"Points: {get_rewards(user)}")

if st.button("Add 10 points"):
    points = get_rewards(user) + 10
    update_rewards(user, points)
    st.success(f"Updated to {points} points!")

st.subheader("Leaderboard")
st.dataframe(get_leaderboard())
