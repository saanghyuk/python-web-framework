import enum
from flask import json, jsonify
from flask import request, session
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


@api.route('/todos', methods=['GET', 'POST', 'DELETE'])
def todos():
    userid = session.get('userid', None)
    if not userid:
        return jsonify(), 401
    if request.method == 'POST':
      # For Test
      # curl -X POST -H 'Content-type:application/json' --data '{"title":"test"}' http://127.0.0.1:5000/api/v1/todos

        data = request.get_json()
        todo = Todo()
        title = data.get('title')
        todo.user_id = userid
        todo.title = title
        db.session.add(todo)
        db.session.commit()
        send_slack("TODO IS CREATED")

        return jsonify(), 201

    elif request.method == 'GET':
        todos = Todo.query.filter_by(user_id=userid)
        todo_list = [todo.serialize for todo in todos]
        return jsonify(todo_list), 201

    elif request.method == 'DELETE':
        # FOR TEST
        # curl -X DELETE -H 'Content-type:application/json' --data '{"todo_id":2}' http://127.0.0.1:5000/api/v1/todos
        data = request.get_json()
        todo_id = data.get('todo_id')
        todo = Todo.query.filter_by(id=todo_id).first()
        print(todo)
        db.session.delete(todo)
        db.session.commit()
        return jsonify(), 203


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
