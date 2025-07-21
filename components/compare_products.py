import streamlit as st
import json
from helpers import eco_score

def show():
    st.header("🔍 Compare Product Eco-Scores")
    with open('data/products.json') as f:
        products = json.load(f)

    options = [p['name'] for p in products]
    prod1 = st.selectbox("Choose First Product", options)
    prod2 = st.selectbox("Choose Second Product", options)

    if st.button("Compare"):
        p1 = next(p for p in products if p["name"] == prod1)
        p2 = next(p for p in products if p["name"] == prod2)
        s1 = eco_score.calculate(p1)
        s2 = eco_score.calculate(p2)
        st.write(f"✅ {prod1}: Eco-Score = {s1}")
        st.write(f"✅ {prod2}: Eco-Score = {s2}")
