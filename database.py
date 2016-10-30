import sqlite3
import random

class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect("./db/database.db")
        self.c = self.conn.cursor()

    def next_avaliable_id(self):
        """
        next_a: gives out the next avaliable id for the sites table
        
        Returns:
            an integer that represents the next possible id
        """
        q = """SELECT sites.id FROM sites ORDER BY sites.id"""

        result = self.c.execute(q).fetchall()

        ##print result

        if (len(result) == 0):
            return 0

        if result[0][0] != 0:
            #print "0 index: " + str(result[0][0])
            return 0

        if (len(result) == 1):
           return 1
       
        for i in range(1, len(result)):
            if result[i][0] - result[i - 1][0] > 1:
                return result[i - 1][0] + 1

        return len(result)

    def create_event(self, event_name):
        """
        create_event: creates the event in the event table, generates id/auth
        code pair
    
        Args:
            event_name (string): name of event
        
        Returns:
            a tuple of the form (event_id, auth_code)
            Note that auth_code is string of length 4
        """

        auth_code = "%04d" % random.randint(0,9999)
        id = self.next_avaliable_id()

        q = """INSERT INTO events VALUES (?, ?, ?)"""

        self.c.execute(q, (id, auth_code, event_name))
        self.conn.commit()
        
        return (id, auth_code)

    def authenticate(self, event_id, auth_code):
        """
        authenticate: authenticates id and auth_code, see if it matches
    
        Args:
            event_id (int): id of event
	    auth_code (string): 4 digit auth code
        
        Returns:
            True if match, False otherwise
        """

        q = """SELECT * FROM events
        WHERE events.id = ? AND events.auth_code = ?"""

        r = self.c.execute(q, (event_id, auth_code)).fetchall()

        return len(r)

    def get_all_loc_in_event(self, event_id):
        """
        get_all_loc_in_event: return a list of location of all the people in ID
    
        Args:
            event_id (int): id of event
        
        Returns:
            the list of tuples of all the people in the event
            [(long1, lat1), (long2, lat2) ...]
        """

        q = """SELECT people.long, people.lat
        FROM people
        WHERE people.id = ?"""

        return self.c.execute(q, (event_id)).fetchall()

    def add_person(self, event_id, name, long, lat):
        """
        add_person: adds a person to the people database
    
        Args:
            event_id (int): id of event
    	    name (string): name of the person
	    long (float): longitude of location
	    lat (float): latitude of location
        
        Returns:
            same as get_all_loc_in_event
        """

        q = """INSERT INTO people VALUES (?, ?, ?, ?)"""

        self.c.execute(q, (event_id, name, long, lat))
        self.conn.commit()

        return self.get_all_loc_in_event(event_id)

    def get_my_location(self, event_id, name):
        """
        get_my_location: get my location based on name
    
        Args:
            event_id (type): TODO
            name (type): TODO
        
        Returns:
            the tuple of (long, lat) or None
        """
        
        q = """SELECT people.long, people.lat FROM people
        WHERE people.id = ? AND people.name = ?"""

        return self.c.execute(q, (event_id, name)).fetchall()

