#!/usr/bin/env python
from importlib import import_module
import os
import json
from libs.drive import drive as dr

from flask import Flask, render_template, Response, request

app = Flask(__name__)


@app.route('/')
def index():
    """Drive Home Page."""
    return render_template('index.html')


@app.route('/drive')
def drive():
    """Drive Home Page."""
    direction = request.args.get('q')
    print(direction)
    dr(direction)
    return json.dumps({"success": True})


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, debug=True)
