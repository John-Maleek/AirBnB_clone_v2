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


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')
