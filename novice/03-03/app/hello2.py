from turtle import update
from flask import Flask, url_for, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login',  methods=['GET', 'POST'])
def login():
    print(request.method)
    return 'login'

@app.route('/user/<username>')
def profile(username):
    print(request)
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

if __name__ == "__main__":
    app.run()

'''
Create = POST
Read   = GET
update = PUT
Delete = DELETE
'''