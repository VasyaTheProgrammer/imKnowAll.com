from flask import Flask
from flask import *
file2 = open('templates/two.html','r')
code2 = file2.read()

app = Flask(__name__)

@app.route('/')



def index():
    file1 = open('templates\home.html','r')
    code1 = file1.read()
    return code1

@app.route('/about')

def about():
    return code2

if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug = True)
