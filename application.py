from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Opening page will be dashboard"""

    return render_template('index.html')
