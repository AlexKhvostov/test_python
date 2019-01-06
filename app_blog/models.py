from app_blog.app import db
from datetime import datetime
import re

def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()


    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)


    def __repr__(self):
        return '<Post id: {}, title: {}>'.format(self.id, self.title)

class Workers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    deptname = db.Column(db.Integer)
    fullname = db.Column(db.String(30))
    birthday = db.Column(db.Date)
    salary = db.Column(db.Integer)

    def __init__(self, *args, **kwargs):
        super(Workers, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '(id: {}, fullname: {}, deptname: {}, birthday: {}, salary: {})'.format(self.id, self.fullname, self.deptname, self.birthday, self.salary)
        #return '<id: {}, name: {}>'.format(self.id, self.fullname)