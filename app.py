from flask import Flask, render_template, request, redirect, url_for
from utils.image_recognition import recognize_dish
from utils.restaurant_recommend import recommend_restaurants
from utils.review_system import save_review, get_reviews
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/images/'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        location = request.form.get('location')
        preferences = {
            'budget': request.form.get('budget'),
            'cuisine_type': request.form.get('cuisine_type')
        }

        if file and file.filename:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Recognize the dish
            dish_name = recognize_dish(filepath)
            if dish_name:
                # Recommend restaurants based on the recognized dish
                restaurants = recommend_restaurants(dish_name, location, preferences)
                return render_template('results.html', dish=dish_name, restaurants=restaurants)
            else:
                return render_template('index.html', error="Dish not recognized.")
    
    return render_template('index.html')

@app.route('/add_review', methods=['POST'])
def add_review():
    restaurant_id = request.form.get('restaurant_id')
    user_review = request.form.get('review')
    save_review(restaurant_id, user_review)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
