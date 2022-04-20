import pyodbc
import psycopg2




class Engine(object):
    def __init__(self):
        self.connection = None
        self.execute = None
        self.select = None
        self.insert = None

def initialize(creds=None):
    engine = creds['engine']
    host = creds['host']
    database = creds['database']
    user = creds['user']
    password = creds['password']
    engine = Engine()

    if creds is not None:
        connection = __connect(engine, host, user, password)
        engine.connection = connection        
        message = f"Connection to [{host}] established."
    else:
        message = f"Connection is not established."
    
    return connection, message


def __connect(engine, host, user, password):
    if engine == 'postgres':
        print(engine, host, user, password)
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password)
        return connection
