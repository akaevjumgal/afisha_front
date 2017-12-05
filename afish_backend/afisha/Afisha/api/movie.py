from Afisha.database import Movie_db
from Afisha.configs import DB_PATH

moviedb = Movie_db(DB_PATH)

class MovieController:
    def saveMovie(self, data):
        saved = moviedb.saveMovie(data)

        return saved

    def getAll(self):
        data = moviedb.getAll()
        return data