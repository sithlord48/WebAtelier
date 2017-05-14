#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template

#Init Flask
app = Flask(__name__)
app.config.from_pyfile('config.cfg', silent=True)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
