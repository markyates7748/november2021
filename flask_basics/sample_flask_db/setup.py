## Python setup file for a simple todo list project from 
### opensource.org/article/18/4/flask
from setuptools import setup, find_packages

requires = [
    'flask',
    'flask-sqlalchemy',
    'psycopg2'
    ]

setup(
    name='flask_todo',
    version='0.0',
    description='Simple To-Do list with Flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
    )