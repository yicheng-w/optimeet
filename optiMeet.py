from flask import *
import util
from database import DBManager

app = Flask(__name__)
database = DBManager()

@app.route('/')
def index():
    return render_template('halloween.html')

@app.route('/create-event')
def create_event():
    return render_template('createEvent.html')

@app.route('/join-event/<int:id>')
def join_event(id):
    return render_template('joinEvent.html', id=id)

@app.route('/view-event/<int:id>/<auth>/<name>')
def view_event(id, auth, name):
    if database.authenticate(id, auth_code):    
        locations = database.get_all_loc_in_event(id)
        meetup_places = get_list_of_locations(locations)
        my_loc = database.get_my_location(id, name)
        locations.remove(my_loc)
        locations = my_loc + locations

        return render_template('viewEvent.html', id=id, auth=auth, name=name, locs = locations, places = meetup_places)
    else:
        return render_template("unauthorized.html")

if (__name__ == '__main__'):
    app.run(debug=True)

