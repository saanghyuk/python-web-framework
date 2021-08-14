import os
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from models import db
from models import User
from flask_wtf.csrf import CSRFProtect, CsrfProtect
from flask import session

from forms import RegisterForm, LoginForm
app = Flask(__name__)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    # POST까지 체크
    if form.validate_on_submit():
        user = User()
        user.userid = form.data.get('userid')
        user.password = form.data.get('password')
        user.username = form.data.get('username')
        db.session.add(user)
        db.session.commit()
        print("SUCCESS")

        return redirect('/')

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # POST까지 체크
    if form.validate_on_submit():
        userid = form.data.get('userid')
        password = form.data.get('password')
        session['userid'] = userid
        return redirect('/')

    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET'])
def logout():
    session.pop('userid', None)
    return redirect('/')


@app.route('/')
def hello():
    userid = session.get('userid', None)
    return render_template('hello.html', userid=userid)


basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir, 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# CSRF SETTING
app.config['SECRET_KEY'] = 'sadlkjf;klasjdfkl;ajsldk;f'
csrf = CSRFProtect()
csrf.init_app(app)

db.init_app(app)
db.app = app
db.create_all()

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
