# Database
# Made by Christophe
# Version 1
# Date 23.11.2023


import mysql.connector


def open_dbconnection():
    global db_connection
    # Establish a connection to the MySQL database
    db_connection = mysql.connector.connect(host='127.0.0.1', port='3306',
                                   user='christophe', password='Pa$$w0rd', database='projetdbpy',
                                   buffered=True, autocommit=True)
    return db_connection


def close_dbconnection():
    # Close the existing database connection
    db_connection.close()


# Function for adding player names to the "players" table
def get_playername(alias, exercise):
    cursor = db_connection.cursor()
    # Check if the player alias already exists in the "players" table
    query_select = "SELECT alias from players"
    cursor.execute(query_select, multi=True)
    rows = cursor.fetchall()
    for name in rows:
        if name[0] == alias:
            return
    # Insert the player alias into the "players" table
    query_insert = "INSERT INTO players (alias) values (%s)"
    cursor.execute(query_insert, (alias, ))
    cursor.close()

    # Call a function to add the exercise title to the "exercises" table
    add_games(exercise)


def add_games(title):
    cursor = db_connection.cursor()
    # Check if the exercise title already exists in the "exercises" table
    query_select = "SELECT name from exercises"
    cursor.execute(query_select, multi=True)
    results = cursor.fetchall()
    for result in results:
        if result[0] == title:

            return
    # Insert the exercise title into the "exercises" table
    query_insert = "INSERT INTO exercises (name) values (%s)"
    cursor.execute(query_insert, (title, ))
    cursor.close()


def get_player_id(player_name):
    cursor = db_connection.cursor()
    # Retrieve the player ID based on the alias from the "players" table
    query = "SELECT id FROM players WHERE alias = %s"
    cursor.execute(query, (player_name,))
    player_id = cursor.fetchone()
    # Close the cursor and database connection
    cursor.close()
    # Return the player_id if found, otherwise return None
    return player_id[0] if player_id else None


def get_exercise_id(exercise_name):
    cursor = db_connection.cursor()
    # Retrieve the exercise ID based on the name from the "exercises" table
    query = "SELECT id FROM exercises WHERE name = %s"
    cursor.execute(query, (exercise_name,))
    exercise_id = cursor.fetchone()
    # Close the cursor and database connection
    cursor.close()
    # Return the exercise_id if found, otherwise return None
    return exercise_id[0] if exercise_id else None


def add_results(start_date, duration_s, nbtrials, nbsuccess, exercise_name, player_name):
    # Fetch exercise_id or insert the exercise if it doesn't exist
    exercise_result = get_exercise_id(exercise_name)
    if exercise_result is None:
        # Exercise not found, insert it
        cursor = db_connection.cursor()
        insert_exercise_query = "INSERT INTO exercises (name) VALUES (%s)"
        cursor.execute(insert_exercise_query, (exercise_name,))
        # Now, fetch the exercise_id again
        exercise_result = get_exercise_id(exercise_name)
        if exercise_result is None:
            # If still not found, handle the error
            print("Error: Exercise not found even after insertion.")
            return
    exercise_id = exercise_result

    # Fetch player_id
    player_id = get_player_id(player_name)
    if player_id is None:
        return

    # Convert duration_s to 'HH:MM:SS' format
    duration_formatted = f"{duration_s // 3600:02}:{(duration_s % 3600) // 60:02}:{duration_s % 60:02}"

    # Insert into the "results" table
    cursor = db_connection.cursor()
    query = 'INSERT INTO results (start_date, time, number_done, max_number, exercise_id, player_id) VALUES (%s, %s, %s, %s, %s, %s)'
    cursor.execute(query, (start_date, duration_formatted,nbsuccess, nbtrials, exercise_id, player_id))
    cursor.close()


# Function for filter with the entrys with the name or the exercise
def filter_results(player_name, exercise_name):
    if exercise_name != '':
        exercise_id = get_exercise_id(exercise_name)
    cursor = db_connection.cursor()
    # Retrieve results by joining "results," "players," and "exercises" tables
    query = ('''SELECT alias, start_date, time, name, number_done, max_number FROM results
                INNER JOIN players ON results.player_id = players.id 
                INNER JOIN exercises ON results.exercise_id = exercises.id
                ''')
    # Options for filter
    if player_name != '' and exercise_name != '':
        query += "WHERE alias = %s AND exercise_id = %s"
        cursor.execute(query, (player_name, exercise_id))
    elif player_name != '':
        query += "WHERE alias = %s"
        cursor.execute(query, (player_name,))
    elif exercise_name != '':
        query += "WHERE exercise_id = %s"
        cursor.execute(query, (exercise_id,))
    else:
        cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows


def count_total():
    cursor = db_connection.cursor()
    # Retrieve the exercise ID based on the name from the "exercises" table
    query_numberlines = "SELECT COUNT(results.id) AS 'NbLignes' FROM results"
    cursor.execute(query_numberlines)
    query_numberlines = "SELECT COUNT(results.id) AS 'NbLignes' FROM results"
    cursor.execute(query_numberlines)
    query_numberlines = "SELECT COUNT(results.id) AS 'NbLignes' FROM results"
    cursor.execute(query_numberlines)
    query_numberlines = "SELECT COUNT(results.id) AS 'NbLignes' FROM results"
    cursor.execute(query_numberlines)
    rows = cursor.fetchall()
    # Close the cursor and database connection
    cursor.close()
