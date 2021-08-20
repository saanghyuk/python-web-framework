from flask import Flask
from flask import render_template, redirect
import os
from models import db
from api_v1.__init__ import api as api_v1
from forms import RegisterForm, LoginForm
from models import User
from flask import session

app = Flask(__name__)
app.register_blueprint(api_v1, url_prefix='/api/v1')


@app.route('/', methods=['GET'])
def home():
    userid = session.get('userid', None)
    return render_template('home.html', userid=userid)


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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    # POST까지 체크
    if form.validate_on_submit():
        user = User()
        user.userid = form.data.get('userid')
        user.password = form.data.get('password')

        db.session.add(user)
        db.session.commit()
        print("SUCCESS")

        return redirect('/login')

    return render_template('register.html', form=form)


basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir, 'db.sqlite')


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret-key'

db.init_app(app)
db.app = app
db.create_all()

if __name__ == "__main__":

    app.run(host='127.0.0.1', port=5000, debug=True)
