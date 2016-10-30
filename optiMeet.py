from flask import *
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/event/<int:id><int:auth>')
def event(id, auth):
	return render_template('event.html', id=id, auth=auth)

@app.route('/create')
def create_event():
	return render_template('createEvent.html')

if (__name__ == '__main__'):
	app.run(debug=True)