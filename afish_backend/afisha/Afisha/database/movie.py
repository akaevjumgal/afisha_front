from .db import db
import json



class Movie_db(db):
    def saveMovie(self, data):
        sql_save_movie = '''
            insert or ignore into movies (title, thumbnail, trailer, description, sessions)
            values(?, ?, ?, ?, ?)
        '''

        movie_params = (data['title'],
                        data['thumbnail'],
                        data['trailer'],
                        json.dumps(data['description']),
                        json.dumps(data['sessions']))

        self.create_conn()
        movie_r = self.do(sql_save_movie, params=movie_params, commit=True)
        self.close_conn()
        return movie_r

    def getAll(self):
        sql = '''
            select id, title, thumbnail, trailer, description, sessions from movies
        '''
        self.create_conn()
        sqlData = self.do(sql, out=True)
        self.close_conn()
        if sqlData['code'] != 200:
            return sqlData
        response = []
        for movie in sqlData['data']:
            response.append(dict(
                id=movie[0],
                title=movie[1],
                thumbnail=movie[2],
                trailer=movie[3],
                description=json.loads(movie[4]),
                sessions=json.loads(movie[5])
            ))
        return dict(code=200, data=response)

