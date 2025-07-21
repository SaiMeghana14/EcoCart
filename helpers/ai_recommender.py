import requests

HUGGINGFACE_TOKEN = "YOUR_HUGGINGFACE_TOKEN"
API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"}

def get_embedding(text):
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": text})
    response.raise_for_status()
    return response.json()[0]  # return first vector

def recommend(user_pref, products):
    user_vec = get_embedding(user_pref)
    recommendations = []
    for product in products:
        product_vec = get_embedding(product["name"])
        similarity = sum(u * p for u, p in zip(user_vec, product_vec))
        recommendations.append((product["name"], similarity))
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations[:3]
