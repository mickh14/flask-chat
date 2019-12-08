import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "random123"
messages = []

def add_message(username, message):
    """add messages to the list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append("({}) {}: {}".format(now, username, message))

def get_all_message():
    """Gets all messages and seperates with a break"""   
    return "<br>".join(messages) 

@app.route('/', methods =["GET", "POST"])
def index():
    """Main Page with instructions"""
    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(session["username"])   
    return render_template("index.html")

@app.route('/<username>')
def user(username):
    """Display Chat Messages"""
    return "<H1>Welcome, {0}</H1>{1}".format(username, get_all_message())

@app.route('/<username>/<message>')
def send_message(username, message):
    "Create a new message and redirect back to the chat page"
    add_message(username, message)
    return redirect("/" + username)

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')),debug=True)           