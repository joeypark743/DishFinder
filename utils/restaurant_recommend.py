def recommend_restaurants(dish_name, location, preferences):
    params = {
        'term': dish_name,
        'location': location,
        'limit': 5,
        'price': preferences['budget'],
        'categories': preferences['cuisine_type'],
    }
    response = requests.get(api_url, headers=headers, params=params)
    return response.json().get('businesses', [])
