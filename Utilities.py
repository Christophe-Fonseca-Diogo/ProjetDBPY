
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from Register import register_window
# color definition
rgb_color = (139, 201, 194)
hex_color = '#%02x%02x%02x' % rgb_color # translation in hexa

# function for when the player quit the windows for going to login
def closing_insertion():
    result_message = messagebox.askyesno(title="Information", message="Vous allez quitter la page.")
    if result_message:
        window_register.destroy()
    else:
        # If the user clicks "Cancel," bring the insertion window to the foreground
        window_register.lift()

def checkpw():
    # Gets
    player_get = entry_player_register.get()
    password_get = entry_password_register.get()
    password_check_get = entry_password_check_register.get()
    if password_get != password_check_get:
        print("mot de passe pas le même")
    if player_get == '' or password_get == "" or password_check_get == "":
        print("Rien")
