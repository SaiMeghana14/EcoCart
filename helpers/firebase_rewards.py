import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import json

# ✅ Initialize Firebase Firestore
def init_firestore():
    # Convert Streamlit TOML secrets to a valid JSON-style Python dict
    firebase_json = json.loads(json.dumps(dict(st.secrets["firebase"])))
    cred = credentials.Certificate(firebase_json)

    # ✅ Avoid reinitialization in Streamlit reruns
    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred)

    db = firestore.client()
    return db

# ✅ Get Rewards Points for a User
def get_rewards(db, user_id):
    try:
        doc = db.collection("rewards").document(user_id).get()
        if doc.exists:
            data = doc.to_dict()
            return data.get("points", 0)
        else:
            return 0
    except Exception as e:
        st.error(f"⚠️ Error fetching rewards: {e}")
        return 0

# ✅ Update Rewards Points for a User
def update_rewards(db, user_id, points):
    try:
        db.collection("rewards").document(user_id).set({"points": points}, merge=True)
        st.success("✅ Rewards updated successfully!")
    except Exception as e:
        st.error(f"⚠️ Error updating rewards: {e}")

# ✅ Add Leaderboard Points 
def add_to_leaderboard(db, username, points):
    try:
        db.collection("leaderboard").document(username).set({
            "username": username,
            "points": points
        }, merge=True)
        st.success("✅ Leaderboard updated!")
    except Exception as e:
        st.error(f"⚠️ Error updating leaderboard: {e}")
