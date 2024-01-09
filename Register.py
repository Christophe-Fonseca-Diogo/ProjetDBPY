from Utilities import *

def show():
    entry_password_register.configure(show='')
    check.configure(command=hide, text='hide password')


def hide():
    entry_password_register.configure(show='*')
    check.configure(command=show, text='show password')
def register_window():
    global window_register,entry_password_register,entry_password_check_register,entry_player_register,check
    # Window parameters
    window_register = tk.Tk()
    window_register.title("Enregistrement")
    window_register.geometry("1000x300")
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

    # Entrys
    entry_player_register = Entry(frame_register, bg="grey")
    entry_player_register.grid(row=0, column=2)
    entry_password_register = Entry(frame_register, bg="grey",show="*")
    entry_password_register.grid(row=1, column=2)
    entry_password_check_register = Entry(frame_register, bg="grey",show="*")
    entry_password_check_register.grid(row=2, column=2)


    # Buttons
    button_show = Button(frame_register, text="Annuler", font=("Arial,15"), command=closing_insertion)
    button_show.grid(row=1, column=0, pady=5)
    check = Checkbutton(window_register, text='show password', command=show)
    # Buttons
    button_add = Button(frame_register, text="Enregistrer", font=("Arial,15"), command=checkpw)
    button_add.grid(row=1, column=10, pady=5,padx=20)

    check.grid(row=1, column=2)
    # main loop
    window_register.mainloop()

register_window()