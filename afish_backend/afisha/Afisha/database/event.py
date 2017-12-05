from .db import db
import json

class Event_db(db):
    def newEvent(self, data):
        SQL = '''
            insert or ignore into events(
                place,
                price,
                description,
                contacts,
                date,
                type,
                thumbnail,
                title)
            values (?,?,?,?,?,?,?,?)
        '''

        params = (data['place'],
                  data['price'],
                  json.dumps(data['description']),
                  json.dumps(data['contacts']),
                  data['date'],
                  data['type'],
                  data['thumbnail'],
                  data['title'])
        self.create_conn()
        saved = self.do(SQL, params=params, commit=True)
        if saved['code'] != 200:
            self.close_conn()
            return saved
        self.close_conn()
        return dict(code=200)

    def allEvents(self):
        SQL = '''
            select
                id,
                place,
                price,
                description,
                contacts,
                date,
                type,
                thumbnail,
                title
            from events
        '''

        self.create_conn()
        sql_data = self.do(SQL, out=True)
        self.close_conn()

        if sql_data['code'] == 404:
            return dict(code=404, message='there is no event')
        sql_data = sql_data['data']
        events = []
        for event in sql_data:
            response = {
                "id": event[0],
                "place": event[1],
                "price": event[2],
                "description": json.loads(event[3]),
                "contacts": json.loads(event[4]),
                "date": event[5],
                "type": event[6],
                "thumbnail": event[7],
                "title": event[8]
            }
            events.append(response)
        return dict(code=200, data=events)

