# Utilities
# Made by Christophe
# Version 1
# Date 15.01.2024

from tkinter import *
from tkinter import messagebox
import tkinter as tk


# color definition

class Theme:
    def __init__(self):
        self.rgb_color = (139, 201, 194)
        self.hex_color = '#%02x%02x%02x' % self.rgb_color  # translation in hexa


local_theme = Theme()


def closing_insertion(window):
    result_message = messagebox.askyesno(title="Information", message="Vous allez quitter la page.")
    if result_message:
        window.destroy()
    else:
        # If the user clicks "Cancel," bring the insertion window to the foreground
        window.lift()


def checkpw(username, password, paswwordcheck):
    # Gets
    player_get = username.get()
    password_get = password.get()
    password_check_get = paswwordcheck.get()
    if player_get == '' or password_get == "" or password_check_get == "":
        messagebox.showinfo(title="Erreur", message="Utilisateur Manquant")
        return False
    if password_get != password_check_get:
        messagebox.showinfo(title="Erreur", message="Mot de passe pas identique")
        return False
    return True


def show(password_entry, check):
    password_entry.configure(show='')
    check.configure(command=lambda: hide(password_entry, check), text='hide password')


def hide(password_entry, check):
    password_entry.configure(show='*')
    check.configure(command=lambda: show(password_entry, check), text='show password')