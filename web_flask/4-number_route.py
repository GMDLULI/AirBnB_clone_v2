#!/usr/bin/python3
''' Creating a script that starts Flask web application.
    With addtional routes:
        /hbnb
        /c/<text> which should display the string "C" followed
        by the value of the variable <text>
        /python/(<text>) which displays "Python", followed by the value
        of the text of the text variable
        <text> variable
        /number/<n> display str "n is a number" Only if n is an integer
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
def c_text(text):
    '''Displays the str "C" followed by value of variable <text>
    '''
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    ''' Displays the str "Pythone" followed by value of variable <text>
    '''
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''Display "n is a number" only if variable n is an integer
    '''
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
