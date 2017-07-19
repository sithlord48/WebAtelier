#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template

#Init Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/download')
def download():
    return render_template('download.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/documentation')
def documentation():
    return render_template('documentation.html')



if __name__ == "__main__":
    app.run(debug=True)
