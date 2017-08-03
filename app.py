from flask import Flask, url_for, request, render_template, Markup
from flask_mongoengine import MongoEngine
app = Flask(__name__)
app.config.from_pyfile('the-config.cfg')
db = MongoEngine(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about/')
def about():
	return render_template('about.html')

@app.route('/portfolio/')
def portfolio():
	return render_template('portfolio.html')