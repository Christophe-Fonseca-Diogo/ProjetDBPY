import database
import tkinter

def assign_prof_level(selected_user_id):
    # Fonction pour attribuer le niveau 2 (prof) à un utilisateur
    database.assign_user_level(selected_user_id, 2)
    # Mettez à jour l'affichage ou effectuez d'autres actions nécessaires

def admin_window():
    def on_tree_select(event):
        # Fonction appelée lorsqu'un élément dans le Treeview est sélectionné
        selected_item = tree.selection()
        if selected_item:
            selected_user_id = tree.item(selected_item, 'values')[0]
            assign_button['state'] = 'normal'
            assign_button['command'] = lambda: assign_prof_level(selected_user_id)
        else:
            assign_button['state'] = 'disabled'

    # Window parameters
    window_admin = ttk.Tk()
    window_admin.title("Admin Panel")
    window_admin.geometry("1000x300")
    window_admin.grid_columnconfigure((0, 1, 2), minsize=300, weight=1)

    # Title for the results window
    label_title_Admin = ttk.Label(window_admin, text="Admin Panel", font=("Arial", 25), borderwidth=2,
                                 relief="solid")
    label_title_Admin.grid(row=0, column=1, ipady=5, padx=40, pady=40)

    frame_admin = tk.Frame(window_admin, bg="white", padx=10, bd=2, relief="solid")
    frame_admin.grid(row=1, columnspan=3)

    # Fetch all players
    players = database.fetch_all_players()

    # Get the column names from the database
    column_names = [column[0] for column in database.fetch_columns_from_players()]

    # Create Treeview to display players
    tree = ttk.Treeview(frame_admin, columns=column_names, show="headings")
    tree.grid(row=0, column=0, padx=10, pady=10)

    # Add headings to the Treeview
    for column_name in column_names:
        tree.heading(column_name, text=column_name)

    # Add player data to the Treeview
    for player in players:
        tree.insert("", "end", values=player)

    # Bind the treeview select event
    tree.bind('<ButtonRelease-1>', on_tree_select)

    # Button to assign level 2 (prof)
    assign_button = tk.Button(frame_admin, text="Assign Level 2 (Prof)", state='disabled')
    assign_button.grid(row=1, column=0, pady=10)

    window_admin.mainloop()

admin_window()