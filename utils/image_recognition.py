import requests
from config import FOOD_IMAGE_API_KEY

def recognize_dish(image_path):
    api_url = 'https://api.logmeal.es/v2/recognition/dish'
    headers = {'Authorization': f'Bearer {FOOD_IMAGE_API_KEY}'}
    with open(image_path, 'rb') as image_file:
        response = requests.post(api_url, headers=headers, files={'image': image_file})
    if response.status_code == 200:
        data = response.json()
        return data.get('dish')
    return None
