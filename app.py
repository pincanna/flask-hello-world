from flask import Flask
from uuid import uuid4

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/uuid4')
def get_uuid4():
    return {'value': str(uuid4())}
