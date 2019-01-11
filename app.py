from flask import Flask, render_template,flash,redirect,url_for,session,request,logging
from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form,StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'

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
      validators.EqualTo('confirm', message='passwords do not match')])
      confirm = PasswordField('Confirm Password')

@app.route('/register',methods=['GET', 'POST'])
def register():
      form = RegisterForm(request.form)
      if request.method == 'POST' and form.validate():
       return render_template('register.html')
      
      return render_template('register.html', form=form)
if __name__ == "__main__":
    app.run(debug=True)