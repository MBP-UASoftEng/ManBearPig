from app import app, db
from flask import Flask, render_template, request
from models import *
import random

@app.route('/')
def index():
    return render_template('search.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    return render_template('results.html', lookup_code="dummy_data", description="dummy_data", price="dummy_data", quantity="dummy_data", active="dummy_data")