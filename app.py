from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "exevazquez_6563"

@app.route("/hola")
def index():
    flash("Cual es tu nombre?")
    return render_template("index.html")

@app.route("/saludar", methods=["POST", "GET"])
def saludar():
    flash("Hola " + str(request.form['name_input'])+ ', que bueno verte!')
    request.form["name_input"]
    return render_template("index.html")