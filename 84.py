from flask import Flask, request, redirect
from replit import db

app = Flask(__name__)

@app.route('/signup', methods = ['POST'])
def createUser():
  keys = db.keys()
  form = request.form
  if form["username"] not in keys:
    db[form["username"]] = {"name": form["name"], "password": form["password"]}
    #should add salting later
    return redirect("/login")
  else:
    return redirect("/signup")

@app.route('/login', methods = ['POST'])
def doLogin():
  keys = db.keys()
  form = request.form
  if form["username"] not in keys:
    return redirect("/login")
  else:
    if form["password"] == db[form["username"]]["password"]:
      return f"""Hello, {db[form["username"]]["name"]}"""
    else:
      return redirect("/login")

@app.route('/login')
def login():
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
  page = """
  <!DOCTYPE html>
  <html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>replit</title>
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