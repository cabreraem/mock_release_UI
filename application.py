from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Opening page will be dashboard"""

    fake ={"version" : "xxx-xxx-xxx", "status" : True, "creation" : "mm/dd/yy at hh:mm:ss", "last_mod" : "mm/dd/yy at hh:mm:ss", "last_active" : "task123", "tag" : 1}

    fakeData = [fake]


    return render_template('index.html', releases=fakeData)

@app.route('/details')
def details():
    return render_template('details.html')
