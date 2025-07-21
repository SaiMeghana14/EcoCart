import streamlit as st
from helpers import maps_nearby

def show():
    st.header("🌍 Nearby Eco-Friendly Stores (Google Maps)")
    lat = st.text_input("Latitude:")
    lng = st.text_input("Longitude:")
    if st.button("Find Nearby Stores"):
        stores = maps_nearby.find_nearby(lat, lng)
        if stores:
            for store in stores:
                st.write(f"🏪 {store['name']} - Rating: {store.get('rating', 'N/A')}")
        else:
            st.error("No nearby eco-friendly stores found.")
