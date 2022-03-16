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


@app.route('/api/smartinfra1')
def smart_infra_1():
    print('api smart infra1 is executing')

    response_body = {'username': 'tawatchai', 'status': 'ok'}
    reseponse = jsonify(response_body)
    reseponse.headers.add('Access-Control-Allow-Origin', '*')
    return reseponse


@app.route('/postexample', methods=['POST'])
def precheck():
    print('postexample is executing')
    # body = request.get_json()
    # device_id = body["deviceId"]
    return_body = {'test_return_key': 'test_return_value'}
    return jsonify(return_body)
