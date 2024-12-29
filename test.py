import pymysql
import json

config_path ='config.json'

with open(config_path, 'r') as file:
    config = json.load(file)

    db_config = config.get("database", {})

def connect_to_mysql(config):

    try:
        # Establish the connection
        connection = pymysql.connect(
            host=db_config.get("host"),
            port=db_config.get("port"),
            user=db_config.get("user"),
            password=db_config.get("password"),
            database=db_config.get("database")
        )
        print("Connected to the MySQL database successfully.")
        
        with connection.cursor() as cursor:
            cursor.execute("SELECT DATABASE();")
            current_db = cursor.fetchone()
            print(f"Currently connected to database: {current_db[0]}")
            
            query = f"SELECT * FROM cpap_parts;"
            cursor.execute(query)
            results = cursor.fetchall()
            for row in results:
                print(row)
        
        return connection
    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
    finally:
        if 'connection' in locals() and connection.open:
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    connect_to_mysql(config)
