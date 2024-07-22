# app/routes.py
from app import app
from app.scheduler import global_data
from flask import jsonify

@app.route('/')
def home():
    return "Hello, Flask!"


@app.route('/sports')
def get_sports():
    print(global_data['sports'])
    return jsonify(global_data['sports'])

@app.route('/world')
def get_world():
    return jsonify(global_data['world'])

@app.route('/science')
def get_science():
    return jsonify(global_data['science'])

@app.route('/politics')
def get_politics():
    return jsonify(global_data['politics'])
