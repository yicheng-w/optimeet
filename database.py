import sqlite3

class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect("./db/database.db")
        self.c = conn.cursor()

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
        
        return (1, "1234")

    def authenticate(self, event_id, auth_code):
        """
        authenticate: authenticates id and auth_code, see if it matches
    
        Args:
            event_id (int): id of event
	    auth_code (string): 4 digit auth code
        
        Returns:
            True if match, False otherwise
        """
        return True

    def get_all_loc_in_event(self, event_id):
        """
        get_all_loc_in_event: return a list of location of all the people in ID
    
        Args:
            event_id (int): id of event
        
        Returns:
            the list of tuples of all the people in the event
            [(long1, lat1), (long2, lat2) ...]
        """
        return [(35.903636, -79.043628), (35.915680, -79.048175), (35.907672, -79.054301), (35.896418, -79.057854)]

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
        return [(35.903636, -79.043628), (35.915680, -79.048175), (35.907672, -79.054301), (35.896418, -79.057854)]

