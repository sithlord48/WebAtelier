#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
from flask import Flask, render_template, send_from_directory


parser = argparse.ArgumentParser(description='Atelier Port')
parser.add_argument('--port', type=int, default=8000)
args=parser.parse_args()

app = Flask(__name__)


@app.errorhandler(400)
def bad_request(e):
    print(e)
    return render_template('400.html')


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


@app.route('/documentation/atcore')
def atcore():
    return render_template('atcore.html')


@app.route('/documentation/atelier')
def atelier():
    return render_template('atelier.html')


@app.route('/supportus')
def supportus():
    return render_template('supportus.html')


@app.route('/files/<path:filename>', methods=['GET'])
def download_binaries(filename):
    if 'exe' in filename:
        return send_from_directory(
            'atcore-binaries/windows/', filename, as_attachment=True)


def main():
    app.run(debug=True, port=args.port)


if __name__ == "__main__":
    app.run(debug=True)
