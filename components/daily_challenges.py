import streamlit as st

def show():
    st.header("🏆 Daily Eco Challenges")
    challenges = [
        "✅ Avoid Plastic Today",
        "✅ Buy Local Produce",
        "✅ Walk/Cycle instead of Car",
        "✅ Eat Plant-Based Meal Today"
    ]
    for challenge in challenges:
        st.write(challenge)
