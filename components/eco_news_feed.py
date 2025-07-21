import streamlit as st

def show():
    st.header("📰 Eco-Friendly News Feed")
    st.markdown("Fetching eco-friendly news headlines (static demo):")
    news = [
        "🌱 Plastic-Free July Gains Global Traction",
        "🚴‍♀️ Cities Promote Cycling for Greener Commutes",
        "🥗 Plant-Based Diets Lower Carbon Footprint"
    ]
    for n in news:
        st.write(n)
