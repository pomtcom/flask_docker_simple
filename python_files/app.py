from flask import Flask, redirect, request, json, jsonify

app = Flask(__name__)

@app.route('/healthcheck')
def healthcheck():
   return 'healthcheck is working'

@app.route('/welcomepage')
def welcome_page():
    return 'Welcome page is working'

@app.route('/')
def hello_world():
   return 'hello world'


@app.route('/postexample', methods=['POST'])
def precheck():
    print('postexample is executing')
    # body = request.get_json()
    # device_id = body["deviceId"]
    return_body = {'test_return_key': 'test_return_value'}
    return jsonify(return_body)