## Model for data representation of needed objects
from .app import db
from datetime import datetime
import secrets

DATE_FMT = '%Y-%m-%d %H:%M:%S'

## Task module
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, nullable=False)
    note = db.Column(db.Unicode)
    creation_date = db.Column(db.DateTime, nullable=False)
    due_date = db.Column(db.DateTime)
    completed = db.Column(db.Boolean, default=False)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    profile = db.relationship("Profile", back_populates='tasks')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'note': self.note,
            'creation_date': self.creation_date.strftime(DATE_FMT),
            'due_date': self.due_date.strftime(DATE_FMT) if self.due_date else None,
            'completed': self.completed,
            'profile_id': self.profile_id
            }

    def __repr__(self):
        return "<Task: {} | Owner: {}>".format(self.name, self.profile.username)

def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.creation_date = datetime.now()

## User module
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Unicode, nullable=False)
    email = db.Column(db.Unicode, nullable=False)
    password = db.Column(db.Unicode, nullable=False)
    date_joined = db.Column(db.Unicode, nullable=False)
    token = db.Column(db.Unicode, nullable=False)
    tasks = db.relationship("Task", back_populates='profile', lazy=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.date_joined = datetime.now()
        self.token = secrets.token_urlsafe(64)

    def to_dict(self):
        return{
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'date_joined': self.date_joined.strftime(DATE_FMT),
            'tasks': [task.to_dict() for task in self.tasks]
            }

    def __repr__(self):
        return "<Profile: {} | Tasks: {}>".format(self.username, len(self.tasks))