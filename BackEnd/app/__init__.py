# app/__init__.py
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from app.scheduler import start_scheduler, task 
task()
start_scheduler()

from app import routes
