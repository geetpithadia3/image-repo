from models import db

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_url = db.Column(db.String(50), nullable=False)
    thumbnail_url = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    @property
    def user(self):
        from models.user import User
        return User.query.get(self.user_id)