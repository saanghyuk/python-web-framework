import enum
from flask import json, jsonify
from flask import request
import requests
from .__init__ import api
from models import db
from models import Todo
import datetime


def send_slack(msg):
    res = requests.post('https://hooks.slack.com/services/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', json={
        'text': msg
    }, headers={'Content-Type': 'application/json'})
    print("SEND_SLACK FUNCTION IS CALLED")
    print(res)


@api.route('/todos', methods=['GET', 'POST'])
def todos():
    if request.method == 'POST':
        # CREATING CODE
        send_slack("TODO IS CREATED")
    elif request.method == 'GET':
        pass

    data = request.get_json()
    return jsonify(data)


@api.route('/slack/todos', methods=['POST'])
def slack_todos():
    res = request.form['text'].split(' ')
    cmd, *args = res

    ret_msg = ''

    if cmd == "create":
        todo_name = args[0]
        todo = Todo()
        todo.title = todo_name
        db.session.add(todo)
        db.session.commit()
        ret_msg = 'TODO IS CREATED'
        send_slack("[%s] %s" % (str(datetime.datetime.now()), todo_name))

    elif cmd == "list":
        todos = Todo.query.all()
        for idx, todo in enumerate(todos):
            ret_msg += '%d. %s (%s) \n' % (idx+1, todo.title, str(todo.tstamp))

    return ret_msg
