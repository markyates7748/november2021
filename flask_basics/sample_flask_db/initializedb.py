## Script to initialize database
from todo_files.app import db
import os

db.create_all()