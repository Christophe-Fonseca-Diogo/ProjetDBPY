import tkinter as tk
from tkinter import ttk

import database
from Utilities import *


def save_player_info():
    level_player = entry_player_level.get()
    player = entry_player_name.get()
    database.update_player_level(level_player, player)
    messagebox.showinfo(title="Changement effectué",message=f"Vous avez bien modifier le niveau de {player}")

def admin_window():
    global entry_player_level,entry_player_name

    # Window parameters
    window_admin = tk.Tk()
    window_admin.title("Admin Panel")
    window_admin.geometry("600x400")

    # Title for the admin window
    label_title_Admin = ttk.Label(window_admin, text="Admin Panel", font=("Arial", 20))
    label_title_Admin.pack(pady=10)

    # Entry for player name
    label_player_name = ttk.Label(window_admin, text="Pseudo du Joueur:")
    label_player_name.pack(pady=5)
    entry_player_name = ttk.Entry(window_admin)
    entry_player_name.pack(pady=10)

    # Entry for player level
    label_player_level = ttk.Label(window_admin, text="Niveau du joueur:")
    label_player_level.pack(pady=5)
    entry_player_level = ttk.Entry(window_admin)
    entry_player_level.pack(pady=10)

    # Button to save player info
    save_button = ttk.Button(window_admin, text="Sauvegarder", command=save_player_info)
    save_button.pack(pady=20)

    window_admin.mainloop()
