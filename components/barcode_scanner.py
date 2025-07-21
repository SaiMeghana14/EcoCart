import streamlit as st
from helpers import openfood_lookup

def show():
    st.header("📲 Barcode Lookup via OpenFoodFacts")
    barcode = st.text_input("Enter barcode number:")
    if st.button("Lookup Product"):
        product = openfood_lookup.lookup(barcode)
        if product:
            st.success(f"Product Found: {product['product_name']}")
            st.image(product.get('image_url', ''), width=150)
            st.json(product)
        else:
            st.error("Product not found!")
