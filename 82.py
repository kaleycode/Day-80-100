from flask import Flask, request

app = Flask(__name__)

@app.route('/language', methods=["GET"])
def lang():
  get = request.args
  if get == {}:
    return "No data"
  if get["lang"].lower() == "eng":
    return "Hello, how are you?"
  elif get["lang"].lower() == "esp":
    return "¿Hola, cómo estás?"
  elif get["lang"].lower() == "ger":
    return "Hallo, wie geht es dir?"
  elif get["lang"].lower()=="fre":
    return "Bonjour, comment ça va?"
  else:
    return "No data"

@app.route('/')
def index():
  return "Hello from Flask"

app.run(host='0.0.0.0', port=81)