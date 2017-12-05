from Afisha import app
from Afisha.api import EventController
from flask import request, abort
import json

events = EventController()

@app.route('/event/new', methods=['POST'])
def newPostHandler():
    try:
        data = request.get_json(force=True)
    except:
        return 'not valid json', 400

    require = ['place', 'price', 'description', 'contacts', 'date', 'type', 'thumbnail', 'title']
    for check in require:
        if check not in data:
            return '{} parameter is missing'.format(check), 400
    response = events.saveEvent(data)
    if response['code'] == 200:
        return 'ok', 200
    return abort(response['code'])

@app.route('/event/all')
def allEventHandler():
    response = events.getAllEvents()
    return json.dumps(response)