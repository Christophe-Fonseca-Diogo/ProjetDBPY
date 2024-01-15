# Login
# Made by Christophe
# Version 1
# Date 15.01.2024

from Utilities import *
import database

def login_window(original_window):
    global window_login,check
    from Register import register_window
    # Window parameters
    window_login = tk.Tk()
    window_login.title("Connexion")
    window_login.geometry("1000x300")
    window_login.configure(bg=local_theme.hex_color)
    window_login.grid_columnconfigure((0, 1, 2), minsize=300, weight=1)

    # Title for the results window
    label_title_login = tk.Label(window_login, text="Connexion", font=("Arial", 25), borderwidth=2,
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
    entry_player_login = Entry(frame_login, bg="grey")
    entry_player_login.grid(row=0, column=2)
    entry_password_login = Entry(frame_login, bg="grey",show="*")
    entry_password_login.grid(row=1, column=2)


    # Buttons
    button_show = Button(frame_login, text="S'inscrire", font=("Arial,15"), command=register_window)
    button_show.grid(row=1, column=0,padx=10,pady=5)
    check = Checkbutton(frame_login, text='show password',relief="solid",bd=1, command=lambda: show(entry_password_login, check))
    check.grid(row=1, column=3)
    # Buttons
    button_add = Button(frame_login, text="Se connecter", font=("Arial,15"), command=lambda:
                                            login(entry_player_login.get(), entry_password_login.get(), original_window,
                                                  window_login))
    button_add.grid(row=1, column=10,padx=25)

    # main loop
    window_login.mainloop()


def login(username, password, original_window, window_login):
    from menu import open_window
    result = database.check_login(username, password)
    if result[0]:
        original_window.destroy()
        window_login.destroy()
        open_window(username)



if __name__ == "__main__":
    login_window()