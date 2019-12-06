import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<H1>Hello there</H1>"

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')),debug=True)        