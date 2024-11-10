import json

def save_review(restaurant_id, user_review):
    # Mock database or JSON storage
    with open('reviews.json', 'r+') as file:
        reviews = json.load(file)
        reviews[restaurant_id] = reviews.get(restaurant_id, []) + [user_review]
        file.seek(0)
        json.dump(reviews, file)

def get_reviews(restaurant_id):
    with open('reviews.json', 'r') as file:
        reviews = json.load(file)
        return reviews.get(restaurant_id, [])
