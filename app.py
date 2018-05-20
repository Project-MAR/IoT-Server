from flask import Flask, request, abort, make_response
from flask_httpauth import HTTPBasicAuth

import requests, json

app = Flask(__name__)

@app.route('/')
def index():
	return 'OK'

@app.route('/hello', methods=['GET'])
def hello():
	username = request.args.get('name')
	return 'hello ' + username

@app.route('/callback', methods=['POST'])
def callback():
    payload     = request.get_json()
    json_string = json.dumps(payload)
    data_dict   = json.loads(json_string)

    user_name = data_dict['name']
    user_id   = data_dict['id']
    user_message = data_dict['message']

    result = 'json string: ' + json_string + '\n'
    result = result + 'user id: ' + user_id + '\n'
    result = result + 'user name: ' + user_name + '\n'
    result = result + 'user message: ' + user_message 

    return result

if __name__ == "__main__":
	app.run()
