#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template

#Init Flask
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template('404.html')

@app.errorhandler(500)
def internal_server_error(e):
    print(e)
    return render_template('500.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/download')
def download():
    return render_template('download.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/documentation')
def documentation():
    return render_template('documentation.html')

@app.route('/supportus')
def supportus():
    return render_template('supportus.html')



if __name__ == "__main__":
    app.run(debug=True)
