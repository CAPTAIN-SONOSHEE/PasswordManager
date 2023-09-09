from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

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

def save():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    new_data = {
         website:{
              "username": username,
              "password": password, 
         }
    }
    
    if len(website) == 0 or len(username) == 0 or len(password) == 0 :
        messagebox.showwarning(title="Missing info", message="Please don't leave any fields empty!")
    else:
            try:
                 with open("data.json", mode="r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError:    
                with open("data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                 with open("data.json", mode="w") as data_file:
                     json.dump(data, data_file, indent=4)    
            finally:
                entry_website.delete(0,'end')
                entry_username.delete(0,'end')
                entry_password.delete(0,'end')     

def find_password():
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="No data", message="No Data File Found")
    else:    
        website = entry_website.get()
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
            if website in data:
                messagebox.showinfo(title=website, message=f"Username: {data[website]['username']}\nPassword: {data[website]['password']}")
            else:
                messagebox.showinfo(title="No details", message=f"No details for {website} exists")

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0,row=1)
label_username = Label(text="Email/Username:")
label_username.grid(column=0,row=2)
label_password = Label(text="Password:")
label_password.grid(column=0,row=3)


entry_website = Entry()
entry_website.grid(column=1,row=1, columnspan=2, sticky="EW")
entry_website.focus()
entry_username = Entry()
entry_username.grid(column=1,row=2, columnspan=2, sticky="EW")
entry_password = Entry()
entry_password.grid(column=1,row=3, sticky="EW")


button_search = Button(text="Search", command=find_password)
button_search.grid(column=2, row=1, sticky="EW")
button_password = Button(text="Generate Password", command=password_generator)
button_password.grid(column=2,row=3, sticky="EW")
button_add = Button(text="Add", width=36, command=save)
button_add.grid(column=1,row=4,columnspan=2, sticky="EW")

window.mainloop()