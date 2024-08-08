from flask import Flask, request, redirect, session
from replit import db
import os

app = Flask(__name__)
app.secret_key = os.environ['sessionKey']

@app.route('/signup', methods = ['POST'])
def createUser():
  if session.get("loggedIn"):
    return redirect('/welcome')
  keys = db.keys()
  form = request.form
  if form["username"] not in keys:
    db[form["username"]] = {"name": form["name"], "password": form["password"]}
    return redirect("/login")
  else:
    return redirect("/signup")

@app.route('/login', methods = ['POST'])
def doLogin():
  if session.get("loggedIn"):
    return redirect('/welcome')
  keys = db.keys()
  form = request.form
  if form["username"] not in keys:
    return redirect("/login")
  else:
    if form["password"] == db[form["username"]]["password"]:
      session["loggedIn"] = form["username"]
      return redirect('/welcome')
    else:
      return redirect("/login")

@app.route('/welcome')
def welcome():
  page = f"""<h1>&emsp;&emsp; Welcome, {db[session["loggedIn"]]["name"]}</h1>

  

  
  <p>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
  <button type="button"onclick="location.href='/logout'">Log out</button></p>
  """
  return page

@app.route('/logout')
def logout():
  session.clear()
  return redirect("/")


@app.route('/login')
def login():
  if session.get("loggedIn"):
    return redirect('/welcome')
  page = ""
  f = open("login.html", "r")
  page = f.read()
  f.close()
  return page

@app.route('/signup')
def signup():
  page = ""
  f = open("signup.html", "r")
  page = f.read()
  f.close()
  return page


@app.route('/')
def index():
  if session.get("loggedIn"):
    return redirect('/welcome')
  page = """
  <!DOCTYPE html>
  <html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>day85</title>
    <style>
  h3, button{
    text-align: center;
  }
  .container { 
    height: 0px;
    position: relative;
    border: none;
    text-align: center;
  }

  .center {
    margin: 0;
    position: absolute;
    top: 50%;
    left: 50%;
    -ms-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
    text-align: center;
  }
  </style>
  </head>
  <body>
    <div class="container">
      <div class="vertical-center">
  <h3><a href = "/signup">Sign Up</a></h3>
<h3><a href = "/login">Login</a></h3>
</div></div>
</html>"""
  return page

app.run(host='0.0.0.0', port=81)