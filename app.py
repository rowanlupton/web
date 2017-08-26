from flask import Flask, url_for, request, render_template, Markup
app = Flask(__name__)

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