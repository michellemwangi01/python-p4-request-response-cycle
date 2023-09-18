#!/usr/bin/env python3
import os
from flask import Flask, request, current_app, g, make_response

app = Flask(__name__)


@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())


@app.route('/')
def index():
    host_name = request.headers.get('Host')
    appname = current_app.name
    response_body =  f'''<h1>The host for this page is {host_name}</h1>
            <h1>The name of this application is {appname}</h1>
            <h1>The path of this application is {g.path}</h1>''', 202
    status_code = 202
    headers = {}

    return  make_response(response_body, status_code, headers)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
