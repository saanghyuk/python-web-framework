import os
from flask import Flask
# from models import User
from flask import redirect
from flask import render_template
from models import db
from api_v1.__init__ import api as api_v1
from flask_jwt import JWT
from models import User

app = Flask(__name__)
app.register_blueprint(api_v1, url_prefix='/api/v1')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__))
    dbfile = os.path.join(basedir, 'db.sqlite')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'secret-key'

    db.init_app(app)
    db.app = app
    db.create_all()

    def authenticate(username, password):
        user = User.query.filter(User.userid == username).first()
        if user.password == password:
            return user

    def identity(payload):
        userid = payload['identity']
        return User.query.filter(User.id == userid).first()

    jwt = JWT(app, authenticate, identity)

    app.run(host='127.0.0.1', port=5000, debug=True)
