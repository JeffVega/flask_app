from flask import Flask, render_template
from data import Articles
app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)