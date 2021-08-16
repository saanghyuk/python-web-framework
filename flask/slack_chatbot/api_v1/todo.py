from flask import json, jsonify
from flask import request
import requests
from .__init__ import api


@api.route('/todos', methods=['GET', 'POST'])
def todos():
    print("TEST")
    if request.method == 'POST':
        res = requests.post('https://hooks.slack.com/services/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', json={
            'text': 'Hello World'
        }, headers={'Content-Type': 'application/json'})
    elif request.method == 'GET':
        pass

    data = request.get_json()
    return jsonify(data)


@api.route('/test', methods=['POST'])
def test():
    res = request.form['text']
    print(res)
    return jsonify(res)
