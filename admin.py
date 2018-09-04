class Admin:

    def __init__(self, ID, password):
        self._ID = ID
        self._password = password
        
    def get_ID(self):
        return self._ID
        
    def get_password(self):
        return self._password
        
    def set_ID(self, ID):
        self._ID = ID
        
    def set_password(self, password):
        self._password = password
