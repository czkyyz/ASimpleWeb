import json
import os
from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy


result = {}

d = os.path.join(os.path.abspath(os.path.dirname(__name__)), '..', 'files') 

for i in os.listdir(d):
    file_path = os.path.join(d, i)
    with open(file_path) as f:
        result[i[:-5]] = json.load(f)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/xiaoshuo'
db = SQLAlchemy(app)

class File(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer,db.ForeignKey(...))
    #category_id = db.Column(db.ForeignKey(category_id))
    content = db.Column(db.Text)

class Category(db.Model):
    id = db.Column(db.Integer)
    name = db.Column(db.String(80))


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

if __name__ == '__main__':
    app.run()

