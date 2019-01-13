from flask import Flask, render_template,flash,redirect,url_for,session,request,logging
from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form,StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
import os
app = Flask(__name__)
host = os.getenv("HOST")
user = os.getenv("USER")
passWrd = os.getenv("PASS")
dataBse = os.getenv("DATAB")
print(host,"this is our host")
print(user,"this is our user")
print(passWrd,"this is our passWrd")

# Config MySQL
app.config['MYSQL_HOST'] = host
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = passWrd
app.config['MYSQL_DB'] = dataBse
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

Articles = Articles()
@app.route('/')
def index():
      return render_template('home.html')
@app.route('/about')
def about():
      return render_template('about.html')

@app.route('/article')
def article():
      return render_template('articles.html', articles = Articles)

@app.route('/articles/<string:id>/')
def articles(id):
    return render_template('articles.html', id=id)

class RegisterForm(Form):
      name = StringField('Name',[validators.Length(min=1,max=50)])
      username = StringField('Username',[validators.Length(min=4, max=25)])
      password = PasswordField('Password',[validators.DataRequired(),
      validators.EqualTo('confirm', message='passwords does not match')])
      confirm = PasswordField('Confirm Password')

@app.route('/register',methods=['GET', 'POST'])
def register():
      form = RegisterForm(request.form)
      if request.method == 'POST' and form.validate():
       return render_template('register.html')
      
      return render_template('register.html', form=form)
if __name__ == "__main__":
    app.run(debug=True)