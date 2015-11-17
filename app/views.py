from app import app, db
from flask import Flask, render_template, request
from models import *
import random

@app.route('/')
def index():
    return render_template('search.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    lookup_code = None
    if request.method == 'POST':
        lookup_code = request.form['lookup_code']

    elif request.method == "GET":
        lookup_code = request.args.get('lookup_code')

    if lookup_code == None:
        return "please enter lookup code"    

    item = db.session.query(Product).filter_by(item_lookup_code = lookup_code).first()

    if item == None:
        return render_template('results.html')

    if item.inactive == "0":
        return render_template('results.html', lookup_code=item.item_lookup_code, description=item.description, price=str(item.price), quantity=str(item.quantity), active="True")

    else:
        return render_template('results.html', lookup_code=item.item_lookup_code, description=item.description, price=str(item.price), quantity=str(item.quantity), active="False") 