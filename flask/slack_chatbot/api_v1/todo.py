import enum
from flask import json, jsonify
from flask import request, session
import requests
from .__init__ import api
from models import db
from models import Todo, User
import datetime


def send_slack(msg):
    res = requests.post('https://hooks.slack.com/services/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', json={
        'text': msg
    }, headers={'Content-Type': 'application/json'})
    print("SEND_SLACK FUNCTION IS CALLED")
    print(res)


@api.route('/todos/done', methods=['PUT'])
def todos_done():
    userid = session.get('userid', 1)
    if not userid:
        return jsonify(), 401
    data = request.get_json()
    todo_id = data.get('todo_id')
    user = User.query.filter_by(id=userid).first()
    todo = Todo.query.filter_by(id=todo_id).first()

    if todo.user_id != user.id:
        return jsonify(), 400
    todo.status = 1
    db.session.commit()
    send_slack("TODO IS COMPLETED\nUSER: %s \nTITLE: %s" %
               (user.userid, todo.title))

    return jsonify()


@api.route('/todos', methods=['GET', 'POST', 'DELETE'])
def todos():
    userid = session.get('userid', 1)
    if not userid:
        return jsonify(), 401
    if request.method == 'POST':
      # For Test
      # curl -X POST -H 'Content-type:application/json' --data '{"title":"test"}' http://127.0.0.1:5000/api/v1/todos
        user = User.query.filter_by(id=userid).first()
        data = request.get_json()
        todo = Todo()
        title = data.get('title')
        due = data.get('due')
        status = 0
        todo.user_id = userid
        todo.title = title
        todo.due = due
        todo.status = status
        db.session.add(todo)
        db.session.commit()

        send_slack("TODO IS CREATED\nUSER: %s \nTITLE: %s\nDUE: %s" %
                   (user.userid, todo.title, todo.due))

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
        todo_user_id = args[0]
        todo_name = args[1]
        todo_due = args[2]
        todo = Todo()

        user = User.query.filter_by(userid=todo_user_id).first()

        todo.title = todo_name
        todo.due = todo_due
        todo.status = 0
        todo.user_id = user.id
        db.session.add(todo)
        db.session.commit()
        ret_msg = 'TODO IS CREATED'
        send_slack("[%s] %s" % (str(datetime.datetime.now()), todo_name))

    elif cmd == "list":
        todo_user_id = args[0]
        user = User.query.filter_by(userid=todo_user_id).first()
        todos = Todo.query.filter_by(user_id=user.id)
        for idx, todo in enumerate(todos):
            ret_msg += '%d. %s (%s, %s) \n' % (todo.id,
                                               todo.title, str(todo.due), ('Not Completed', 'Completed')[todo.status])

    elif cmd == "done":
        todo_id = args[0]
        todo = Todo.query.filter_by(id=todo_id).first()
        todo.status = 1
        db.session.commit()
        ret_msg = 'TODO IS CHANGED TO "COMPLETED"'

    elif cmd == "undo":
        todo_id = args[0]
        todo = Todo.query.filter_by(id=todo_id).first()
        todo.status = 0
        db.session.commit()
        ret_msg = 'TODO IS CHANGED TO "NOT COMPLETED"'

    return ret_msg
