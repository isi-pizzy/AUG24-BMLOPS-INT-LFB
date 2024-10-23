from airflow.models import Connection
from airflow import settings

def check_and_update_mongo_connection():
    session = settings.Session()
    mongo_conn = session.query(Connection).filter(Connection.conn_id == 'mongo_default').first()

    if mongo_conn:
        print(f"Current connection type: {mongo_conn.conn_type}")
        if mongo_conn.conn_type != 'mongo':
            print("Updating connection type to 'mongo'")
            mongo_conn.conn_type = 'mongo'
            session.add(mongo_conn)
            session.commit()
            print("Connection type updated successfully.")
        else:
            print("Connection type is already set correctly to 'mongo'.")
    else:
        print("Mongo connection does not exist.")
    
    session.close()

check_and_update_mongo_connection()
