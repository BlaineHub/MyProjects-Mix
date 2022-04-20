from flask_login import UserMixin
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import psycopg2
from sqlalchemy import create_engine

def create_table():
    conn = psycopg2.connect("dbname='my_app' user='postgres' password='123456' host='localhost' port='5432' ")
    cur=conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS data2 (id INT NOT NULL IDENTITY PRIMARY KEY, email_ VARCHAR(120) UNIQUE, password_ VARCHAR(20))')
    conn.commit()
    conn.close()

db = SQLAlchemy()

class Data(db.Model, UserMixin):
    __tablename__='data2'
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120),unique=True)
    password_=db.Column(db.String(20))

    def __init__(self,email_,password_):
        self.email_=email_
        self.password_= password_

def create_app():  
    app=Flask(__name__)
    app.config['SECRET_KEY'] = 'hjhjhjhjhhjh'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://Blaine91:Bod273191!@Blaine91.mysql.pythonanywhere-services.com/Blaine91$my_app'
    #engine=create_engine('mysql+mysqlconnector://Blaine91:Bod273191!@Blaine91.mysql.pythonanywhere-services.com/Blaine91$my_app')
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:123456@localhost/my_app'
    db.init_app(app)

    from views import views
    app.register_blueprint(views, url_prefix="/")

    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Data.query.get(int(id))
    
    return app

  