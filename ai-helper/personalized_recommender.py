import requests

API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
HEADERS = {"Authorization": "Bearer YOUR_HF_TOKEN"}

def get_embedding(text):
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": text})
    return response.json()

# Example Personalized Recommender
def recommend(user_history, products):
    history_embedding = get_embedding(user_history)["embeddings"][0]
    product_scores = []
    for product in products:
        product_embedding = get_embedding(product["name"])["embeddings"][0]
        score = sum(h * p for h, p in zip(history_embedding, product_embedding))
        product_scores.append((product, score))
    recommended = sorted(product_scores, key=lambda x: x[1], reverse=True)[:3]
    return [r[0] for r in recommended]

if __name__ == '__main__':
    print("Personalized recommendation demo")
