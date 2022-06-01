from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
from pyperclip import copy
import json


def gen_password():
    password_output.delete(0, END)
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    pass_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pass_nums = [choice(numbers) for _ in range(randint(2, 4))]

    pass_list = password_letters + pass_symbols + pass_nums
    shuffle(pass_list)
    final_pass = "".join(pass_list)
    password_output.insert(0, final_pass)
    copy(final_pass)


def save_pass():
    txt_email = email_txt_input.get()
    txt_site = webpage_txt_input.get()
    txt_pass = password_output.get()

    new_data = {
        txt_site: {
            "email": txt_email,
            "lozinka": txt_pass
        }
    }

    if len(txt_site) == 0 or len(txt_pass) == 0:
        messagebox.showerror(title="Greška", message="Niste ispunili jedno od traženih polja!\nPokušajte ponovo.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except (FileNotFoundError, json.JSONDecodeError):
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            webpage_txt_input.delete(0, END)
            password_output.delete(0, END)


def find_pass():
    try:
        text = webpage_txt_input.get()
        with open("data.json", "r") as data:
            file = json.load(data)
            if text in file:
                old_data = file[text]
                messagebox.showinfo(title="Vaši podaci",
                                    message=f"Sajt: {text}\nemail: {old_data['email']}\nlozinka: {old_data['lozinka']}")
            else:
                messagebox.showerror(title="Greška", message="Nemate lozinku za dati sajt")
    except FileNotFoundError:
        messagebox.showerror(title="Greška", message="Fajl sa lozinkama je prazan")
        with open("data.json", "w") as data_file:
            pass


window = Tk()
window.title("Menadžer lozinke")
window.config(padx=30, pady=30)

LOCK_IMG = PhotoImage(file="logo.png")

picture_canvas = Canvas(height=200, width=200)
picture_canvas.create_image(60, 100, image=LOCK_IMG)
picture_canvas.grid(row=0, column=1)

webpage_label = Label(text="Sajt:", width=20)
webpage_label.grid(row=1, column=0)

webpage_txt_input = Entry(width=33)
webpage_txt_input.focus()
webpage_txt_input.grid(column=1, row=1)

search_button = Button(text="Pretrazi", width=10, command=find_pass)
search_button.grid(row=1, column=2)

email_label = Label(text="Imejl/korisničko ime:", width=20)
email_label.grid(row=2, column=0)

email_txt_input = Entry(width=46)
email_txt_input.insert(0, "example@test.com")
email_txt_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Lozinka:", width=20)
password_label.grid(row=3, column=0)

password_output = Entry(width=33)
password_output.grid(row=3, column=1)

password_button = Button(text="Napravi", width=10, command=gen_password)
password_button.grid(row=3, column=2)

add_button = Button(text="Dodaj", width=39, command=save_pass)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
