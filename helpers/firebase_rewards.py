import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import json

def init_firestore():
    # Convert TOML secret to clean JSON dict
    firebase_json = json.loads(json.dumps(dict(st.secrets["firebase"])))
    cred = credentials.Certificate(firebase_json)
    app = firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db

def get_rewards(db, user_id):
    doc = db.collection("rewards").document(user_id).get()
    if doc.exists:
        return doc.to_dict().get("points", 0)
    else:
        return 0

def get_leaderboard(db):
    leaderboard_ref = db.collection("leaderboard").order_by("points", direction=firestore.Query.DESCENDING).limit(5).stream()
    return [{"username": doc.id, **doc.to_dict()} for doc in leaderboard_ref]
