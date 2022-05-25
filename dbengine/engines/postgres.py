import psycopg2

def connect(credentials):
    connection = psycopg2.connect(
            host=credentials.HOST,
            port=credentials.PORT,
            user=credentials.USER,
            password=credentials.PASSWORD)
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