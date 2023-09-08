from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():

    if len(entry_password.get()) > 0:
        entry_password.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))] + [choice(symbols) for _ in range(randint(2, 4))] + [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()
    
    if len(website) == 0 or len(username) == 0 or len(password) == 0 :
        messagebox.showwarning(title="Missing info", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail/Username: {username}\nPassword: {password}\nIs it ok to save?")

        if is_ok:
            with open("data.txt", mode="a") as data:
                data.write(f"{website} | {username} | {password}\n")

            entry_website.delete(0,'end')
            entry_username.delete(0,'end')
            entry_password.delete(0,'end')     

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0,row=1)
entry_website = Entry()
entry_website.grid(column=1,row=1, columnspan=2, sticky="EW")
entry_website.focus()

label_username = Label(text="Email/Username:")
label_username.grid(column=0,row=2)
entry_username = Entry()
entry_username.grid(column=1,row=2, columnspan=2, sticky="EW")

label_password = Label(text="Password:")
label_password.grid(column=0,row=3)
entry_password = Entry()
entry_password.grid(column=1,row=3, sticky="EW")
button_password = Button(text="Generate Password", command=password_generator)
button_password.grid(column=2,row=3, sticky="EW")

button_add = Button(text="Add", width=36, command=save)
button_add.grid(column=1,row=4,columnspan=2, sticky="EW")


window.mainloop()