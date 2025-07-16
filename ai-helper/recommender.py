```python
def recommend_alternatives(product_name):
    alternatives = {
        "Toothpaste": "Eco-friendly Herbal Toothpaste",
        "Shampoo": "Organic Aloe Vera Shampoo"
    }
    for keyword in alternatives:
        if keyword.lower() in product_name.lower():
            return alternatives[keyword]
    return "No eco-friendly alternative found"

if __name__ == "__main__":
    print(recommend_alternatives("Toothpaste"))
```