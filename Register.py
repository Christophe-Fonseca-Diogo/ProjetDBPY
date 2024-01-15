from Utilities import *
import bcrypt
import database

def hash_password(password):
   password_bytes = password.encode('utf-8')
   hashed_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
   return hashed_bytes



def register_window():
    global window_register,entry_password_register,entry_password_check_register,entry_player_register,check,value_player,value_password,value_checkpassword,passwordhashed
    # Window parameters
    window_register = tk.Tk()
    window_register.title("Enregistrement")
    window_register.geometry("1000x300")
    window_register.configure(bg=local_theme.hex_color)
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
    value_player = entry_player_register.get()
    entry_password_register = Entry(frame_register, bg="grey",show="*")
    entry_password_register.grid(row=1, column=2)
    value_password = entry_password_register.get()
    entry_password_check_register = Entry(frame_register, bg="grey",show="*")
    entry_password_check_register.grid(row=2, column=2)
    value_checkpassword = entry_password_check_register.get()


    # Buttons
    button_show = Button(frame_register, text="Annuler", font=("Arial,15"), command=lambda: closing_insertion(window_register))
    button_show.grid(row=1, column=0, pady=5)
    check = Checkbutton(frame_register, text='show password',relief="solid",bd=1, command=lambda: show(entry_password_register,check))
    check.grid(row=1, column=3)
    check = Checkbutton(frame_register, text='show password',relief="solid",bd=1, command=lambda: show(entry_password_register,check))
    check.grid(row=2, column=3)
    # Buttons
    button_add = Button(frame_register, text="Enregistrer", font=("Arial,15"), command=register)
    button_add.grid(row=1, column=10, pady=5,padx=20)
    value_password = hash_password(value_password)

    # main loop
    window_register.mainloop()

def register():
    if checkpw(entry_player_register, entry_password_register, entry_password_check_register):
        database.createuser(entry_player_register.get(), hash_password(entry_password_register.get()))


if __name__ == "__main__":
    register_window()