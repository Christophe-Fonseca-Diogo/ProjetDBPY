# Results
# Made by Christophe
# Version 1
# Date 15.12.2023

import time
import tkinter as tk
import database, datetime
from tkinter import *
from tkinter import messagebox
from datetime import datetime


# variables
rgb_color = (139, 201, 194)
hex_color = '#%02x%02x%02x' % rgb_color  # translation in hexa


# function for when the player quit windows
def closing_insertion():
    result_message = messagebox.askokcancel(title="Information", message="Vous allez quitter la page.")
    if result_message:
        window_insert_results.destroy()
        new_modify_window.destroy()
        show_info_filtered(infos_frame, count_frame)
    else:
        # If the user clicks "Cancel," bring the insertion window to the foreground
        window_insert_results.lift()


# function for the button deleting
def delete_button_infos(res_frame, student_id, count_frame, row, column):
    delete_button = Button(res_frame, text="Supprimer", command=lambda: modify_or_delete(student_id, main_data=[res_frame, count_frame]))
    delete_button.grid(row=row, column=column)


# function for the button modify
def modify_button_infos(res_frame, main_window, student_id, count_frame, row, column):
    modify_button = Button(res_frame, text="Modifier", command=lambda: modify_window(main_window, id=student_id, main_data=[res_frame, count_frame]))
    modify_button.grid(row=row, column=column)


# modify window
def modify_window(parent_frame, main_data, id=None, table_type="modify"):
    global new_modify_window, option_modify_frame
    new_modify_window = tk.Tk()
    new_modify_window.title("Modification")
    new_modify_window.geometry("1920x1080")
    new_modify_window.configure(bg=hex_color)
    new_modify_window.grid_columnconfigure((0, 1, 2), minsize=300, weight=1)

    # Title for the adding modify window
    new_result_window_title = tk.Label(new_modify_window, text="Modification d'un résultat", font=("Arial", 25),borderwidth=2,relief="solid")
    new_result_window_title.grid(row=0, column=1, ipady=5, padx=40, pady=40)
                                       # Color definition
    new_modify_window.configure(bg=hex_color)
    new_modify_window.grid_columnconfigure((0, 1, 2), minsize=300, weight=1)

    # Frames for the window for the modification
    up_window_modify_results = Frame(new_modify_window, bg=hex_color, relief="solid")
    up_window_modify_results.grid(row=1, columnspan=3)
    option_modify_frame = Frame(up_window_modify_results, bg="white", padx=10, bd=2, relief="solid")
    option_modify_frame.grid(row=1, columnspan=3)

    # Options labels
    label_modify_player = Label(option_modify_frame, text="Élève : ", bg="white", padx=40, font=("Arial,15"))
    label_modify_player.grid(row=0, column=0)
    label_modify_date = Label(option_modify_frame, text="Date et Heure : ", bg="white", padx=40, font=("Arial,15"))
    label_modify_date.grid(row=0, column=2)
    label_modify_time = Label(option_modify_frame, text="Temps : ", bg="white", padx=40, font=("Arial,15"))
    label_modify_time.grid(row=0, column=4)
    label_modify_exercice = Label(option_modify_frame, text="Exercice : ", bg="white", padx=40, font=("Arial,15"))
    label_modify_exercice.grid(row=0, column=6)
    label_modify_number_ok = Label(option_modify_frame, text="Nombre OK : ", bg="white", padx=40, font=("Arial,15"))
    label_modify_number_ok.grid(row=1, column=2)
    label_modify_number_tot = Label(option_modify_frame, text="Nombre Total : ", bg="white", padx=40, font=("Arial,15"))
    label_modify_number_tot.grid(row=1, column=4)

    # Options Entrys
    name_entry = Entry(option_modify_frame, bg="grey")
    name_entry.grid(row=0, column=1)
    date_entry = Entry(option_modify_frame, bg="grey")
    date_entry.grid(row=0, column=3)
    time_entry = Entry(option_modify_frame, bg="grey")
    time_entry.grid(row=0, column=5)
    exercise_entry = Entry(option_modify_frame, bg="grey")
    exercise_entry.grid(row=0, column=7)
    ok_entry = Entry(option_modify_frame, bg="grey")
    ok_entry.grid(row=1, column=3)
    total_entry = Entry(option_modify_frame, bg="grey")
    total_entry.grid(row=1, column=5)

    # Button to hide the insertion window
    button_return = Button(option_modify_frame, text="Retour", font=("Arial,15"),
                           command=lambda: closing_insertion())
    button_return.grid(row=1, column=0, pady=5)

    finish_button = Button(option_modify_frame, text="Confirmer", width=10, height=2,
                           command=lambda: validate_and_finish(name_entry, date_entry, time_entry, exercise_entry,
                                                               ok_entry, total_entry, id, table_type, main_data))
    finish_button.grid(row=1, column=8, pady=10)


# Check if the infos are valid
def validate_and_finish(name_entry, date_entry, time_entry, exercise_entry, ok_entry, total_entry, id, table_type,
                        main_data):
    # Check if any of the entry fields is empty
    if not all(
            entry.get() for entry in [name_entry, date_entry, time_entry, exercise_entry, ok_entry, total_entry]):
        tk.messagebox.showerror("Erreur", "Merci de rentrer toutes les informations.")
        new_modify_window.lift()
        return
    # Continue with modification or creation
    if table_type == "modify":
        modify_or_delete(id, data=[name_entry.get(), date_entry.get(), time_entry.get(), exercise_entry.get(),
                                   ok_entry.get(), total_entry.get()], main_data=main_data)
    else:
        create_result(
            data=[name_entry.get(), date_entry.get(), time_entry.get(), exercise_entry.get(), ok_entry.get(),
                  total_entry.get()], main_data=main_data)


# function for the modify or delete on the right of each rows
def modify_or_delete(id, main_data, data=None):
    if data != None:
        database.modify_result(data, id)
        messagebox.showinfo(title="Modification réussie", message="Les modifications ont été mises à jours.")
        new_modify_window.destroy()
    else:
        database.delete_result(id)
    show_info_filtered(main_data[0], main_data[1])
    show_count_infos(main_data[1])


# create the result
def create_result(main_data, data=None):
    # Get the pseudo from the entry widget
    pseudo = data[0]

    # Check if the pseudo is empty
    if not pseudo.strip():
        # Display an error message if the pseudo is empty
        tk.messagebox.showerror("Error", "Please enter a non-empty pseudo.")
        return  # Return without saving the game

    try:
        player_id = database.get_player_id(data[0])[0]
        games = database.get_exercise_id(data[3])[0]
        date_data = data[1].split(" ")
        date_date_data = date_data[0].split("-")
        date_time_data = date_data[1].split(":")
        final_date = datetime.datetime(int(date_date_data[0]), int(date_date_data[1]), int(date_date_data[2]),
                                       int(date_time_data[0]), int(date_time_data[1]), int(date_time_data[2]))
        final_time = data[2]
        okay_tries = int(data[4])
        total_tries = int(data[5])
        if okay_tries > total_tries:
            okay_tries = 0 / 0
    except:
        tk.messagebox.showerror("Erreur", "Problème avec les données")
        return

    database.create_results(entry_add_player, entry_add_exercise, entry_start_date, entry_add_time, entry_add_number_ok, entry_add_number_tot)
    show_info_filtered(main_data[0], main_data[1])
    show_count_infos(main_data[1])


# Process for closing the connection and the result page
def closing_results():
    result_message = messagebox.askokcancel(title="Information", message="Vous allez quitter la page des résultats.")
    if result_message:
        database.close_dbconnection()
        window_results.destroy()
    else:
        # If the user clicks "Cancel," bring the result window to the foreground
        window_results.lift()


# function for display the result
def display_result():
    database.open_dbconnection()
    global up_window_results, entry_player, entry_exercise, window_results, infos_frame, count_frame
    # Window parameters
    window_results = tk.Tk()
    window_results.title("Résultats")
    window_results.geometry("1920x1080")
    window_results.configure(bg=hex_color)
    window_results.grid_columnconfigure((0, 1, 2), minsize=300, weight=1)

    # Title for the results window
    label_title_results = tk.Label(window_results, text="TRAINING : AFFICHAGE", font=("Arial", 25), borderwidth=2,
                                   relief="solid")
    label_title_results.grid(row=0, column=1, ipady=5, padx=40, pady=40)

    # Frames for the window
    up_window_results = Frame(window_results, bg=hex_color, relief="solid")
    up_window_results.grid(row=1, columnspan=3)
    down_window_results = Frame(window_results, bg=hex_color, relief="solid")
    down_window_results.grid(row=2, columnspan=3)
    option_frame = Frame(up_window_results, bg="white", padx=10, bd=2, relief="solid")
    option_frame.grid(row=1, columnspan=3)
    infos_frame = Frame(up_window_results, bg="white", padx=10, bd=2, relief="solid")
    infos_frame.grid(row=2, pady=10, columnspan=3)
    title_count_frame = Frame(down_window_results, bg="white", padx=10, bd=2, relief="solid")
    title_count_frame.grid(row=3, pady=10, columnspan=3)
    count_frame = Frame(down_window_results, bg="white", padx=10, bd=2, relief="solid")
    count_frame.grid(row=4, pady=10, columnspan=3)
    count_infos_frame = Frame(down_window_results, bg="white", padx=10, bd=2, relief="solid")
    count_infos_frame.grid(row=5, pady=10, columnspan=3)

    # Options labels
    label_player = Label(option_frame, text="Pseudo : ", bg="white", padx=40, font=("Arial,15"))
    label_player.grid(row=0, column=0, padx=(0, 10))
    label_exercises = Label(option_frame, text="Exercice : ", bg="white", padx=40, font=("Arial,15"))
    label_exercises.grid(row=0, column=2, padx=(0, 10))
    label_start_date = Label(option_frame, text="Date de début : ", bg="white", padx=40, font=("Arial,15"))
    label_start_date.grid(row=0, column=4, padx=(0, 10))
    label_end_date = Label(option_frame, text="Date de fin : ", bg="white", padx=40, font=("Arial,15"))
    label_end_date.grid(row=0, column=6, padx=(0, 10))

    # Options Entrys
    entry_player = Entry(option_frame, bg="grey")
    entry_player.grid(row=0, column=1)
    entry_exercise = Entry(option_frame, bg="grey")
    entry_exercise.grid(row=0, column=3)
    entry_start_date = Entry(option_frame, bg="grey")
    entry_start_date.grid(row=0, column=5)
    entry_end_date = Entry(option_frame, bg="grey")
    entry_end_date.grid(row=0, column=7)

    # Totals labels
    title_total = Label(title_count_frame, text="Total", bg="white", font=("Arial, 15"), width=10, borderwidth=2)
    title_total.grid(row=3, pady=10, columnspan=3)
    label_total_line = Label(count_frame, text="Nombre de Lignes", bg="white", padx=15, font=("Arial, 15"))
    label_total_line.grid(row=0, column=0, padx=(0, 10))
    label_time_count = Label(count_frame, text="Temps Total", bg="white", padx=15, font=("Arial, 15"))
    label_time_count.grid(row=0, column=1, padx=(0, 10))
    label_count_number_rok = Label(count_frame, text="Nombre OK", bg="white", padx=15, font=("Arial, 15"))
    label_count_number_rok.grid(row=0, column=2, padx=(0, 10))
    label_line_number_total = Label(count_frame, text="Nombre Total", bg="white", padx=15, font=("Arial, 15"))
    label_line_number_total.grid(row=0, column=3, padx=(0, 10))
    label_purcent = Label(count_frame, text="% Total", bg="white", padx=15, font=("Arial, 15"))
    label_purcent.grid(row=0, column=4, padx=(0, 10))

    show_info_filtered(infos_frame, count_frame)
    # Buttons
    button_show = Button(option_frame, text="Afficher les résultats", font=("Arial,15"),
                         command=lambda: show_info_filtered(infos_frame, count_frame))
    button_show.grid(row=1, column=0, pady=5)

    # Buttons
    button_add = Button(option_frame, text="Ajouter un résultat", font=("Arial,15"),
                        command=lambda: insert_result_window())
    button_add.grid(row=1, column=7, pady=5)

    window_results.protocol("WM_DELETE_WINDOW", closing_results)
    # main loop
    window_results.mainloop()


# Function for the display of the filtered infos
def show_info_filtered(infos_frame, count_frame):
    global window_results
    name = database.filter_results(entry_player.get(), entry_exercise.get())
    for widget in infos_frame.winfo_children():
        if widget.grid_info()["row"] != 0:
            widget.destroy()
    if not name:
        # Display a message if there are no results
        tk.messagebox.showinfo("Information", "Il n'y a aucun résultat inscrit dans la base de donnée.")
        return

    # Results labels
    label_player = Label(infos_frame, text="Élève", bg="white", padx=40, font=("Arial,15"))
    label_player.grid(row=0, column=0, padx=(0, 10))
    label_date_hour = Label(infos_frame, text="Date et Heure", bg="white", padx=40, font=("Arial,15"))
    label_date_hour.grid(row=0, column=1, padx=(0, 10))
    label_time = Label(infos_frame, text="Temps", bg="white", padx=40, font=("Arial,15"))
    label_time.grid(row=0, column=2, padx=(0, 10))
    label_exercise = Label(infos_frame, text="Exercice", bg="white", padx=40, font=("Arial,15"))
    label_exercise.grid(row=0, column=3, padx=(0, 10))
    label_number_ok = Label(infos_frame, text="Nombre OK", bg="white", padx=40, font=("Arial,15"))
    label_number_ok.grid(row=0, column=4, padx=(0, 10))
    label_number_tot = Label(infos_frame, text="Nombre Total", bg="white", padx=40, font=("Arial,15"))
    label_number_tot.grid(row=0, column=5, padx=(0, 10))
    label_done = Label(infos_frame, text="% Réussi", bg="white", padx=40, font=("Arial,15"))
    label_done.grid(row=0, column=6, padx=(0, 10))
    label_actions = Label(infos_frame, text="Actions", bg="white", padx=40, font=("Arial,15"))
    label_actions.grid(row=0, column=7, columnspan=2, padx=(0, 10))  # Adjusted columnspan

    # Add all the infos of the database on the result variable
    for x in range(len(name)):
        if float(name[x][5]) != 0:
            result = round(float(name[x][4]) * 100 / float(name[x][5]), 2)
        else:
            result = 0

        # Add all the infos of result on the frame infos
        for data in range(len(name[x])):
            results = Label(infos_frame, width=15, text=name[x][data])
            results.grid(row=x + 1, column=data)

        for x in range(len(name)):
            if float(name[x][5]) != 0:
                result = round(float(name[x][4]) * 100 / float(name[x][5]), 2)
            else:
                result = 0

            # Add all the infos of result on the frame infos
            for data in range(len(name[x])):
                results = Label(infos_frame, width=15, text=name[x][data])
                results.grid(row=x + 1, column=data)

            # Add buttons for actions using the functions
            delete_button_infos(infos_frame, name[x][6], count_frame, x + 1, 7)
            modify_button_infos(infos_frame, window_results, name[x][6], count_frame, x + 1, 8)

            # Create a canvas for the progress bar after the result is calculated
            canvas = tk.Canvas(infos_frame, width=100, height=20, bg="white")
            canvas.grid(row=x + 1, column=6)

            # Progress bar creation and setup

            # Determine the color based on the result value
            max_value = float(name[x][5])
            ok_value = float(name[x][4])
            average_value = max_value / 2

            # Determine the color of the canvas background
            if ok_value < average_value:
                canvas_bg_color = "red"
            elif ok_value == 0 or max_value == 0:
                canvas_bg_color = "red"
            elif ok_value == average_value:
                canvas_bg_color = "orange"
            else:
                canvas_bg_color = "green"

            # Determine the color of the progress based on the background color
            progress_color = canvas_bg_color

            # Calculate the width of the filled portion based on the result
            fill_width = max(5, int((result / 100) * 100))  # Ensure a minimum width

            # Add a rectangle to represent the progress
            canvas.create_rectangle(0, 0, fill_width, 20, fill=progress_color)

            # Add buttons for actions using the functions
            delete_button_infos(infos_frame, name[x][6], count_frame, x + 1, 7)
            modify_button_infos(infos_frame, window_results, name[x][6], count_frame, x + 1, 8)

    show_count_infos(count_frame)


# function for the total (count)
def show_count_infos(count_frame):
    # Clear existing labels and widgets
    for widget in count_frame.winfo_children():
        if widget.grid_info()["row"] != 0:
            widget.destroy()

    dataset = database.count_total(entry_player.get(), entry_exercise.get())
    if entry_player.get() == '':
        pass

    # Add data values to the frame
    for i, value in enumerate(dataset[0]):
        label = tk.Label(count_frame, width=15, text=value)
        label.grid(row=1, column=i)

    if float(dataset[0][3]) != 0:
        result = round(float(dataset[0][2]) * 100 / float(dataset[0][3]), 2)
    else:
        result = 0

    # Progress bar creation and setup

    # Determine the color based on the result value
    max_value = float(dataset[0][3])
    ok_value = float(dataset[0][2])
    average_value = max_value / 2

    # Determine the color of the canvas background
    if ok_value < average_value:
        canvas_bg_color = "red"
    elif ok_value == 0 or max_value == 0:
        canvas_bg_color = "red"

    elif ok_value == average_value:
        canvas_bg_color = "orange"
    else:
        canvas_bg_color = "green"

    # Create a canvas for the progress bar
    canvas = tk.Canvas(count_frame, width=100, height=20, bg="white")
    canvas.grid(row=1, column=4)

    # Determine the color of the progress based on the background color
    progress_color = canvas_bg_color

    # Calculate the width of the filled portion based on the result
    fill_width = max(5, int((result / 100) * 100))  # Ensure a minimum width

    # Add a rectangle to represent the progress
    canvas.create_rectangle(0, 0, fill_width, 20, fill=progress_color)


# function for adding a result manually
def insert_result_window():
    global window_insert_results,entry_add_player, entry_add_exercise, entry_start_date, entry_add_time, entry_add_number_ok, entry_add_number_tot
    window_insert_results = tk.Tk()
    window_insert_results.title("Insertion")
    window_insert_results.geometry("1920x1080")
    window_insert_results.configure(bg=hex_color)
    window_insert_results.grid_columnconfigure((0, 1, 2), minsize=300, weight=1)

    # Title for the adding results window
    label_title_add_results = tk.Label(window_insert_results, text="Ajout d'un résultat", font=("Arial", 25),
                                       borderwidth=2,
                                       relief="solid")
    label_title_add_results.grid(row=0, column=1, ipady=5, padx=40, pady=40)

    # Frames for the window for the insertion
    up_window_add_results = Frame(window_insert_results, bg=hex_color, relief="solid")
    up_window_add_results.grid(row=1, columnspan=3)
    option_add_frame = Frame(up_window_add_results, bg="white", padx=10, bd=2, relief="solid")
    option_add_frame.grid(row=1, columnspan=3)

    # Options labels
    label_add_player = Label(option_add_frame, text="Pseudo : ", bg="white", padx=40, font=("Arial,15"))
    label_add_player.grid(row=0, column=0)
    label_add_exercises = Label(option_add_frame, text="Exercice : ", bg="white", padx=40, font=("Arial,15"))
    label_add_exercises.grid(row=0, column=2)
    label_add_start_date = Label(option_add_frame, text="Date de début : ", bg="white", padx=40, font=("Arial,15"))
    label_add_start_date.grid(row=0, column=4)
    label_add_time = Label(option_add_frame, text="Temps : ", bg="white", padx=40, font=("Arial,15"))
    label_add_time.grid(row=0, column=6)
    label_add_start_date = Label(option_add_frame, text="Nombre OK : ", bg="white", padx=40, font=("Arial,15"))
    label_add_start_date.grid(row=1, column=2)
    label_add_end_date = Label(option_add_frame, text="Nombre Total : ", bg="white", padx=40, font=("Arial,15"))
    label_add_end_date.grid(row=1, column=4)

    # Options Entrys
    entry_add_player = Entry(option_add_frame, bg="grey")
    entry_add_player.grid(row=0, column=1)

    entry_add_exercise = Entry(option_add_frame, bg="grey")
    entry_add_exercise.grid(row=0, column=3)

    entry_start_date = Entry(option_add_frame, bg="grey")
    entry_start_date.grid(row=0, column=5)

    entry_add_time = Entry(option_add_frame, bg="grey")
    entry_add_time.grid(row=0, column=7)

    entry_add_number_ok = Entry(option_add_frame, bg="grey")
    entry_add_number_ok.grid(row=1, column=3)

    entry_add_number_tot = Entry(option_add_frame, bg="grey")
    entry_add_number_tot.grid(row=1, column=5)

    # Button to hide the insertion window
    button_return = Button(option_add_frame, text="Retour", font=("Arial,15"),
                           command=lambda: closing_insertion())
    button_return.grid(row=1, column=0, pady=5)

    # Buttons
    confirmation_result = Button(option_add_frame, text="Confirmer", font=("Arial,15"), command=get_creation)
    confirmation_result.grid(row=1, column=9, pady=5)


# Function to take the data for create row
def get_creation():
    global entry_add_player, entry_add_exercise, entry_start_date, entry_add_time, entry_add_number_ok, entry_add_number_tot

    # Retrieve user input from entry widgets
    player = entry_add_player.get()
    exercise = entry_add_exercise.get()
    start_date = entry_start_date.get()
    time = entry_add_time.get()
    nbok = entry_add_number_ok.get()
    nbtot = entry_add_number_tot.get()

    # Check if any field is empty
    if player == "" or exercise == "" or start_date == "" or time == "" or nbok == "" or nbtot == "":
        messagebox.showerror(parent=insert_result_window(), title="Erreur", message="Merci de bien remplir toutes les informations")
        window_insert_results.destroy()
    else:
        # Insert data into the database
        # Change the order of parameters when calling creation_result
        database.creation_result(player, exercise, start_date, time, nbok, nbtot)
        show_info_filtered(infos_frame, count_frame)
        show_count_infos(count_frame)
        messagebox.showinfo(title="Succès", message="Vos données ont bien été pris en compte")
        window_insert_results.destroy()


display_result()
