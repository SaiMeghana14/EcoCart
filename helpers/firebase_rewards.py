import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("backend/firebaseServiceAccount.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def get_rewards(user_id):
    doc = db.collection("rewards").document(user_id).get()
    return doc.to_dict().get("points", 0) if doc.exists else 0

def get_leaderboard():
    leaderboard = db.collection("leaderboard").order_by("points", direction=firestore.Query.DESCENDING).limit(5).stream()
    return [{"username": doc.id, **doc.to_dict()} for doc in leaderboard]
