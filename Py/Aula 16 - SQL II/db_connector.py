import mysql.connector

class DatabaseConnection:
    def __init__(self, config:dict):
        self.config = config
        self.connection = None
    
    def __enter__(self):
        self.connection = mysql.connector.connect(**self.config)
        return self.connection
    
    def __exit__(self, exc_type, exc_value, traceback):
        if sel.connection:
            self.connection.close()


config = {
    
}