from app import db


class Tweets(db.Model):
    __tablename__ = "Tweets"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)

    def __repr__(self):
        return "{}".format(self.name)

class Speeches(db.Model):
    __tablename__ = "speeches"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)

    def __repr__(self):
        return "<Speeches: {}>".format(self.name)

class Interviews(db.Model):
    __tablename__ = "interviews"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)

    def __repr__(self):
        return "<Interviews: {}>".format(self.name)
