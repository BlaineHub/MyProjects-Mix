from flask import Blueprint, flash, render_template,request
from send_email import send_email
from translate import *
from models import *
from quotes import get_quote
from dictionary import *
from flask_login import login_user, login_required, logout_user, current_user
#MySql will use mysql.connector

views = Blueprint("views",__name__)

@views.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template('login.html', text='Logged Out')

@views.route('/')
def index():
    return render_template('login.html')

@views.route('/login', methods=['POST','GET'])
def login():
    if request.method=='POST':
        email=request.form['email_name']
        password=request.form['password_name']
        user = Data.query.filter_by(email_=email).first()
        if user:
            if user.password_ == password:
                login_user(user,remember=True)
                return render_template("home.html")
            else:
                return render_template('login.html', text='Password is incorrect')
        else:
            return render_template('login.html', text='User does not exist')
    return render_template("login.html", user=current_user)


@views.route('/signup', methods=['POST','GET'])
def signup():
    if request.method=='POST':
        email=request.form['email_name']
        password=request.form['password_name']
        password2=request.form['password_name2']
        user = Data.query.filter_by(email_=email).first()
        if user:
            return render_template('signup.html', 
                    text='Opps, email already exists')
        elif password != password2:
                return render_template('signup.html', 
                        text='Opps, Passwords dont match')
        else:
            new_user = Data(email_=email, password_=password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
        return render_template('login.html',text='Signed Up Successfully')
    return render_template('signup.html')


@views.route('/forgotpassword', methods=['POST','GET'])
def forgotpassword():
    if request.method=='POST':
        email=request.form['email_name']
        if db.session.query(Data).filter(Data.email_==email).count() == 0:
            return render_template('forgotpassword', 
                    text='Opps, email does not exists')
        else:
            user = Data.query.filter_by(email_=email).first()
            x = user.password_
            send_email(email,x)
            return render_template('login.html', text='Your Password is on its way')
    return render_template('forgotpassword.html')

@views.route("/home", methods=['POST','GET'])
@login_required
def home():
    if request.method=='POST':
        feel=request.form['feel']
        text = get_quote(feel)
        return render_template('home.html', text=text)
    return render_template('home.html')

@views.route("/dictionary", methods=['POST','GET'])
@login_required
def dictionary():
    if request.method=='POST':
        word=request.form['word']
        text = diction(word)
        return render_template('dictionary.html', text=text)
    return render_template('dictionary.html')

@views.route("/dictionary2", methods=['POST','GET'])
@login_required
def dictionary2():
    if request.method=='POST':
        word2=request.form['word2']
        text = diction2(word2)
        return render_template('dictionary.html', text2=text)
    return render_template('dictionary.html')

@views.route("/translate", methods=['POST','GET'])
@login_required
def translate():
    if request.method=='POST':
        dest=request.form['languages']
        input=request.form['input']
        output = trans(input,dest)
        return render_template('translate.html',input=input, output=output)
    return render_template('translate.html')