#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from flask import Flask, jsonify
import pandas as pd
import json
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
df= None 
@app.route('/')
def index():
    global df
    if not sys.stdin.isatty():
        if(df is None or len(df)==0):
            s = sys.stdin
            df = pd.read_csv(s)
            return jsonify(json.loads(df.to_json()))
        else:
            return jsonify(json.loads(df.to_json()))
    else:
        return "nothing"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)
