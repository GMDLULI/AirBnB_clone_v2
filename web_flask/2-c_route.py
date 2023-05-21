#!/usr/bin/python3
''' Creating a script that starts Flask web application.
    With addtional route /hbnb and /c/<text> which should
    display the string "C" followed by the value of the
    <text> variable
'''

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''display "hello HBNB" '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Displays str HBNB'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text():
    '''Displays the str "C" followed buy value of variable <text>
    '''
    text = text.replace("_", " ")
    return 'C %s' % escape(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
