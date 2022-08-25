from pymongo import MongoClient
def get_db_handle(db_name, host, port, username, password):
    client = MongoClient(host=localhost,
                        port=int(8080),
                        username=admin,
                        password=pass1234
                        )
    db_handle = client['todo_db']
    
 return db_handle, client