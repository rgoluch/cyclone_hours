from datetime import datetime
from back_end import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    ta = db.Column(db.Boolean, default=False)


class TA(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_code = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))