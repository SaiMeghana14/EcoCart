def calculate(product):
    score = 100
    if 'plastic' in product.get('material', '').lower():
        score -= 30
    if product.get('origin', '').lower() != 'local':
        score -= 20
    if product.get('packaging', '').lower() in ['plastic', 'non-recyclable']:
        score -= 20
    return max(score, 0)
