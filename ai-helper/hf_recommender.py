```python
import requests

API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
headers = {"Authorization": f"Bearer YOUR_HF_TOKEN"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json={"inputs": payload})
    return response.json()

if __name__ == "__main__":
    print(query("Suggest eco-friendly alternatives for plastic bottles"))
