from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def getIndex():
  return "Hi!"

@app.route('/home')
def getHome():
  return render_template('home.html')

@app.route('/about')
def getAbout():
  return "<h3>Maksims Daņilovs</h3>"

@app.route('/about_html')
def about():
  return render_template('about.html')

@app.route('/contact')
def contact():
  return render_template('contact.html', phone = "3214532")

@app.route('/params')
def params():
  return request.args


app.run(host = '0.0.0.0', port = 8020)

