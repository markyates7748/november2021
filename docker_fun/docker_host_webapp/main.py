## Sample blog app to explore flask

from flask import Flask, render_template, url_for

app = Flask(__name__)

sample_posts = [
    {
     'author': 'John Smith',
     'title': 'Intro',
     'content': 'Introduction to the story',
     'post_date': '1 January 2000'
    },
    {
     'author': 'James Doe',
     'title': 'Middle',
     'content': 'The middle part of the story',
     'post_date': '15 July 2000'
    },
    {
     'author': 'Jannett Smith',
     'title': 'Conclusion',
     'content': 'Conclusion of the story',
     'post_date': '31 December 2000'
     }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=sample_posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')