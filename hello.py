from flask import Flask, render_template
from markupsafe import escape
from datetime import datetime


app = Flask(__name__)
# filtros
@app.add_template_filter
def today(date):
    return date.strftime('%d-%m-%Y')


@app.route('/')
def index():
    name = "Luis David"
    frineds = ['Jose', 'Juan', 'Lisandro', 'Ana','Otras mas' ]
    date = datetime.now()

    return  render_template('index.html', name = name, friends= frineds, date=date)

@app.route('/hello')
@app.route('/hello/<string:name>')
@app.route('/hello/<string:name>/<int:age>')
def hello(name = None, age= None):
    if name == None and age == None:
        return '<h1> Hello world</h1>'
    elif age == None:
        return f'<h1>Hello {name}</h1>'
    else:
        return f'<h1>hola {name}, tu edad {age}!!</h1>'
        
@app.route('/code/<path:code>')
def code(code):
    return f'hola, {escape(code)}'
