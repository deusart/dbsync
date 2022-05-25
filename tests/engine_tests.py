import dbengine

def run_dbengine_test(connection):

    message = "Creating engine {dbengine.dbEngine()}"
    try:
        engine = dbengine.dbEngine(connection)
        print(engine)
        print(f"[Success] {message}.")
    except Exception as error:
        print(f"[Failed] {message}. Error: {error}")

    message = "Execute {engine.execute()}"
    try:
        engine.execute('DROP TABLE IF EXISTS dbsync_test_table;')
        engine.execute('CREATE TABLE dbsync_test_table (id int);')        
        print(f"[Success] {message}.")
    except Exception as error:
        print(f"[Failed] {message}. Error: {error}")

    message = "Insert {engine.insert()}"
    try:
        insert_data = [(1, ), (2, )]
        if engine.credentials.ENGINE == 'mssql':
            engine.insert('INSERT INTO dbsync_test_table (id) VALUES (?);', insert_data)
        else:
            engine.insert('INSERT INTO dbsync_test_table (id) VALUES (%s);', insert_data)       
        print(f"[Success] {message}.")
    except Exception as error:
        print(f"[Failed] {message}. Error: {error}")

    message = "Select {engine.insert()}"
    try:
        select_data = engine.select('SELECT id FROM dbsync_test_table;')
        if select_data[0][0] == insert_data[0][0] and select_data[1][0] == insert_data[1][0]:
            print(f"[Success] {message}.")
        else:
            print(f"[Failed] {message}. Select data is not accurate.")
        engine.execute('DROP TABLE IF EXISTS dbsync_test_table;')
    except:
        print(f"[Failed] {message}.")