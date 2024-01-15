# Admin Panel
# Made by Christophe
# Version 1
# Date 15.01.2024
from database import fetch_all_players, fetch_columns_from_players
from tkinter import ttk
def admin_window():
    # Window parameters
    window_admin = tk.Tk()
    window_admin.title("Admin Panel")
    window_admin.geometry("1000x300")
    window_admin.grid_columnconfigure((0, 1, 2), minsize=300, weight=1)

    # Title for the results window
    label_title_Admin = ttk.Label(window_admin, text="Admin Panel", font=("Arial", 25), borderwidth=2,
                                 relief="solid")
    label_title_Admin.grid(row=0, column=1, ipady=5, padx=40, pady=40)

    frame_login = ttk.Frame(window_admin, bg="white", padx=10, bd=2, relief="solid")
    frame_login.grid(row=1, columnspan=3)

    # Fetch all players
    players = fetch_all_players()

    # Get the column names from the database
    column_names = [column[0] for column in fetch_columns_from_players()]

    # Create Treeview to display players
    tree = ttk.Treeview(frame_login, columns=column_names, show="headings")
    tree.grid(row=0, column=0, padx=10, pady=10)

    # Add headings to the Treeview
    for column_name in column_names:
        tree.heading(column_name, text=column_name)

    # Add player data to the Treeview
    for player in players:
        tree.insert("", "end", values=player)

    window_admin.mainloop()
admin_window()