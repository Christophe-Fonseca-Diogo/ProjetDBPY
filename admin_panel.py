# Admin Panel
# Made by Christophe
# Version 1
# Date 16.01.2024

import tkinter as tk
from tkinter import ttk, messagebox
import database


# Function for saving the level of the player in the administration
def save_player_info():
    level_player = entry_player_level.get()
    player = entry_player_name.get()

    if level_player == "" or player == "":
        messagebox.showerror(title="Erreur", message="Merci de rentrer des informations.")
    else:
        try:
            level_player = int(level_player)
            if level_player > 2:
                messagebox.showerror(title="Erreur", message="Le niveau de joueur ne doit pas être plus grand que 2.")
            elif level_player <= 0:
                messagebox.showerror(title="Erreur", message="Le niveau du joueur doit être strictement supérieur à 0.")
            else:
                if database.update_player_level(level_player, player):
                    messagebox.showinfo(title="Changement effectué", message=f"Vous avez bien modifié le niveau du joueur.")
                    window_admin.destroy()
                else:
                    messagebox.showwarning(title="Échec de modification", message=f"Le joueur avec le pseudo {player} n'existe pas.")
        except ValueError:
            messagebox.showerror(title="Erreur", message="Le niveau du joueur doit être un nombre entier.")


# Admin window for the pannel
def admin_window():
    global entry_player_level, entry_player_name,window_admin

    # Window parameters
    window_admin = tk.Tk()
    window_admin.title("Administration")
    window_admin.geometry("600x400")
    window_admin.configure(bg="cyan")

    # Title for the admin window
    label_title_Admin = ttk.Label(window_admin, text="Administration", font=("Arial", 20))
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

    # Entry for help
    label_player_level = ttk.Label(window_admin, text="Niveaux :1 = Eleve | 2 = Prof ")
    label_player_level.pack(pady=5)

    # Button to save player info
    save_button = ttk.Button(window_admin, text="Sauvegarder", command=save_player_info)
    save_button.pack(pady=20)

    window_admin.mainloop()
