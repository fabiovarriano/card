from flask import Flask, request, render_template, session, redirect, url_for, jsonify
from flask_scss import Scss

app = Flask(__name__)
Scss(app, static_dir = "static", asset_dir = "assets/scss")


@app.route('/')
def index():

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug= True)


