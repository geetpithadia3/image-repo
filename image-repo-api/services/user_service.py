from models.user import User
from models import db

class UserService:
    def __init__(self, db=db):
        self.db = db

    # create user function that handles all the error checking
    def create_user(self, username, password, email):
        # check if username is empty
        if username == '':
            return None
        # check if password is empty
        if password == '':
            return None
        # check if email is empty
        if email == '':
            return None
        # check if username is too long
        if len(username) > 50:
            return None
        # check if password is too long
        if len(password) > 50:
            return None
        # check if email is too long
        if len(email) > 120:
            return None
        # check if username already exists
        if self.get_user_by_username(username) is not None:
            return None
        # check if email already exists
        if self.get_user_by_email(email) is not None:
            return None
        # create user
        user = User(username=username, password=password, email=email)
        db.session.add(user)
        db.session.commit()
        return user
    

    def get_user_by_username(self, username):
        return User.query.filter_by(username=username).first()

    def get_user_by_email(self, email):
        return User.query.filter_by(email=email).first()

    def get_user_by_id(self, id):
        return User.query.filter_by(id=id).first()

    def get_all_users(self):
        return User.query.all()

    def delete_user(self, user):
        db.session.delete(user)
        db.session.commit()
        return user

    # update user function that takes all parameters as optional and handles all relevant exceptions from Postgres and SQLlite
    def update_user(self, user, username=None, password=None, email=None):
        # check if username is too long
        if username is not None and len(username) > 50:
            return None
        # check if password is too long
        if password is not None and len(password) > 50:
            return None
        # check if email is too long
        if email is not None and len(email) > 120:
            return None
        # check if username already exists
        if self.get_user_by_username(username) is not None:
            return None
        # check if email already exists
        if self.get_user_by_email(email) is not None:
            return None
        # update user
        if username is not None and username != '':
            user.username = username
        if password is not None and password != '':
            user.password = password
        if email is not None and email != '':
            user.email = email
        db.session.commit()
        return user
        