from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    """Opening page will be dashboard"""

    return render_template('index.html')

@app.route('/details')
def details():
    return render_template('details.html')
