import json, pymysql
from flask import Flask, request, jsonify, render_template
from pymysql.cursors import DictCursor

app = Flask(__name__)
config_path ='config.json'
with open(config_path, 'r') as file:
    config = json.load(file)
    db_config = config.get("database", {})

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    
    data = request.json  
    selected_date = data.get('selected_date')
    item_name = data.get('item_name')

    insert_data_to_db(config, data)

    if not selected_date:
        return jsonify({"success": False, "message": "No date provided"}), 400

    json_file_path = "submitted_data.json"
    try:
        with open(json_file_path, 'r') as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        existing_data = []

    existing_data.append({"selected_date": selected_date, "item_name":item_name})

    with open(json_file_path, 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)

    return jsonify({"success": True, "message": f"Date {selected_date} saved successfully!"})

def insert_data_to_db(config, data):
      
    selected_date = data.get('selected_date')
    item_name = data.get('item_name')
    
    connection = connect_to_mysql(config)
        
    try:
        query = "INSERT INTO cpap_parts (item_name, timestamp) VALUES (%s, %s)"
        print(f"Inserting item_name: {item_name}, selected_date: {selected_date}")
        with connection.cursor() as cursor:
            cursor.execute(query, (item_name, selected_date))
            connection.commit()
            print(f"Data inserted successfully.")
    except pymysql.MySQLError as e:
        print(f"Error inserting data into MySQL: {e.args[0]}, {e.args[1]}")

    finally:
        if 'connection' in locals() and connection.open:
            connection.close()
            print("MySQL connection closed after insertion.")
    

def connect_to_mysql(config):
    try:
        connection = pymysql.connect(
            host=db_config.get("host"),
            port=db_config.get("port"),
            user=db_config.get("user"),
            password=db_config.get("password"),
            database=db_config.get("database")
        )
        print("Connected to the MySQL database successfully.")
        
        return connection
    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")

@app.route('/get_timestamp', methods=['GET'])
def get_timestamp():
    
    try:
        connection = connect_to_mysql(config)
        cursor = connection.cursor(DictCursor)
        
        query = "SELECT MAX(TIMESTAMP) as `timestamp` FROM cpap_parts WHERE ITEM_NAME = 'cpap_cushion';"
        cursor.execute(query)
        result = cursor.fetchone()
        
        if result:
            return jsonify(success=True, timestamp=result['timestamp'])
        else:
            return jsonify(success=False, message="No records found")
        
    except Exception as e:
        return jsonify(success=False, message=f"Error: {str(e)}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == '__main__':
    connect_to_mysql(config)
    app.run(debug=True)
