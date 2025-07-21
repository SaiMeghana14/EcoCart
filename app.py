import streamlit as st
from components import (
    product_list, barcode_scanner, dashboard, compare_products,
    coupons, daily_challenges, eco_news_feed, login, leaderboard
)
from helpers import firebase_rewards

# ✅ Initialize Firebase Firestore
db = firebase_rewards.init_firestore()

# ✅ Streamlit App Config
st.set_page_config(page_title="EcoCart Streamlit", layout="wide")
st.title("🛒 EcoCart – Sustainable Smart Shopping Assistant (Streamlit Edition)")

# ✅ Sidebar Navigation
menu = st.sidebar.radio(
    "Navigate", 
    ["Product List", "Barcode Lookup", "Nearby Stores", "Compare Products", 
     "Daily Challenges", "Coupons", "Leaderboard", "Eco News", "Login"]
)

# ✅ Optional: Display Points if Logged In
if 'user_id' in st.session_state:
    user_id = st.session_state.user_id
    points = firebase_rewards.get_rewards(db, user_id)
    st.sidebar.success(f"🎁 Points: {points}")

# ✅ Routing
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
