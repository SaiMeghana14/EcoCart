import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import random

def get_client():
    creds = Credentials.from_service_account_info(
        st.write("Secrets Keys:", list(st.secrets.keys()))
        st.secrets["gcp_service_account"],
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    return gspread.authorize(creds)

st.sidebar.header("🔍 Debug: Google Sheets Access Test")
try:
    client = get_client()
    st.sidebar.success("✅ Auth OK")
    files = client.list_spreadsheet_files()
    st.sidebar.write("Available sheets:", [f['name'] for f in files])
    sheet = client.open("EcoCart Rewards").worksheet("Leaderboard")
    st.sidebar.success("✅ Found worksheet 'Leaderboard'")
except Exception as e:
    st.sidebar.error("❌ " + repr(e))
st.stop()

# ✅ Google Sheets Setup
def get_gsheet_client():
    credentials = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=[
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
    )
    return gspread.authorize(credentials)

def get_sheet():
    client = get_gsheet_client()
    return client.open("EcoCart Rewards").worksheet("Leaderboard")

def get_rewards(sheet, username):
    data = sheet.get_all_records()
    for row in data:
        if row['Username'] == username:
            return row['Points']
    return 0

def update_rewards(sheet, username, points):
    data = sheet.get_all_records()
    for i, row in enumerate(data, start=2):
        if row['Username'] == username:
            sheet.update_cell(i, 2, points)
            return True
    sheet.append_row([username, points])
    return True

# ✅ EcoCart Logic
def get_carbon_footprint(item, quantity):
    item_data = {
        "Banana": 0.1,
        "Milk": 1.2,
        "Beef": 27.0,
        "Rice": 2.7,
        "Bread": 0.8
    }
    return item_data.get(item, 0) * quantity

def get_suggestions(item):
    suggestions = {
        "Beef": "Try plant-based alternatives like tofu or lentils.",
        "Milk": "Consider oat or almond milk to reduce emissions.",
        "Rice": "Quinoa or barley are eco-friendlier grains.",
        "Bread": "Whole grain breads with local ingredients are better.",
        "Banana": "Buy local and seasonal to cut transport emissions."
    }
    return suggestions.get(item, "Good choice!")

def assign_reward(points):
    if points < 10:
        return "🌱 Eco Beginner"
    elif points < 30:
        return "🌿 Eco Warrior"
    else:
        return "🌍 Sustainability Champion"

# ✅ EcoCart Streamlit App
from components import (
    product_list, barcode_scanner, dashboard, compare_products,
    coupons, daily_challenges, eco_news_feed, login, leaderboard
)

# ✅ Initialize Sheet
sheet = get_sheet()

if "user_id" not in st.session_state:
    st.session_state.user_id = None

st.set_page_config(page_title="EcoCart Streamlit", layout="wide")
st.title("🛒 EcoCart – Sustainable Smart Shopping Assistant (Streamlit Edition)")

if st.session_state.user_id:
    points = get_rewards(sheet, st.session_state.user_id)
    st.sidebar.success(f"Logged in as: {st.session_state.user_id}")
    st.sidebar.info(f"🌱 Your Eco Points: {points}")
else:
    st.sidebar.warning("Not logged in. Login to track your points.")

menu = st.sidebar.radio(
    "Navigate",
    [
        "Product List", "Barcode Lookup", "Nearby Stores", "Compare Products",
        "Daily Challenges", "Coupons", "Leaderboard", "Eco News", "Login", "Eco Impact Tracker"
    ]
)

if menu == "Product List":
    product_list.show()

elif menu == "Barcode Lookup":
    barcode_scanner.show()

elif menu == "Nearby Stores":
    dashboard.show()

elif menu == "Compare Products":
    compare_products.show()

elif menu == "Daily Challenges":
    daily_challenges.show()

elif menu == "Coupons":
    coupons.show()

elif menu == "Leaderboard":
    leaderboard.show(sheet)

elif menu == "Eco News":
    eco_news_feed.show()

elif menu == "Login":
    login.show()

elif menu == "Eco Impact Tracker":
    st.header("🌍 Eco-Friendly Product Tracker")

    username = st.session_state.user_id
    if not username:
        st.warning("Please login first to track rewards.")
    else:
        item = st.selectbox("Select an item:", ["Banana", "Milk", "Beef", "Rice", "Bread"])
        quantity = st.number_input("Enter quantity:", min_value=1, step=1)

        if st.button("Calculate Impact"):
            impact = get_carbon_footprint(item, quantity)
            st.info(f"🧮 {quantity} {item}(s) = {impact:.2f} kg CO₂e")
            st.info(get_suggestions(item))

            reward_points = max(0, int(5 - impact))
            st.success(f"🎁 You earned {reward_points} EcoPoints!")

            current = get_rewards(sheet, username)
            total = current + reward_points
            update_rewards(sheet, username, total)
            st.balloons()
            st.success(f"🏅 Your new reward tier: {assign_reward(total)} (Total: {total} Points)")

        if st.button("Show Eco Leaderboard"):
            data = sheet.get_all_records()
            sorted_leaderboard = sorted(data, key=lambda x: x['Points'], reverse=True)
            st.write("## 🏆 Leaderboard")
            st.table(sorted_leaderboard)
