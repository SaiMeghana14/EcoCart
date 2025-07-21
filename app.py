import streamlit as st
from components import (
    product_list, barcode_scanner, dashboard, compare_products,
    coupons, daily_challenges, eco_news_feed, login, leaderboard
)
from helpers import firebase_rewards

# ✅ Initialize Firebase
db = firebase_rewards.init_firestore()

# ✅ Session state setup
if "user_id" not in st.session_state:
    st.session_state.user_id = None

st.set_page_config(page_title="EcoCart Streamlit", layout="wide")

st.title("🛒 EcoCart – Sustainable Smart Shopping Assistant (Streamlit Edition)")

if st.session_state.user_id:
    points = firebase_rewards.get_rewards(db, st.session_state.user_id)
    st.sidebar.success(f"Logged in as: {st.session_state.user_id}")
    st.sidebar.info(f"🌱 Your Eco Points: {points}")
else:
    st.sidebar.warning("Not logged in. Login to track your points.")

menu = st.sidebar.radio(
    "Navigate", 
    ["Product List", "Barcode Lookup", "Nearby Stores", "Compare Products", 
     "Daily Challenges", "Coupons", "Leaderboard", "Eco News", "Login"]
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
    leaderboard.show()

elif menu == "Eco News":
    eco_news_feed.show()

elif menu == "Login":
    login.show()
