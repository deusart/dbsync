from dbengine.engines import mssql, postgres

class dbEngine(object):

    def __init__(self, credentials) -> None:
        self.credentials = credentials
        if credentials.ENGINE == 'postgres':  
            self.engine = postgres
        elif credentials.ENGINE == 'mssql': 
            self.engine = mssql
        else:
            self.engine = None

    def select(self, query):
        connection = self.engine.connect(self.credentials)
        data = self.engine.select(connection, query)
        self.engine.disconnect(connection)
        return data

    def execute(self, query):
        connection = self.engine.connect(self.credentials)
        self.engine.execute(connection, query)
        self.engine.commit(connection)
        self.engine.disconnect(connection)
        
    def insert(self, query, data):
        connection = self.engine.connect(self.credentials)
        self.engine.insert(connection, query, data)
        self.engine.commit(connection)
        self.engine.disconnect(connection)

    def __str__(self):
        info =  f'Engine:{self.credentials.ENGINE}\n'
        info +=  f'Host:{self.credentials.HOST}\n'
        info +=  f'Port:{self.credentials.PORT}\n'
        info +=  f'Database:{self.credentials.DATABASE}\n'
        info +=  f'User:{self.credentials.USER}'        
        return info