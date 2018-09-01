# Danny Overton
# August 18th, 2018
# Bronwens Webpage

### My attempt at making a functioning website for Bronwen using flask. ###

# Guides used so far in the making, list may grow:
# https://pythonhow.com/how-a-flask-app-works/
# http://opentechschool.github.io/python-flask/core/html-css-js.html

from flask import Flask, render_template, request, redirect


app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')


if __name__ == '__main__':
  app.run(debug=True)
