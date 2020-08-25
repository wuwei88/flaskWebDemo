# coding: utf-8
from application import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(30))
    login_name = db.Column(db.String(20), unique=True)
    login_pwd = db.Column(db.String(32))
    login_salt = db.Column(db.String(32))
    status = db.Column(db.Integer, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime)
    created_time = db.Column(db.DateTime)
