from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')

def index():
    produs="smanatana"
    return render_template("index.html", produs=produs)


@app.route("/produse")

def produse():    
    return render_template("produse.html")



@app.errorhandler(404)

def page_not_found(e):
    return render_template("404.html"),404

@app.errorhandler(500)

def page_not_found(e):
    return render_template("500.html"),500
