from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index ():
    #return "Hello " + name
    return render_template('home.html')

@app.route('/robot/go/<distance>')
def go(distance=None):
	return render_template('robotgo.html', distance=distance)
   

@app.route('/robot/square/<distance>')
def square(distance=None):
    return render_template('robotsquare.html', distance=distance)


@app.route('/robot/buns/<distance>')
def xbuns(distance=None):
    return render_template('robotxbuns.html', distance=distance)


@app.route('/robot/hexagon/<distance>')
def hexagon(distance=None):
    return render_template('robothexagon.html', distance=distance)


if __name__ == '__main__':
    app.run(debug=True)
