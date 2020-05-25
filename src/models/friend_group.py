from models import db


class FriendGroup(db.Model):
    friend_group_id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Client group %r>' % ''.join([self.name, self.surname])
