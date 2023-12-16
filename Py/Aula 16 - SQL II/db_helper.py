from db_connector import DatabaseConnection, config

class DBHelper():
    def __init__(self):
        sefl.connection = None
    
    def execute(self,sql):
        with DatabaseConnection(config) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)

https://dontpad.com/dfs713