import tkinter as tk
import database
from tkinter import *


# Function to create the windows results
rgb_color = (139, 201, 194)
hex_color = '#%02x%02x%02x' % rgb_color  # translation in hexa


# Process for closing the connection
def on_closing_results():
    print("close_connection_results")
    database.close_dbconnection()
    window_results.destroy()


def display_result():
    print("In the results")
    database.open_dbconnection()
    global up_window_results, entry_player, entry_exercise, window_results,count_infos_frame
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
    pages_frame = Frame(down_window_results, bg=hex_color, padx=10, bd=2)
    pages_frame.grid(row=41, pady=10, columnspan=4)
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
    button_show = Button(option_frame, text="Afficher les résultats", font=("Arial,15"),
                         command=lambda: show_info_filtered(infos_frame,count_frame))
    button_show.grid(row=1, column=0, pady=5)

    # Buttons
    button_next_page = Button(pages_frame, text="Page anterieur", font=("Arial,15"),
                              command=lambda: show_info_filtered(infos_frame), relief="ridge")
    button_next_page.grid(row=1, column=0, pady=5)

    # Buttons
    button_previous = Button(pages_frame, text="Page suivante", font=("Arial,15"),
                             command=lambda: show_info_filtered(infos_frame), relief="ridge")
    button_previous.grid(row=1, column=2, pady=5)

    window_results.protocol("WM_DELETE_WINDOW", on_closing_results)
    # main loop
    window_results.mainloop()


# Function for the display of the filtered infos
def show_info_filtered(infos_frame,count_frame):
    global window_results
    name = database.filter_results(entry_player.get(), entry_exercise.get())
    for widget in infos_frame.winfo_children():
        if widget.grid_info()["row"] != 0:
            widget.destroy()

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

    # Add all the infos of the database on the result variable
    for x in range(len(name)):
        if float(name[x][5]) != 0:
            result = round(float(name[x][4]) * 100 / float(name[x][5]), 2)
        else:
            result = 0

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

        # Create a canvas for the progress bar
        canvas = tk.Canvas(infos_frame, width=100, height=20, bg="white")
        canvas.grid(row=x + 1, column=6)

        # Determine the color of the progress based on the background color
        progress_color = canvas_bg_color

        # Calculate the width of the filled portion based on the result
        fill_width = max(5, int((result / 100) * 100))  # Ensure a minimum width

        # Add a rectangle to represent the progress
        canvas.create_rectangle(0, 0, fill_width, 20, fill=progress_color)

        # Add all the infos of result on the frame infos
        for data in range(len(name[x])):
            results = Label(infos_frame, width=15, text=name[x][data])
            results.grid(row=x + 1, column=data)
    show_count_infos(count_frame)


def show_count_infos(count_frame):
    # Clear existing labels and widgets
    for widget in count_frame.winfo_children():
        if widget.grid_info()["row"] != 0:
            widget.destroy()

    dataset = database.count_total(entry_player.get(), entry_exercise.get())
    if entry_player.get() == '':
        print("Rien")

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


display_result()