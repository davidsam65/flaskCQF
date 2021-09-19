from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('lesson1.html')


@app.route('/lesson/<name>')
def lesson(name):
    return "<h1>Upper Case: {}</h1>".format(name.upper())


@app.route('/latin/<name>')
def latinName(name):
    returnName = ''
    if name[-1] == 'y':
        returnName = name[:-1] + 'iful'
    else:
        returnName = name + 'y'

    return "<h1>Your Latin Name is : {}</h1>".format(returnName)


if __name__ == '__main__':
    app.run()
