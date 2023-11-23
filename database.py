import mysql.connector
from tkinter import messagebox

import geo01
from geo01 import *

def open_dbconnection():
    global db_connection
    db_connection = mysql.connector.connect(host='127.0.0.1', port='3306',
                                   user='christophe', password='Pa$$w0rd', database='projetdbpy',
                                   buffered=True, autocommit=True)
    return db_connection

def close_dbconnection():
    db_connection.close()


## Function for adding the names on the user table with the first parameter alias(the name) and the second the window for staying on the right windows after the messagebox
def playername(alias, exercise):
    open_dbconnection()
    cursor = db_connection.cursor()
    query_select = "SELECT alias from players"
    cursor.execute(query_select, multi=True)
    rows = cursor.fetchall()
    for name in rows:
        if name[0] == alias:
            close_dbconnection()
            return
    query_insert = "INSERT INTO players (alias) values (%s)"
    cursor.execute(query_insert, (alias, ))
    cursor.close()
    close_dbconnection()

    # Function that will add the title of the game in the database
    database.add_games(exercise)

def add_games(title):
    open_dbconnection()
    cursor = db_connection.cursor()

    query_select = "SELECT name from exercises"
    cursor.execute(query_select, multi=True)
    results = cursor.fetchall()

    for result in results:
        if result[0] == title:
            close_dbconnection()
            return

    query_insert = "INSERT INTO exercises (name) values (%s)"

    cursor.execute(query_insert, (title, ))
    cursor.close()

def get_player_id(player_name):
    open_dbconnection()
    cursor = db_connection.cursor()
    query = "SELECT id FROM players WHERE alias = %s"

    cursor.execute(query, (player_name,))
    player_id = cursor.fetchone()

    # Close the cursor and database connection
    cursor.close()
    close_dbconnection()

    # Return the player_id if found, otherwise return None
    return player_id[0] if player_id else None

def get_exercise_id(exercise_name):
    open_dbconnection()
    cursor = db_connection.cursor()
    query = "SELECT id FROM exercises WHERE name = %s"

    cursor.execute(query, (exercise_name,))
    exercise_id = cursor.fetchone()

    # Close the cursor and database connection
    cursor.close()
    close_dbconnection()

    # Return the player_id if found, otherwise return None
    return exercise_id[0] if exercise_id else None

