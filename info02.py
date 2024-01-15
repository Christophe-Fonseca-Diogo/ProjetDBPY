# Info02
# Made by Christophe
# Version 1
# Date 15.12.2023

from math import pow
from database import *
import tkinter as tk
import random
import time
import database
import datetime
from tkinter import messagebox
#important data (to save)
pseudo='' #pseudo for the user
exercise="INFO02"
nbtrials=0 #number of total trials
nbsuccess=0 #number of successfull trials


# Liaison entre le canvas et le code
unite = ["B", "kB", "MB", "GB", "TB"]
n1 = 0  # valeur à convertir
u1 = unite[0]
n2 = 0  # valeur à convertir
u2 = unite[0]
rapport = 0


def next(event):
    global n1, u1, u2, rapport
    window_info02.configure(bg=hex_color)

    n1 = round(random.random(), 3)
    dec = random.randint(0, 3)
    for i in range(dec):
        n1 *= 10
    n1 = round(n1, 3)
    p1 = random.randint(1, 4)
    u1 = unite[p1]
    p2 = p1
    while p1 == p2:
        p2 = random.randint(0, 4)
    u2 = unite[p2]
    rapport = pow(10, 3 * (p2 - p1))
    label_n1.configure(text=f" {n1} {u1} =")
    label_u2.configure(text=f" {u2} ")
    entry_n2.delete(0, 'end')


# save the game of the player
def save_game(event,username):
    global pseudo
    pseudo = username
    if pseudo == "":
        messagebox.showerror(parent=window_info02, title="Pseudo Invalide", message="Veuillez ajouter un pseudo")
    else:
        # Check if the player exists or add them
        database.get_playername(pseudo, exercise)
        if pseudo:
            database.add_results(start_date, duration_s, nbtrials, nbsuccess, player_name=pseudo, exercise_name=exercise)
            messagebox.showinfo(title="Sauvegarde", message="Sauvegarde Validée")
            window_info02.destroy()


def test(event):
    global n2, nbsuccess, nbtrials
    # Fonction pour tester si la valeur est juste
    n2 = float(entry_n2.get().replace(" ", ""))
    nbtrials+=1
    success = (abs(n1 / n2 / rapport - 1) < 0.01) #tolerance 1%
    if success:
        nbsuccess += 1
        window_info02.configure(bg="green")
    else:
        window_info02.configure(bg="red")
    lbl_result.configure(text=f"Essais réussis : {nbsuccess} / {nbtrials}")
    window_info02.update()
    time.sleep(1) # delai 1s
    next(event=None)


def display_timer():
    global duration_s
    duration = datetime.datetime.now() - start_date  # elapsed time since beginning, in time with decimals
    duration_s = int(duration.total_seconds())  # idem but in seconds (integer)
    # display min:sec (00:13)
    lbl_duration.configure(text="{:02d}".format(int(duration_s / 60)) + ":" + "{:02d}".format(duration_s % 60))
    window_info02.after(1000, display_timer)  # recommencer après 15 ms


def open_window_info_02(window,username):
    global window_info02, lbl_duration, lbl_result, entry_n2, label_u2, label_n1, hex_color, start_date, entry_pseudo
    window_info02 = tk.Toplevel(window)

    # window_info02 = tk.Tk()
    window_info02.title("Conversion d'unités")
    window_info02.geometry("1100x900")
    window_info02.grid_columnconfigure((0,1,2), minsize=150, weight=1)

    # color definition
    rgb_color = (139, 201, 194)
    hex_color = '#%02x%02x%02x' % rgb_color # translation in hexa
    window_info02.configure(bg=hex_color)

    lbl_title = tk.Label(window_info02, text=f"{exercise}", font=("Arial", 15))
    lbl_title.grid(row=0,column=0,columnspan=3, ipady=5, padx=20,pady=20)
    lbl_duration = tk.Label(window_info02, text="0:00", font=("Arial", 15))
    lbl_duration.grid(row=0,column=2, ipady=5, padx=10,pady=10)

    tk.Label(window_info02, text='Pseudo:', font=("Arial", 15)).grid(row=1, column=0, padx=5, pady=5)
    tk.Label = tk.Label(window_info02,text=username, font=("Arial", 15)).grid(row=1, column=1)

    lbl_result = tk.Label(window_info02, text=f"{pseudo}  Essais réussis : 0/0", font=("Arial", 15))
    lbl_result.grid( row=1, column=2,columnspan=3, ipady=5, padx=20,pady=20)

    label_n1 = tk.Label(window_info02, text="n1:",font=("Arial", 15))
    label_n1.grid(row=2,column=0,ipady=5, padx=20,pady=20,sticky='E')

    entry_n2 = tk.Entry(window_info02,font=("Arial", 15))
    entry_n2.grid(row=2,column=1,ipady=5,padx=5, pady=20,sticky='E')

    label_u2 =tk.Label(window_info02, text="u2:",font=("Arial", 15))
    label_u2.grid(row=2,column=2,ipady=5,padx=5,pady=20,sticky='W')

    btn_next =tk.Button(window_info02, text="Suivant", font=("Arial", 15))
    btn_next.grid(row=3,column=0,columnspan=3,ipady=5, padx=5,pady=5)

    btn_finish = tk.Button(window_info02, text="Terminer", font=("Arial", 15))
    btn_finish.grid(row=6, column=0, columnspan=6)

    start_date = datetime.datetime.now()
    display_timer()
    # first call of next_point
    next(event=None)

    # binding actions (entry & buttons)
    entry_n2.bind("<Return>", test)
    btn_next.bind("<Button-1>", next)
    btn_finish.bind("<Button-1>", lambda event: save_game(event=event, username=username))

    # Main loop
    window_info02.mainloop()
