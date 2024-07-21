from app import app
import csv
import datetime
import os




@app.route('/')
def home():
    return "Hello, Flask!"

