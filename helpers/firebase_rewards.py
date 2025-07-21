import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import json

# ✅ Initialize Firebase Firestore using secrets.toml 'firebase' key
def init_firestore():
    # Load the JSON string from secrets.toml
    firebase_json = st.secrets["firebase"]
    firebase_dict = json.loads(firebase_json)

    # Initialize Firebase App (avoids duplicate initialization in Streamlit reruns)
    if not firebase_admin._apps:
        cred = credentials.Certificate(firebase_dict)
        firebase_admin.initialize_app(cred)

    return firestore.client()

# ✅ Get rewards points for a user
def get_rewards(db, user_id):
    try:
        doc = db.collection("rewards").document(user_id).get()
        if doc.exists:
            return doc.to_dict().get("points", 0)
        else:
            return 0
    except Exception as e:
        st.error(f"⚠️ Error fetching rewards: {e}")
        return 0

# ✅ Update rewards points for a user
def update_rewards(db, user_id, points):
    try:
        db.collection("rewards").document(user_id).set({"points": points}, merge=True)
        st.success("✅ Rewards updated successfully!")
    except Exception as e:
        st.error(f"⚠️ Error updating rewards: {e}")

# ✅ Update leaderboard (optional)
def add_to_leaderboard(db, username, points):
    try:
        db.collection("leaderboard").document(username).set({
            "username": username,
            "points": points
        }, merge=True)
        st.success("✅ Leaderboard updated!")
    except Exception as e:
        st.error(f"⚠️ Error updating leaderboard: {e}")
