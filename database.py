# Database
# Made by Christophe
# Version 1
# Date 23.11.2023
import time
import mysql.connector
import traceback
import datetime
from datetime import datetime
# opening the connection with the db
def open_dbconnection():
    global db_connection
    # Establish a connection to the MySQL database
    db_connection = mysql.connector.connect(host='127.0.0.1', port='3306',
                                   user='christophe', password='Pa$$w0rd', database='projetdbpy',
                                   buffered=True, autocommit=True)
    return db_connection


# closing the connection with the db
def close_dbconnection():
    # Close the existing database connection
    db_connection.close()


# Function for adding player names to the "players" table
def get_playername(alias, exercise = None):
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

    if exercise != None:
        # Call a function to add the exercise title to the "exercises" table
        add_games(exercise)


# Add the games on the db
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


# getting the id of the player with his name
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


# getting the id of the exercise with his name
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


# adding the results when the player play the games
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
    query = ('''SELECT alias, start_date, time, name, number_done, max_number, results.id FROM results
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


def count_total(player_name, exercise_name):
    cursor = db_connection.cursor()
    if exercise_name != '':
        exercise_id = get_exercise_id(exercise_name)
    if player_name != '':
        player_id = get_player_id(player_name)

    # Query for getting the infos for the total with time formatted as HH:MM:SS
    query = "SELECT COUNT(id), SUM(time), SUM(number_done), SUM(max_number) FROM results"
    # Options for filter
    if player_name != '' and exercise_name != '':
        query += " WHERE player_id = %s AND exercise_id = %s"
        cursor.execute(query, (get_player_id(player_name), exercise_id))
    elif player_name != '':
        query += " WHERE player_id = %s"
        cursor.execute(query, (player_id,))
    elif exercise_name != '':
        query += " WHERE exercise_id = %s"
        cursor.execute(query, (exercise_id,))
    else:
        cursor.execute(query)  # No need for additional parameters in this case
    rows_tot = cursor.fetchall()
    time_in_seconds = time.gmtime(int(rows_tot[0][1]))
    result_tot = [(rows_tot[0][0], time.strftime('%H:%M:%S', time_in_seconds), rows_tot[0][2], rows_tot[0][3])]
    cursor.close()
    return result_tot


def delete_result(id):
    query = "DELETE FROM results WHERE id=%s"
    cursor = db_connection.cursor()
    cursor.execute(query, (id,))


def modify_result(dataset, id):
    if get_player_id(dataset[0]) == None:
        get_playername(dataset[0])
    user_id = get_player_id(dataset[0])
    exercise_id = get_exercise_id(dataset[3])
    date_data = dataset[1].split(" ")
    date_date_data = date_data[0].split("-")
    date_time_data = date_data[1].split(":")
    final_date = datetime.datetime(int(date_date_data[0]), int(date_date_data[1]), int(date_date_data[2]),
                                   int(date_time_data[0]), int(date_time_data[1]), int(date_time_data[2]))
    final_time = dataset[2]
    number_tries = int(dataset[4])
    number_total_tries = int(dataset[5])
    query = "UPDATE results SET player_id = %s, start_date = %s, time = %s, number_done = %s, max_number = %s, exercise_id = %s WHERE id=%s"
    cursor = db_connection.cursor()
    cursor.execute(query, (user_id, final_date, final_time, number_tries, number_total_tries, exercise_id, id))

def creation_result(player, exercise, start_date, time, nbok, nbtot):
    open_dbconnection()
    cursor = db_connection.cursor()

    # Check if the game exists
    query3 = "SELECT id FROM exercises WHERE name = %s"
    cursor.execute(query3, (exercise,))
    data1 = cursor.fetchone()

    # Check if the player exists
    query4 = "SELECT id FROM players WHERE alias = %s"
    cursor.execute(query4, (player,))
    data2 = cursor.fetchone()

    # If the game doesn't exist, show an error message
    if data1 is None:
        print("problème1")
        print(data1)
    else:
        # If the player doesn't exist, insert it
        if data2 is None:
            query2 = "INSERT INTO players (alias) values (%s)"
            cursor.execute(query2, (player,))
            query4 = "SELECT id FROM players WHERE alias = %s"
            cursor.execute(query4, (player,))
            data2 = cursor.fetchone()

        format_date = "%Y-%m-%d %H:%M:%S"
        format_time = "%H:%M:%S"
        start_date_test = False
        time_test = False
        nbok_test = False
        nbtot_test = False

        try:
            # Check if the date is in the correct format
            date_checked = datetime.strptime(start_date, format_date)
            start_date_test = True
        except ValueError as e:
            print(f"problème2: {e}")
            traceback.print_exc()

        try:
            # Check if the time is in the correct format
            time_checked = datetime.strptime(time, format_time)
            time_test = True
        except ValueError as e:
            print(f"problème3: {e}")
            traceback.print_exc()

        try:
            # Check if nbok is an integer
            nbok_checked = int(nbok)
            nbok_test = True
        except ValueError as e:
            print(f"problème14: {e}")
            traceback.print_exc()

        try:
            # Check if nbtot is an integer
            nbtot_checked = int(nbtot)
            nbtot_test = True
        except ValueError as e:
            print(f"problème5: {e}")
            traceback.print_exc()

        # If all checks pass, insert the result
        if start_date_test and time_test and nbok_test and nbtot_test:
            query1 = "INSERT INTO results (start_date, time, number_done, max_number, exercise_id, player_id) values (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query1, (date_checked, time_checked, nbok_checked, nbtot_checked, data1[0], data2[0]))