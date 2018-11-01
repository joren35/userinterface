from flask import Flask, jsonify, request, session, render_template, url_for, redirect
import requests, json
import flask, sys, os

app = Flask(__name__)
app.secret_key = 'celeron0912'
# app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    params = request.get_json()
    username = params["username"]
    password = params["password"]
    headers = {'content-type': 'application/json; charset=utf-8', 'dataType': "json"}
    resp = requests.post("http://localhost:8080/login", headers=headers, json={'username': username, 'password': password})
    data = resp.json()
    if "error" in data['status']:
        return jsonify(resp.json())
    else:
        session['user'] = data['status']
        return jsonify(resp.json())

@app.route('/register/<string:username>/<string:name>/<string:fname>/<string:password>/<string:mobnum>/<string:admin_prev>')
def register(username,name,fname,password,mobnum,admin_prev):
    print("test")

@app.route('/dashboard', methods=['GET'])
def landing_page():
    headers = {'dataType': "json"}
    resp = requests.get("http://localhost:8080/dashboard/"+str(session['user'])+"", headers=headers)
    data = resp.json()
    if data['entries'][0]['admin_prev'] == 'False':
        print 'False but true'
    else:
        print 'True'
    return jsonify(resp.json())

@app.after_request
def add_cors(resp):
    resp.headers['Access-Control-Allow-Origin'] = flask.request.headers.get(
        'Origin', '*')
    resp.headers['Access-Control-Allow-Credentials'] = True
    resp.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS, GET, PUT, DELETE'
    resp.headers['Access-Control-Allow-Headers'] = flask.request.headers.get('Access-Control-Request-Headers',
                                                                             'Authorization')

    # set low for debugging

    if app.debug:
        resp.headers["Access-Control-Max-Age"] = '1'
    return resp


if __name__ == '__main__':
    app.run(debug=True)