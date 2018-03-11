# =============================================================================
#                               User Class
# =============================================================================

from flask import request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String
from database import Base, db_session


# We define the structure of our table in the database.
# The structure for a database table is called a model in Flask.
# We create a new class (with the parent as db.Model) that is written as a singular (User) and then within the,
# class we name the table as a plural (users).
# The structure for a DB table is called a model in flask.


class User(Base):

    __tablename__ = 'users'
    #id = db.Column(db.Integer, primary_key=True)
    #username = db.Column(db.String(100), unique=True, nullable=False)
    #password = db.Column(db.String(60), nullable=False)
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(60), nullable=False)

    # =============================       Constructor      =====================================


    def __init__(self, username, password, userID=None):

        self.username = username
        self.password = password
        self.userID = userID
        self.team = []


    # =============================       Representation      =====================================


    def __repr__(self):
        return '<Username: %r>' % self.username


    # =============================       Password Hashing Functions      =====================================


    def set_password(self, password):
        self.password = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password, password)


    # =============================       Verify username and password in DB      =====================================


    def verify_user(self):
        verification = User.query.filter_by(username=self.username, password=self.password).scalar() is not None
        return verification


    # =======================      Check if username already taken (user exists)      ===============================


    def existing_user(self):
        is_existing = User.query.filter_by(username=self.username).scalar() is not None
        return is_existing


    # =============================       Post User to DB      =====================================


    def register_user(self, password_repeat):
        if self.password != password_repeat:
            return "Passwords don't match"
        if self.existing_user():
            return "Username already taken"

        db_session.add(self)
        db_session.commit()
        return "User " + self.username + " successfully registered!"
