import psycopg2, json
from psycopg2 import sql
from flask import Flask, request, jsonify, render_template

config_path ='config.json'
with open(config_path, 'r') as file:
    config = json.load(file)
    db_config = config.get("database", {})

def connect_to_postgres(config):
    try:
        conn = psycopg2.connect(
                host=db_config.get("host"),
                port=db_config.get("port"),
                user=db_config.get("user"),
                password=db_config.get("password"),
                database=db_config.get("database")
            )
        print("Connected to the PostgreSQL database.")

        return conn
    except psycopg2.errors as e:
        print(f"ERROR connecting to the PostgreSQL db:{e}")
        
def connect_to_postgres1(config):
    try:
        conn = psycopg2.connect(
                host=db_config.get("host"),
                port=db_config.get("port"),
                user=db_config.get("user"),
                password=db_config.get("password"),
                database=db_config.get("database")
            )
        print("Connected to the PostgreSQL database.")

        cursor = conn.cursor()
        query = "select * from cpap_parts;"
        cursor.execute(query)
        # cursor.execute("SELECT version();")
        query_output = cursor.fetchone()
        print(f"{query_output}")

        cursor.close()
        conn.close()
        print("Connection closed.")

    except psycopg2.Error as e:
        print(f"Error connecting to the PostgreSQL database: {e}")
        

connect_to_postgres(config)
