import os
from flask import Flask, redirect

app = Flask(__name__)
messages = []

def add_message(username, message):
    """add messages to the list"""
    messages.append("{}: {}".format(username, message))

def get_all_message():
    """Gets all messages and seperates with a break"""   
    return "<br>".join(messages) 

@app.route('/')
def index():
    """Main Page with instructions"""
    return "To send a message use /USERNAME/MESSAGE"

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