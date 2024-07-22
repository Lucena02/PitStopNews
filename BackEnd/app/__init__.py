# app/__init__.py
from flask import Flask

app = Flask(__name__)

from app.scheduler import start_scheduler
start_scheduler()

from app import routes
