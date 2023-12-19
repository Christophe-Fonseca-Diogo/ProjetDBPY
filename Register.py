# Register
# Made by Christophe
# Version 1
# Date 15.12.2023


from results import closing_insertion
from tkinter import *
from tkinter import messagebox
import tkinter as tk

# color definition
rgb_color = (139, 201, 194)
hex_color = '#%02x%02x%02x' % rgb_color # translation in hexa




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

    # Buttons
    button_show = Button(option_frame, text="Annuler", font=("Arial,15"),
                         command=lambda: closing_insertion)
    button_show.grid(row=1, column=0, pady=5)

    # Buttons
    button_add = Button(option_frame, text="Enregistrer", font=("Arial,15"),
                        command=lambda: insert_result_window())
    button_add.grid(row=1, column=7, pady=5)

    window_results.protocol("WM_DELETE_WINDOW", closing_results)
    # main loop
    window_results.mainloop()
