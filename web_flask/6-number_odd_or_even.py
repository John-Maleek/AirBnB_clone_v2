#!/usr/bin/python3
"""
    script starts a Flask web application:
    listens on 0.0.0.0, port 5000
"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Prints a message when the root endpoint is called"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Prints a message when the endpoint is called"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Prints a message when the endpoint is called"""
    return "C {}".format(text.replace("_", " "))

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pyhton_text(text='is cool'):
    """Prints a message when the endpoint is called"""
    return "Python {}".format(text.replace("_", " "))

@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """Prints a message when the endpoint is called"""
    return "{n} is a number".format(n=n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def is_number_template(n):
    """Returns an HTML page when the endpoint is called"""
    return render_template('5-number.html', number=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def is_even_or_odd(n):
    """Returns an HTML page when the endpoint is called"""
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')
