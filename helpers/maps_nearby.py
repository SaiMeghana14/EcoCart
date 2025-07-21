import requests
GOOGLE_API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"

def find_nearby(lat, lng):
    radius = 5000
    keyword = "organic|eco|sustainable"
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&keyword={keyword}&key={GOOGLE_API_KEY}"
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        return data.get("results", [])
    return []
