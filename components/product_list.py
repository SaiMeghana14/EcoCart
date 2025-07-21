import streamlit as st
import json
from helpers import eco_score

def show():
    st.header("🛒 Product List with Eco-Score")
    with open('data/products.json') as f:
        products = json.load(f)
    for product in products:
        score = eco_score.calculate(product)
        st.markdown(f"**{product['name']}** – Eco Score: :green[{score}]")
        st.caption(product.get("description", ""))
