# Register
# Made by Christophe
# Version 1
# Date 15.12.2023


from tkinter import *
from tkinter import messagebox
import tkinter as tk



# color definition
rgb_color = (139, 201, 194)
hex_color = '#%02x%02x%02x' % rgb_color # translation in hexa
# function for when the player quit windows




# function for when the player quit the windows for going to login
def closing_insertion():
    result_message = messagebox.askyesno(title="Information", message="Vous allez quitter la page.")
    if result_message:
        window_register.destroy()
    else:
        # If the user clicks "Cancel," bring the insertion window to the foreground
        window_register.lift()



# function for display the result
def register_window():
    global window_register
    # Window parameters
    window_register = tk.Tk()
    window_register.title("Enregistrement")
    window_register.geometry("1000x400")
    window_register.configure(bg=hex_color)
    window_register.grid_columnconfigure((0, 1, 2), minsize=300, weight=1)

    # Title for the results window
    label_title_register = tk.Label(window_register, text="Enregistrement", font=("Arial", 25), borderwidth=2,
                                   relief="solid")
    label_title_register.grid(row=0, column=1, ipady=5, padx=40, pady=40)


    frame_register = Frame(window_register, bg="white", padx=10, bd=2, relief="solid")
    frame_register.grid(row=1, columnspan=3)


    # labels register
    label_player_register = Label(frame_register, text="Nom d'utilisateur : ", bg="white", padx=40, font=("Arial,15"))
    label_player_register.grid(row=0, column=1, padx=(0, 10))
    label_password_register = Label(frame_register, text="Mot de passe : ", bg="white", padx=40, font=("Arial,15"))
    label_password_register.grid(row=1, column=1, padx=(0, 10))
    label_password_check_register = Label(frame_register, text="Confirmation mot de passe : ", bg="white", padx=40, font=("Arial,15"))
    label_password_check_register.grid(row=2, column=1, padx=(0, 10))

    # Options Entrys
    entry_player_register = Entry(frame_register, bg="grey")
    entry_player_register.grid(row=0, column=2)
    label_password_register = Entry(frame_register, bg="grey")
    label_password_register.grid(row=1, column=2)
    label_password_check_register = Entry(frame_register, bg="grey")
    label_password_check_register.grid(row=2, column=2)

    # Buttons
    button_show = Button(frame_register, text="Annuler", font=("Arial,15"), command=closing_insertion)
    button_show.grid(row=1, column=0, pady=5)

    # Buttons
    button_add = Button(frame_register, text="Enregistrer", font=("Arial,15"))
    button_add.grid(row=1, column=10, pady=5,padx=20)

    # main loop
    window_register.mainloop()


# function for display the result
def login_window():
    global window_login
    # Window parameters
    window_login = tk.Tk()
    window_login.title("Connection")
    window_login.geometry("1000x400")
    window_login.configure(bg=hex_color)
    window_login.grid_columnconfigure((0, 1, 2), minsize=300, weight=1)

    # Title for the results window
    label_title_login = tk.Label(window_login, text="Connection", font=("Arial", 25), borderwidth=2,
                                   relief="solid")
    label_title_login.grid(row=0, column=1, ipady=5, padx=40, pady=40)


    frame_login = Frame(window_login, bg="white", padx=10, bd=2, relief="solid")
    frame_login.grid(row=1, columnspan=3)


    # Options labels
    label_player_login = Label(frame_login, text="Nom d'utilisateur : ", bg="white", padx=40, font=("Arial,15"))
    label_player_login.grid(row=0, column=1, padx=(0, 10))
    label_password_login = Label(frame_login, text="Mot de passe : ", bg="white", padx=40, font=("Arial,15"))
    label_password_login.grid(row=1, column=1, padx=(0, 10))


    # Options Entrys
    entry_player_register = Entry(frame_login, bg="grey")
    entry_player_register.grid(row=0, column=2)
    label_password_register = Entry(frame_login, bg="grey")
    label_password_register.grid(row=1, column=2)


    # Buttons
    button_show = Button(frame_login, text="S'inscrire", font=("Arial,15"), command=register_window)
    button_show.grid(row=1, column=0,pady=30)

    # Buttons
    button_add = Button(frame_login, text="Se connecter", font=("Arial,15"))
    button_add.grid(row=1, column=10,pady=30)

    # main loop
    window_login.mainloop()



def before():
    global window_before
    # Window parameters
    window_before = tk.Tk()
    window_before.title("Bienvenue")
    window_before.geometry("600x400")
    window_before.configure(bg=hex_color)
    window_before.grid_columnconfigure((0, 1, 2), minsize=100, weight=1)

    # Title for the results window
    label_title_before = tk.Label(window_before, text="Bienvenue", font=("Arial", 25), borderwidth=2,
                                   relief="solid")
    label_title_before.grid(row=0, column=1, ipady=5, padx=40, pady=40)


    frame_before = Frame(window_before, bg="white", padx=10, bd=2, relief="solid")
    frame_before.grid(row=1, columnspan=3)

    # Buttons
    button_show = Button(frame_before, text="S'inscrire", font=("Arial,15"), command=register_window)
    button_show.grid(row=1, column=0, pady=5,padx=5)

    # Buttons
    button_add = Button(frame_before, text="Se connecter", font=("Arial,15"), command= login_window)
    button_add.grid(row=1, column=10, pady=5,padx=5)

    # main loop
    window_before.mainloop()


before()