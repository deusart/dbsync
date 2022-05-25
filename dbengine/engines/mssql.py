import pyodbc

def connect(credentials):
    connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};'
    connection_string += f'SERVER={credentials.HOST};DATABASE={credentials.DATABASE};'
    connection_string += f'UID={credentials.USER};PWD={credentials.PASSWORD}'
    connection = pyodbc.connect(connection_string)
    return connection

def select(connection, query):
    '''Fetchall from query'''
    cursor=connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def execute(connection, query):
    '''Execute query'''
    cursor=connection.cursor()
    cursor.execute(query)

def insert(connection, query, data):
    '''Insert query'''
    cursor = connection.cursor()
    cursor.executemany(query, data)            
    return cursor.rowcount

def commit(connection):
    connection.commit()

def disconnect(connection):
    connection.close()