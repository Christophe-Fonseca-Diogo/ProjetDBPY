# Database
# Made by Christophe
# Version 1
# Date 16.01.2024

import time
import bcrypt
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


# function for the total count
def count_total(player_name, exercise_name):
    cursor = db_connection.cursor()
    if exercise_name != '':
        exercise_id = get_exercise_id(exercise_name)
    if player_name != '':
        player_id = get_player_id(player_name)

    # Query for getting the infos for the total with time formatted as HH:MM:SS
    query = "SELECT COUNT(id), SUM(TIME_TO_SEC(time)), SUM(number_done), SUM(max_number) FROM results"

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

    # Convert the total time to 'HH:MM:SS' format
    total_seconds = rows_tot[0][1]
    total_time_formatted = f"{total_seconds // 3600:02}:{(total_seconds % 3600) // 60:02}:{total_seconds % 60:02}"

    result_tot = [(rows_tot[0][0], total_time_formatted, rows_tot[0][2], rows_tot[0][3])]
    cursor.close()
    return result_tot


# function for deleting the row in the results
def delete_result(id):
    query = "DELETE FROM results WHERE id=%s"
    cursor = db_connection.cursor()
    cursor.execute(query, (id,))


# function for modify the row in the results
def modify_result(dataset, id):
    if get_player_id(dataset[0]) == None:
        get_playername(dataset[0])
    user_id = get_player_id(dataset[0])
    exercise_id = get_exercise_id(dataset[3])
    date_data = dataset[1].split(" ")
    date_date_data = date_data[0].split("-")
    date_time_data = date_data[1].split(":")
    final_date = datetime(int(date_date_data[0]), int(date_date_data[1]), int(date_date_data[2]),
                                   int(date_time_data[0]), int(date_time_data[1]), int(date_time_data[2]))
    final_time = dataset[2]
    number_tries = int(dataset[4])
    number_total_tries = int(dataset[5])
    query = "UPDATE results SET player_id = %s, start_date = %s, time = %s, number_done = %s, max_number = %s, exercise_id = %s WHERE id=%s"
    cursor = db_connection.cursor()
    cursor.execute(query, (user_id, final_date, final_time, number_tries, number_total_tries, exercise_id, id))


# for the creation of the result manually
def creation_result(player, exercise, start_date, time, nbok, nbtot):
    cursor = db_connection.cursor()
    # Check if the game is in the db
    query_game_exist = "SELECT id FROM exercises WHERE name = %s"
    cursor.execute(query_game_exist, (exercise,))
    selected_exercise_id = cursor.fetchone()
    # Check if the player exist in the db
    query_player_exist = "SELECT id FROM players WHERE alias = %s"
    cursor.execute(query_player_exist, (player,))
    selected_player_id = cursor.fetchone()

    # If the game doesn't exist, return
    if selected_exercise_id is None:
        selected_exercise_id = False
    else:
        # If the player doesn't exist, insert it
        if selected_player_id is None:
            query_insert_player = "INSERT INTO players (alias) values (%s)"
            cursor.execute(query_insert_player, (player,))
            query_select_with_name = "SELECT id FROM players WHERE alias = %s"
            cursor.execute(query_select_with_name, (player,))
            selected_player_id = cursor.fetchone()

        # some variables
        format_date = "%Y-%m-%d %H:%M:%S"
        format_time = "%H:%M:%S"
        start_date_boolean = False
        time_boolean = False
        nbok_boolean = False
        nbtot_boolean = False

        try:
            # Check if the date is in the good format
            date_tested = datetime.strptime(start_date, format_date)
            start_date_boolean = True
        except ValueError as e:
            print(f"Error date : {e}")
            traceback.print_exc()

        try:
            # Check if the time is in the good format
            time_tested = datetime.strptime(time, format_time)
            time_boolean = True
        except ValueError as e:
            print(f"Error time : {e}")
            traceback.print_exc()

        try:
            # Check if nbok is not a float or something else
            nbok_tested = int(nbok)
            nbok_boolean = True
        except ValueError as e:
            print(f"Error nbok : {e}")
            traceback.print_exc()

        try:
            # Check if nbtot is not a float or something else
            nbtot_tested = int(nbtot)
            nbtot_boolean = True
        except ValueError as e:
            print(f"Error nbtot: {e}")
            traceback.print_exc()

        # If all checks are ok insert in the db
        if start_date_boolean and time_boolean and nbok_boolean and nbtot_boolean:
            query_insertion_database = "INSERT INTO results (start_date, time, number_done, max_number, exercise_id, player_id) values (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query_insertion_database, (date_tested, time_tested, nbok_tested, nbtot_tested, selected_exercise_id[0], selected_player_id[0]))
        else:
            print("Error")


# Function for the creation of the player in the db for the register
def create_user(player, password):
    cursor = db_connection.cursor()
    # Check if the player exist in the db
    query_player_exist = "SELECT id FROM players WHERE alias = %s"
    cursor.execute(query_player_exist, (player,))
    selected_player_id = cursor.fetchone()
    if selected_player_id is not None:
        return "Player already exists"
    query_adduser = "INSERT INTO players (alias, password, level) values (%s, %s, %s)"
    cursor.execute(query_adduser, (player, password, 1))
    return "User created successfully"


# Check if the password when the player try to log is correct
def check_login(user, password):
    cursor = db_connection.cursor()
    # Get the password from database.
    query = "SELECT password from players WHERE alias = %s"
    cursor.execute(query, (user, ))
    result = cursor.fetchone()
    if result == None:
        return False
    if bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
        return True
    else:
        return False


# Check if the player is in the database
def player_exists(alias):
    cursor = db_connection.cursor()
    try:
        # Check if the player exist
        cursor.execute("SELECT COUNT(*) FROM players WHERE alias = %s", (alias,))
        count = cursor.fetchone()[0]
        return count > 0
    except Exception as e:
        print(f"Error checking if player exists: {str(e)}")
        return False


# Add an Admin for the administration
def addAdmin():
    from Register import hash_password
    alias = "Admin"
    password = b'$2b$12$EhBV77O69R3HK5l04kPCheQJnkSg7j6lNCCpzCy7DZM.wSqGCxzGS'
    level = 3
    cursor = db_connection.cursor()
    query_addadmin = "INSERT INTO players (alias, password, level) values (%s, %s, %s)"
    try:
        cursor.execute(query_addadmin, (alias,password,level))
    except:
        print("Admin Done")


# Function for checkin the level of an account for the rights
def check_account_level(username):
    cursor = db_connection.cursor()
    query_check_level = "SELECT level FROM players WHERE alias = %s"
    try:
        cursor.execute(query_check_level, (username,))
        result = cursor.fetchone()
        if result:
            # Store user role in a global variable or session variable
            user_role = result[0]
            return user_role
        else:
            print("User not found")
            return None
    except Exception as e:
        print(f"Error checking account level: {str(e)}")
        return None


# Function for updating the level in the administration
def update_player_level(level_player, player):
    cursor = db_connection.cursor()
    select_query = "SELECT COUNT(*) FROM players WHERE alias = %s"
    cursor.execute(select_query, (player,))
    player_count = cursor.fetchone()[0]

    if player_count > 0:
        update_query = "UPDATE players SET level = %s WHERE alias = %s"
        cursor.execute(update_query, (level_player, player))
        return True
    else:
        return False
    cursor.close()


