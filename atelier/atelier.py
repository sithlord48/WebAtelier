#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template

#Init Flask
app = Flask(__name__)
app.config.from_pyfile('config.cfg', silent=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')


if __name__ == "__main__":
    app.run(debug=True)
