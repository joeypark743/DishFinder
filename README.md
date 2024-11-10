# DishFinder 🍽️

DishFinder is a web application that uses image recognition to identify dishes from uploaded food photos and recommends nearby restaurants where the dish can be enjoyed. This project combines AI-based food image recognition, personalized restaurant recommendations, and interactive map integration for a complete user experience.

## Features

- **Dish Recognition**: Upload a food image to identify the dish using an AI-powered image recognition API.
- **Restaurant Recommendations**: Get a list of nearby restaurants serving the recognized dish, filtered by user preferences such as budget and cuisine type.
- **Interactive Maps**: See restaurant locations on an interactive Google Map centered on the user's location or a default location in Boston, Kenmore.
- **User Reviews**: Users can leave and view reviews for recommended restaurants.
- **Real-Time Feedback**: Provides instant feedback for dish recognition using WebSocket integration.

## Tech Stack

- **Backend**: Python, Flask, SocketIO
- **Frontend**: HTML, CSS, JavaScript, Google Maps API
- **APIs**: LogMeal (for dish recognition), Yelp API (for restaurant recommendations)

## Getting Started

### Prerequisites

1. **Python 3.8+**
2. **Virtual Environment**: Install `venv` to manage dependencies.
3. **API Keys**:
   - LogMeal API Key for food image recognition.
   - Yelp API Key or Google Places API Key for restaurant recommendations.

### Installation

1. **Clone the Repository**:
   ```
   git clone https://github.com/your-username/DishFinder.git  
   cd DishFinder
    ```
2. **Create a Virtual Environment**:
   ```
   python3 -m venv venv  
   source venv/bin/activate
    ```
3. **Install Dependencies**:
    ```
   pip install -r requirements.txt
    ```
4. **Set Up API Keys**:
   - Create a `config.py` file in the project root to store API keys.
   - Add the following content to `config.py`:
   
     # config.py  
     ```
     FOOD_IMAGE_API_KEY = 'your_logmeal_api_key_here'  
     RESTAURANT_API_KEY = 'your_yelp_or_google_places_api_key_here'
     ```

### Running the Application

1. **Start the Flask Server**:
   ```
   python app.py
   ```

2. **Access the Application**:
   Open a browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Project Structure
```
DishFinder/  
├── app.py                     # Main Flask application  
├── config.py                  # API keys and configuration settings  
├── requirements.txt           # Project dependencies  
├── static/  
│   ├── css/  
│   │   └── styles.css         # Custom CSS for styling  
│   ├── images/                # Folder for user-uploaded images  
│   └── js/  
│       ├── main.js            # JavaScript for handling file upload, real-time feedback  
│       └── map.js             # JavaScript for initializing and controlling Google Maps  
├── templates/  
│   ├── index.html             # Main upload page for users  
│   └── results.html           # Results page displaying identified dish and restaurant recommendations  
├── utils/  
│   ├── __init__.py  
│   ├── image_recognition.py   # Image recognition logic  
│   ├── restaurant_recommend.py# Fetches nearby restaurants from Yelp/Google Places API  
│   └── review_system.py       # Handles storing and retrieving user reviews  
└── README.md                  # Project documentation  
```

## Usage

1. **Upload a Food Image**: On the home page, upload an image of a dish.
2. **View Dish and Restaurants**: After recognizing the dish, view nearby restaurant recommendations.
3. **Interact with Map**: Use the interactive map to explore the location of recommended restaurants.
4. **Leave a Review**: Add your review for any recommended restaurant.

## APIs Used

- **LogMeal API**: Recognizes food items from images, returning a dish name and ingredients.
- **Yelp or Google Places API**: Retrieves nearby restaurants based on the recognized dish, user’s location, and preferences.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **LogMeal** for food recognition.
- **Yelp API / Google Places API** for restaurant data.
- Inspired by open-source project: [Recipe Generation from Food Image](https://github.com/navassherif98/Recipe-Generation-from-Food-Image)
