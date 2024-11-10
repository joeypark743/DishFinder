import requests
from config import RESTAURANT_API_KEY

def recommend_restaurants(dish_name, location, preferences):
    api_url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': f'Bearer {RESTAURANT_API_KEY}'}
    params = {
        'term': dish_name,
        'location': location,
        'limit': 5,
        'price': preferences.get('budget', '1,2,3,4'),
        'categories': preferences.get('cuisine_type', '')
    }
    response = requests.get(api_url, headers=headers, params=params)
    return response.json().get('businesses', []) if response.status_code == 200 else []
