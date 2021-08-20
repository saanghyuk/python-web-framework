from typing import ValuesView
from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from models import User


class RegisterForm(FlaskForm):
    userid = StringField('userid', validators=[DataRequired()])
    password = PasswordField('password', validators=[
                             DataRequired(), EqualTo('re_password')])
    re_password = PasswordField('re_password', validators=[DataRequired()])


class LoginForm(FlaskForm):
    # 이거 지금 validator가서 참고해서 만든 것.
    class UserPassword(object):
        def __init__(self, message=None):
            self.message = message

        def __call__(self, form, field):
            userid = form['userid'].data
            password = field.data
            try:
                user = User.query.filter_by(userid=userid).first()
                if user.password != password:
                    self.message = "Wrong Password"
            except:
                raise ValueError("Wrong ID")
            if self.message == "Wrong Password":
                raise ValueError(self.message)

    userid = StringField('userid', validators=[DataRequired()])
    password = PasswordField('password', validators=[
                             DataRequired(), UserPassword()])
