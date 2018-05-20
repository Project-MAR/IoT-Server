from flask import Flask, request, abort, make_response
from flask_httpauth import HTTPBasicAuth

import requests, json

app = Flask(__name__)

@app.route('/')
def index():
	return 'OK'

if __name__ == "__main__":
	app.run()
	