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
        filter_by = request.form['filter_by']
        lower_bound = request.form['lower_bound']
        upper_bound = request.form['upper_bound']

    elif request.method == "GET":
        lookup_code = request.args.get('lookup_code')
        filter_by = request.args.get('filter_by')
        lower_bound = request.args.get('lower_bound')
        upper_bound = request.args.get('upper_bound')

    if lower_bound == '':
        lower_bound = 0

    if upper_bound == '':
        upper_bound = 99999999999

    if filter_by == 'price':
        items = db.session.query(Product).filter(Product.item_lookup_code.like('%' + lookup_code + '%'), Product.price.between(float(lower_bound), float(upper_bound))).all()
    elif filter_by == 'cost':
        items = db.session.query(Product).filter(Product.item_lookup_code.like('%' + lookup_code + '%'), Product.cost.between(float(lower_bound), float(upper_bound))).all()
    elif filter_by == 'msrp':
        items = db.session.query(Product).filter(Product.item_lookup_code.like('%' + lookup_code + '%'), Product.msrp.between(float(lower_bound), float(upper_bound))).all()

    return render_template('results.html', items = items)
