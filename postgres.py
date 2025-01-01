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

        cursor = conn.cursor()

        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print(f"PostgreSQL version: {version}")

        cursor.close()
        conn.close()
        print("Connection closed.")

    except psycopg2.Error as e:
        print(f"Error connecting to the PostgreSQL database: {e}")
        

connect_to_postgres(config)
