import mysql.connector

def connect():
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="streamlit")
    return conn