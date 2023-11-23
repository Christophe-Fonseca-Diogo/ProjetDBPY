# Menu
# Made by Christophe
# Version 1
# Date 23.11.2023

# Importing modules
import tkinter as tk
from tkinter import *
import database
import geo01
import info02
import info05

# Definition of exercises
a_exercise = ["geo01", "info02", "info05"]
albl_image = [None, None, None]  # array of labels (with images)
a_image = [None, None, None]  # array of images
a_title = [None, None, None]  # array of titles (e.g., GEO01)

# Dictionary of games with links to corresponding functions
dict_games = {"geo01": geo01.open_window_geo_01, "info02": info02.open_window_info_02, "info05": info05.open_window_info_05}

# Function to open other windows (exercises)
def exercise(event, exer):
    dict_games[exer](window)

# Function to display results
def display_result(event):
    window_results = Tk()

    # Window parameters
    window_results.title("Résultats")
    window_results.geometry("1920x1080")
    window_results.configure(bg=hex_color)
    window_results.grid_columnconfigure((0, 1, 2), minsize=300, weight=1)

    # Frames for the window
    option_frame = Frame(window_results, bg="white", padx=10, bd=2, relief="solid")
    results_frame = Frame(window_results, bg="white", padx=10, bd=2, relief="solid")
    title_total_frame = Frame(window_results, bg="white", padx=10, bd=2, relief="solid")
    total_frame = Frame(window_results, bg="white", padx=10, bd=2, relief="solid")

    # Title for the results window
    label_title_results = tk.Label(window_results, text="TRAINING : AFFICHAGE", font=("Arial", 25), borderwidth=2, relief="solid")
    label_title_results.grid(row=0, column=1, ipady=5, padx=40, pady=40)

    # Option labels
    label_player = Label(option_frame, text="Pseudo : ", bg="white", padx=40, font=("Arial,15"))
    label_exercises = Label(option_frame, text="Exercice : ", bg="white", padx=40, font=("Arial,15"))
    label_start_date = Label(option_frame, text="Date de début : ", bg="white", padx=40, font=("Arial,15"))
    label_end_date = Label(option_frame, text="Date de fin : ", bg="white", padx=40, font=("Arial,15"))

    # Label placement
    label_player.grid(row=0, column=0, padx=(0, 10))
    label_exercises.grid(row=0, column=2, padx=(0, 10))
    label_start_date.grid(row=0, column=4, padx=(0, 10))
    label_end_date.grid(row=0, column=6, padx=(0, 10))

    # Option Entry
    entry_player = Entry(option_frame, bg="grey")
    entry_exercise = Entry(option_frame, bg="grey")
    entry_startdate = Entry(option_frame, bg="grey")
    entry_enddate = Entry(option_frame, bg="grey")

    # Entry placement
    entry_player.grid(row=0, column=1)
    entry_exercise.grid(row=0, column=3)
    entry_startdate.grid(row=0, column=5)
    entry_enddate.grid(row=0, column=7)

    # Results labels
    label_player = Label(results_frame, text="Élève", bg="white", padx=40, font=("Arial,15"))
    label_date_hour = Label(results_frame, text="Date et Heure", bg="white", padx=40, font=("Arial,10"))
    label_time = Label(results_frame, text="Temps", bg="white", padx=40, font=("Arial,15"))
    # Im forced to put the grid here or it dosn't appear
    label_time.grid(row=0, column=2, padx=(0, 10))
    label_ex = Label(results_frame, text="Exercice", bg="white", padx=40, font=("Arial,15"))
    label_nbok = Label(results_frame, text="Nombre OK", bg="white", padx=40, font=("Arial,15"))
    # Im forced to put the grid here or it dosn't appear
    label_nbok.grid(row=0, column=4, padx=(0, 10))
    label_nbtot = Label(results_frame, text="Nombre Total", bg="white", padx=40, font=("Arial,15"))
    label_reussi = Label(results_frame, text="% Réussi", bg="white", padx=40, font=("Arial,15"))

    # Totals labels
    title_total = Label(title_total_frame, text="Total", bg="white", font=("Arial, 15"), width=10, borderwidth=2)
    label_tot = Label(total_frame, text="Nombre Lignes", bg="white", padx=40, font=("Arial, 15"))
    label_time = Label(total_frame, text="Temps Total", bg="white", padx=40, font=("Arial, 15"))
    label_nbok = Label(total_frame, text="Nombre OK", bg="white", padx=40, font=("Arial, 15"))
    label_nbtotal = Label(total_frame, text="Nombre Total", bg="white", padx=40, font=("Arial, 15"))
    label_purcenttot = Label(total_frame, text="% Total", bg="white", padx=40, font=("Arial, 15"))

    # Labels second frame
    label_player.grid(row=0, column=0, padx=(0, 10))
    label_date_hour.grid(row=0, column=1, padx=(0, 10))

    label_ex.grid(row=0, column=3, padx=(0, 10))
    label_nbtot.grid(row=0, column=5, padx=(0, 10))
    label_reussi.grid(row=0, column=6, padx=(0, 10))

    # Last Frame labels placements
    title_total_frame.grid(row=3, pady=10, columnspan=3)
    title_total.grid(row=3, pady=10, columnspan=3)
    label_tot.grid(row=0, column=0, padx=(0, 10))
    label_time.grid(row=0, column=1, padx=(0, 10))
    label_nbok.grid(row=0, column=2, padx=(0, 10))
    label_nbtotal.grid(row=0, column=3, padx=(0, 10))
    label_purcenttot.grid(row=0, column=4, padx=(0, 10))

    # Frames placement
    option_frame.grid(row=1, columnspan=3)
    results_frame.grid(row=2, pady=10, columnspan=3)
    total_frame.grid(row=4, pady=10, columnspan=3)

    # Buttons
    button_result = Button(option_frame, text="Voir résultats", font=("Arial,15"))
    button_result.grid(row=1, column=0, pady=5)

    database.open_dbconnection()
    name = database.show_results()
    for x in range(len(name)):
        if float(name[x][5]) != 0:
            result = round(float(name[x][4]) * 100 / float(name[x][5]), 2)
        else:
            result = 0

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

        # Create a canvas for the progress bar
        canvas = tk.Canvas(results_frame, width=100, height=20, bg="white")
        canvas.grid(row=x + 1, column=6)

        # Determine the color of the progress based on the background color
        progress_color = canvas_bg_color

        # Calculate the width of the filled portion based on the result
        fill_width = max(5, int((result / 100) * 100))  # Ensure a minimum width

        # Add a rectangle to represent the progress
        canvas.create_rectangle(0, 0, fill_width, 20, fill=progress_color)

        for data in range(len(name[x])):
            results = Label(results_frame, width=15, text=name[x][data])
            results.grid(row=x + 1, column=data)

    database.close_dbconnection()

    # main loop
    window.mainloop()
    print("display_result")


# Main window
window = tk.Tk()
window.title("Training, entrainement cérébral")
window.geometry("1100x900")

# color définition
rgb_color = (139, 201, 194)
hex_color = '#%02x%02x%02x' % rgb_color # translation in hexa
window.configure(bg=hex_color)
window.grid_columnconfigure((0,1,2), minsize=300, weight=1)

# Title création
lbl_title = tk.Label(window, text="TRAINING MENU", font=("Arial", 15))
lbl_title.grid(row=0, column=1,ipady=5, padx=40,pady=40)

# labels creation and positioning
for ex in range(len(a_exercise)):
    a_title[ex]=tk.Label(window, text=a_exercise[ex], font=("Arial", 15))
    a_title[ex].grid(row=1+2*(ex//3),column=ex % 3 , padx=40,pady=10) # 3 label per row

    a_image[ex] = tk.PhotoImage(file="img/" + a_exercise[ex] + ".gif") # image name
    albl_image[ex] = tk.Label(window, image=a_image[ex]) # put image on label
    albl_image[ex].grid(row=2 + 2*(ex // 3), column=ex % 3, padx=40, pady=10) # 3 label per row
    albl_image[ex].bind("<Button-1>", lambda event, ex = ex :exercise(event=None, exer=a_exercise[ex])) #link to others .py
    print(a_exercise[ex])

# Buttons, display results & quit
btn_display = tk.Button(window, text="Display results", font=("Arial", 15))
btn_display.grid(row=1+ 2*len(a_exercise)//3 , column=1)
btn_display.bind("<Button-1>",lambda e: display_result(e))

btn_finish = tk.Button(window, text="Quitter", font=("Arial", 15))
btn_finish.grid(row=2+ 2*len(a_exercise)//3 , column=1)
btn_finish.bind("<Button-1>", quit)

# main loop
window.mainloop()
