from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index ():
    name = request.args.get('name', '')
    #return "Hello " + name
    return render_template('home.html', name=name)

@app.route('/robot')
@app.route('/robot/go/<distance>')
def view(distance=None):
	return render_template('robot.html', distance=distance)
   



if __name__ == '__main__':
    app.run(debug=True)
