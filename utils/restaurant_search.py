import requests
from config import RESTAURANT_API_KEY

def find_restaurants(dish_name):
    api_url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': f'Bearer {RESTAURANT_API_KEY}'}
    params = {
        'term': dish_name,
        'location': 'Boston, MA',  # Replace with dynamic location data as needed
        'limit': 5
    }
    response = requests.get(api_url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get('businesses', [])
    return []
