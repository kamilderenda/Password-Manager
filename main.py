from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list.extend(random.choices(letters, k=nr_letters))


    password_list.extend(random.choices(symbols, k=nr_symbols))


    password_list.extend(random.choices(numbers, k=nr_numbers))



    random.shuffle(password_list)

    password = ''.join(password_list)
    Password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_to_file():
    user_password = Password_entry.get()
    user_email = Email_entry.get()
    user_website = Website_entry.get()

    new_data = {
        user_website:{
            "email": user_email,
            "password": user_password,
        }
    }

    if len(user_website) == 0 or len(user_password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave empty gaps.")
    else:
        try:
            with open("data.json", "r") as data_file:
                    data_json = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data,data_file, indent=4)
        else:
            data_json.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data_json, data_file, indent=4)
        finally:
            Website_entry.delete(0, END)
            Password_entry.delete(0, END)


def find_password():
    user_website = Website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data_json = json.load(data_file)

            if user_website in data_json:
                looking_data = data_json[user_website]
                looking_email = looking_data.get("email")
                looking_password = looking_data.get("password")
                messagebox.showinfo(title=user_website, message=f"Email: {looking_email}\nPassword: {looking_password}")
            else:
                messagebox.showinfo(title="Oops", message=f"No data found for {user_website}")

    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="File not found")
    except json.JSONDecodeError:
        messagebox.showinfo(title="Oops", message="Invalid JSON format in data.json")


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img=PhotoImage(file="logo.png")   #musze go przerobic na image w jezyku tkintera
canvas.create_image(100, 100, image = logo_img)
canvas.grid(row=0, column=1)

Website_label = Label(text="Website:")
Website_label.grid(column=0, row=1)
Email_label = Label(text="Email/Username:")
Email_label.grid(column=0, row=2)
Password_label = Label(text="Password:")
Password_label.grid(column=0, row=3)

Website_entry = Entry(width=21)
Website_entry.grid(column=1, row=1)
Website_entry.focus()   #automatyczne ustawienie kursora
Email_entry = Entry(width=42)
Email_entry.grid(column=1, row=2, columnspan=2)
Email_entry.insert(0, "example@outlook.com")  #wprowadzenie domyslne
Password_entry = Entry(width=21)
Password_entry.grid(column=1, row=3)

search_button = Button(text="Search", width=21, command=find_password)
search_button.grid(column=2, row=1)
Generate_button = Button(text="Generate Password", command=random_password, width=21)
Generate_button.grid(column=2, row=3)
Add_button = Button(width=36, text="Add", command=save_to_file)
Add_button.grid(column=1, row=4, columnspan=2)





window.mainloop()
