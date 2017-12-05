from Afisha.database import Event_db
from Afisha.configs import DB_PATH

eventDB = Event_db(DB_PATH)

class EventController:
    def saveEvent(self, data):
        response = eventDB.newEvent(data)
        return response

    def getAllEvents(self):
        response = eventDB.allEvents()
        return response