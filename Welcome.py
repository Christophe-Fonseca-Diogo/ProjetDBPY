# Welcome
# Made by Christophe
# Version 1
# Date 15.01.2024

from Utilities import *
from Login import *
from Register import register_window
from database import open_dbconnection
from database import addAdmin


def start_script():

    global window_before
    # Window parameters
    window_before = tk.Tk()
    window_before.title("Bienvenue")
    window_before.geometry("600x300")
    window_before.configure(bg=local_theme.hex_color)
    window_before.grid_columnconfigure((0, 1, 2), minsize=100, weight=1)

    # Title for the results window
    label_title_before = tk.Label(window_before, text="Bienvenue", font=("Arial", 25), borderwidth=2,
                                   relief="solid")
    label_title_before.grid(row=0, column=1, ipady=5, padx=40, pady=40)


    frame_before = Frame(window_before, bg="white", padx=10, bd=2, relief="solid")
    frame_before.grid(row=1, columnspan=3)

    # Buttons
    button_show = Button(frame_before, text="S'inscrire", font=("Arial,15"), command=lambda: register_window(window_before))
    button_show.grid(row=1, column=0, pady=5,padx=5)

    # Buttons
    button_add = Button(frame_before, text="Se connecter", font=("Arial,15"), command=lambda: login_window(window_before))
    button_add.grid(row=1, column=10, pady=5,padx=5)

    # main loop
    window_before.mainloop()

if __name__ == "__main__":
    open_dbconnection()
    addAdmin()
    start_script()

