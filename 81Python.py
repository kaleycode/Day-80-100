from flask import Flask, request

app = Flask(__name__)

@app.route("/81robot", methods=["POST"])
def robot():
  form = request.form
  if form['metal'] == "Yes":
    return "You're a robot!"
  elif "error" in form["infinity"].lower():
    return "You're a robot!"
  elif form["food"] == "None":
    return "You're a robot!"
  elif form["beep"] == "Yes":
    return "You're a robot!"
  else:
    return "Hi there fellow human"


@app.route('/')
def index():
  page = ""
  f = open("81robot.html", "r")
  page = f.read()
  f.close()
  return page

app.run(host='0.0.0.0', port=81)