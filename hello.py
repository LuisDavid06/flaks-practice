from flask import Flask, render_template, url_for, request
from markupsafe import escape
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Length

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY = 'DEV'
)
# filtros
@app.add_template_filter
def today(date):
    return date.strftime('%d-%m-%Y')


@app.route('/')
def index():
    print(url_for('index'))
    print(url_for('hello', name="luis"))
    print(url_for('code', code ='print("hola")'))
    name = "Luis David"
    frineds = ['Jose', 'Juan', 'Lisandro', 'Ana','Otras mas' ]
    date = datetime.now()

    return  render_template('index.html', name = name, friends= frineds, date=date)

@app.route('/hello')
@app.route('/hello/<string:name>')
@app.route('/hello/<string:name>/<int:age>')
@app.route('/hello/<string:name>/<int:age>/<email>')
def hello(name = None, age= None, email= None):
    my_data = {
        'name':name,
        'age':age,
        'email':email
    }

    return render_template('hello.html', data= my_data)
        
@app.route('/code/<path:code>')
def code(code):
    return f'hola, {escape(code)}'

# crear formulario wtfrom

class RegisterForm(FlaskForm):
    username = StringField("Nombre de usuario:", validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField("Password: ", validators=[DataRequired(), Length(min=6, max=25)])
    submit = SubmitField("Registrar")


# registrar usuarios
@app.route('/auth/register', methods=['GET', 'POST'])
def registrar_usuarios():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        return f"Nombre de usuario{username}, Contraseña: {password}"


    # if request.method == 'POST':
    #     username = request.form['username']
    #     password = request.form['password']

    #     if len(username)>= 4 and len(username) <= 25 and len(password) >= 6 and len(password) <= 40:
    #         return f"Nombre de usuario{username}, Contraseña: {password}"
    #     else:
    #         error = """Nombre de usuarii debe tener 4 y 25 caracteres, tambien la contraseña debe tener entre 6 y 25 caracteres"""
    #         return render_template('auth/register.html', form = form,  error = error)
    return render_template('auth/register.html', form = form)