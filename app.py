from flask import Flask, jsonify, request

# Intitialise the app
app = Flask(__name__)

# Define what the app does
@app.get("/greet")
def index():
    fname = request.args.get("fname")
    sname = request.args.get("sname")
    if not fname and not sname:
        return jsonify({"status":"error"})
    elif fname and not sname:
        response = {'data': f'Hello, {fname} !'}
    elif sname and not fname:
        response = {'data': f'Hello, Mr.{sname} !'}
    else:
        response = {'data': f'Is your name, {fname} {sname}  ?'}
    return jsonify(response)