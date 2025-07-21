import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# ✅ Initialize Firestore connection
def init_firestore():
    # ✅ Convert Streamlit SecretsDict to a plain dict
    firebase_dict = dict(st.secrets["firebase"])

    # ✅ Prevent multiple initializations on rerun
    if not firebase_admin._apps:
        cred = credentials.Certificate(firebase_dict)
        firebase_admin.initialize_app(cred)

    db = firestore.client()
    return db

# ✅ Get rewards points for a user (returns int)
def get_rewards(db, user_id):
    try:
        doc = db.collection("rewards").document(user_id).get()
        if doc.exists:
            return doc.to_dict().get("points", 0)
        else:
            return 0
    except Exception as e:
        st.error(f"⚠️ Failed to fetch rewards: {e}")
        return 0

# ✅ Update rewards points for a user
def update_rewards(db, user_id, points):
    try:
        db.collection("rewards").document(user_id).set({"points": points}, merge=True)
        st.success("✅ Rewards updated!")
    except Exception as e:
        st.error(f"⚠️ Failed to update rewards: {e}")

# ✅ Update leaderboard with username and points
def add_to_leaderboard(db, username, points):
    try:
        db.collection("leaderboard").document(username).set({
            "username": username,
            "points": points
        }, merge=True)
        st.success("✅ Leaderboard updated!")
    except Exception as e:
        st.error(f"⚠️ Failed to update leaderboard: {e}")
