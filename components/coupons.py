import streamlit as st

def show():
    st.header("🎁 Available Eco-Friendly Coupons")
    coupons = [
        {"code": "ECO10", "description": "10% off on sustainable items"},
        {"code": "GREEN20", "description": "20% discount on eco-friendly brands"}
    ]
    for coupon in coupons:
        st.markdown(f"**{coupon['code']}**: {coupon['description']}")
