from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def main():
  return render_template('base.html')

@app.route("/user/Human")

def page():
  return render_template('page.html')

app.run(host='0.0.0.0', port=81)
