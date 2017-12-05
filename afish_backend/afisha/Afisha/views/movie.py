from Afisha import app
from flask import request, abort, make_response
import json

from Afisha.api import MovieController

movieController = MovieController()

@app.route('/movie/new', methods=['POST'])
def movie_new():
    try:
        data = request.get_json(force=True)
    except:
        return 'not valid json', 400

    require = ['title', 'thumbnail', 'description', 'trailer', 'sessions']
    for check in require:
        if check not in data:
            return '{} parameter is missing'.format(check), 400
    response = movieController.saveMovie(data)

    if response['code'] == 200:
        return 'ok', 200
    return abort(response['code'])

@app.route('/movie/all')
def allmovies():
    response = movieController.getAll()
    r = make_response(json.dumps(response))
    r.headers["Access-Control-Allow-Origin"] = 'http://192.168.0.160:5000/movie/all'
    return r
