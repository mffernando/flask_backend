from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'name' : 'Fernando'}
    products = [{'name': 'milk'}, {'name' : 'rice'}]
    return render_template('index.html', title='Home', user=user, products=products)