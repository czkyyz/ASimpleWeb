#import os
#import json
from datetime import date,datetime
from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from yourapplication import db
#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/test'
#db = SQLAlchemy(app)

class File(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    category = db.relationship('Category', backref='file')
    content = db.Column(db.Text)
    def __init__(self,title,created_time,category,content):
        self.title = title
        self.created_time = created_time
        self.category = category
        self.content = content
    def __repr__():
        return '<File %r>'%self.title

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    def __init__(self,name):
        self.name = name
    def __repr__():
        return '<Category %r>'%self.name
'''
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

@app.route('/')
def index():
    l = [i['title'] for i in result.values()]
    return render_template('index.html', l=l)

@app.route('/files/<filename>')
def file(filename):
    filename1 = '/home/shiyanlou/files/'+filename+'.json'
    if os.path.exists(filename1):
        with open(filename1) as file:
            _title = json.loads(file.read())
            return (_title['content'])
    else:
        not_found(error)
'''
if __name__ == '__main__':
#    app.run()
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/test'
    db = SQLAlchemy(app)
    db.create_all()
    java = Category('Java')
    python = Category('Python')
    file1 = File("Hello Java",datetime.utcnow(),java,'File Content-Java is cool!')
    file2 = File('Hello Python',datetime.utcnow(),python,'File Content - Python is cool!')
    db.session.add(java)
    db.session.add(python)
    db.session.add(file1)
    db.session.add(file2)
    db.session.commit()
    engine = create_engine('mysql://root@localhost/test')
    engine.execute('select * from file').fetchall()
