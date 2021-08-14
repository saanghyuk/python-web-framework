from functools import update_wrapper
from operator import delitem

from werkzeug.exceptions import UnsupportedMediaType
from .__init__ import api
from flask import json, jsonify
from models import User
from flask import request
from models import db


@api.route('/users', methods=["GET", "POST"])
def users():
    if request.method == "POST":
        userid = request.form.get('userid')
        username = request.form.get('username')
        password = request.form.get('password')
        re_password = request.form.get('re-password')
        print(userid)
        print(username)
        print(password)
        print(re_password)
        if not (userid and username and password and re_password):
            return jsonify({'error': 'No Arguments'}), 400

        if password != re_password:
            return jsonify({'error': 'Wrong Password'}), 400
        user = User()
        user.userid = userid
        user.username = username
        user.password = password

        db.session.add(user)
        db.session.commit()

        return jsonify(), 201

    # GET
    # 직렬화 함수 & 지능형리스트 사용
    users = User.query.all()
    return jsonify(
        [user.serialize for user in users]
    )


@api.route('/users/<uid>', methods=['GET', 'PUT', 'DELETE'])
def user_detail(uid):
    if request.method == 'GET':
        user = User.query.filter(User.id == uid).first()
        return jsonify(user.serialize)
    elif request.method == 'DELETE':
        User.query.delte(User.id == uid)
        return jsonify(), 204  # 204 : No content

    elif request.method == 'PUT':
        data = request.get_json()
        # userid = data.get('userid')
        # username = data.get('username')
        # password = data.get('password')
        # updated_data = {}
        # if userid:
        #     updated_data['userid'] = userid
        # if username:
        #     updated_data['username'] = username
        # if password:
        #     updated_data['password'] = password

        user = User.query.filter(User.id == uid).update(data)
        user = User.query.filter(User.id == uid).first()
        return jsonify(user.serialize), 200
        # 요청 requestt
        # curl -XPUT -H "Content-Type: application/json; charset=utf-8" -d '{"userid":"alghost"}' http://127.0.0.1:5000/api/v1/users/1
