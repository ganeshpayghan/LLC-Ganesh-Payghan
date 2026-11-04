from flask import render_template, request
from app import app
from app.bio_generator import get_biography

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    person = request.values.get('search', '')
    data = get_biography(person)
    return render_template('result.html', person=person, data=data)
