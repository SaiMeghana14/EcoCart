import streamlit as st
from helpers import firebase_rewards

def show():
    st.header("🏅 Leaderboard (EcoPoints)")
    leaderboard = firebase_rewards.get_leaderboard()
    if leaderboard:
        for rank, entry in enumerate(leaderboard, start=1):
            st.write(f"#{rank} — {entry['username']} : {entry['points']} points")
    else:
        st.info("No leaderboard data available.")
