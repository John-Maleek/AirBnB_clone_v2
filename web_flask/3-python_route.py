#!/usr/bin/python3
"""
    script starts a Flask web application:
    listens on 0.0.0.0, port 5000
"""


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Prints a message when the root endpoint is called"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Prints a message when the root endpoint is called"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Prints a message when the root endpoint is called"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pyhton_text(text='is cool'):
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')
