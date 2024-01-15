# Menu
# Made by Christophe
# Version 1
# Date 15.12.2023
import subprocess

# Importing modules
import info02
import info05
import geo01
import database
import tkinter as tk
import subprocess
from Welcome import start_script

# Definition of exercises
a_exercise = ["geo01", "info02", "info05"]
albl_image = [None, None, None]  # array of labels (with images)
a_image = [None, None, None]  # array of images
a_title = [None, None, None]  # array of titles (e.g., GEO01)
number = 0

# Dictionary of games with links to corresponding functions
dict_games = {"geo01": geo01.open_window_geo_01, "info02": info02.open_window_info_02, "info05": info05.open_window_info_05}


# Function to open other windows (exercises)
def exercise(event, exer, window, username):
    dict_games[exer](window, username)


# close menu connection with parameter
def on_closing(event, window):
    free_ressources(window)


# close menu connection
def delete_window(window):
    free_ressources(window)


# destroy the windows and stop the connection with the database
def free_ressources(window):
    database.close_dbconnection()
    window.destroy()


# open the window results
def display_results(event):
    subprocess.Popen(["python","results.py"])


def logout():
    window.destroy()
    start_script()


def admin_button(username):
    from database import check_account_level
    from admin_panel import admin_window
    level = check_account_level(username)
    if int(level) == 3:
        # Button admin panel
        btn_admin = tk.Button(window, text="Admin Panel", font=("Arial", 15))
        btn_admin.grid(row=1 + 2 * len(a_exercise) // 3, column=1)
        btn_admin.bind("<Button-1>", lambda e: admin_window())
    else:
        print("Unable to retrieve the level for the logged-in user.")


def open_window(username):
    global window
    # Main window
    window = tk.Tk()
    window.title("Training, entrainement cérébral")
    window.geometry("1100x900")

    database.open_dbconnection()

    # color definition
    rgb_color = (139, 201, 194)
    hex_color = '#%02x%02x%02x' % rgb_color # translation in hexa
    window.configure(bg=hex_color)
    window.grid_columnconfigure((0,1,2), minsize=300, weight=1)

    # Title creation
    lbl_title = tk.Label(window, text="TRAINING MENU", font=("Arial", 15))
    lbl_title.grid(row=0, column=1,ipady=5, padx=40,pady=40)

    # Labels creation and positioning
    for ex in range(len(a_exercise)):
        a_title[ex]=tk.Label(window, text=a_exercise[ex], font=("Arial", 15))
        a_title[ex].grid(row=1+2*(ex//3),column=ex % 3 , padx=40,pady=10) # 3 label per row

        a_image[ex] = tk.PhotoImage(file="img/" + a_exercise[ex] + ".gif") # image name
        albl_image[ex] = tk.Label(window, image=a_image[ex]) # put image on label
        albl_image[ex].grid(row=2 + 2*(ex // 3), column=ex % 3, padx=40, pady=10) # 3 label per row
        albl_image[ex].bind("<Button-1>", lambda event, ex = ex :exercise(event=None, exer=a_exercise[ex],
                                                                window=window, username=username)) #link to others .py
        print(a_exercise[ex])


    # Buttons, display results & quit
    btn_display = tk.Button(window, text="Display results", font=("Arial", 15))
    btn_display.grid(row=2 + 2 * len(a_exercise) // 3, column=1)
    btn_display.bind("<Button-1>", lambda e: display_results(e))

    btn_logout = tk.Button(window, text="Logout", font=("Arial", 15))
    btn_logout.grid(row=3+ 2*len(a_exercise)//3 , column=1)
    btn_logout.bind("<Button-1>", lambda event: logout())

    btn_finish = tk.Button(window, text="Quitter", font=("Arial", 15))
    btn_finish.grid(row=4+ 2*len(a_exercise)//3 , column=1)
    btn_finish.bind("<Button-1>", lambda event: on_closing(event, window))

    window.protocol("WM_DELETE_WINDOW", lambda: delete_window(window))

    # Main loop
    admin_button(username)
    window.mainloop()
