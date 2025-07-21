import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

def init_firestore():
    firebase_dict = st.secrets["firebase"].to_dict()
    cred = credentials.Certificate(firebase_dict)
    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred)
    return firestore.client()

def get_rewards(db, user_id):
    try:
        doc = db.collection('rewards').document(user_id).get()
        if doc.exists:
            return doc.to_dict().get('points', 0)
        else:
            return 0
    except Exception as e:
        st.error(f"Failed to fetch rewards: {e}")
        return 0

def update_rewards(db, user_id, points):
    try:
        db.collection('rewards').document(user_id).set({"points": points}, merge=True)
        return True
    except Exception as e:
        st.error(f"Failed to update rewards: {e}")
        return False

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
