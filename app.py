from flask import Flask, render_template
import time
app = Flask(__name__)
global color
color = "#FF0000"

@app.route("/")
def home():
    return render_template('home.html', color=color)

app.run(debug=True)

while True:
    pass