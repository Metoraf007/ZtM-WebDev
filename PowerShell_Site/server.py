from flask import Flask, flash, escape, request, render_template, send_from_directory, redirect, url_for
from os import path
from pathlib import Path
from urllib.request import urlopen
from werkzeug.utils import secure_filename
import csv
import json
import time

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/thankyou.html')
def return_thankyou_page():
        email = request.args.get('email')
        return render_template('/thankyou.html', email=email)

@app.route('/<string:page_name>')
def return_index_page(page_name):
    pages = page_list()
    if page_name.lower() in pages:
        return render_template(page_name)
    else:
        return render_template('/error.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(path.join(app.root_path, 'static'),
                               'logo.png', mimetype='image/vnd.microsoft.icon')

def page_list():
    return ['index.html', 'psworkplan.html', 'cheatsheet.html', 'psscripts.html', 'splunkscripts.html', 'carousel.html', 'page_template.html']

