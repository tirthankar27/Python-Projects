from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import json
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_my_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    if password_entry.get()!="":
        password_entry.delete(0,END)

    password_letters=[choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list=password_letters + password_symbols + password_numbers
    shuffle(password_list)
    my_password="".join(password_list)
    password_entry.insert(END,my_password)
    pyperclip.copy(my_password)

# ---------------------------- SEARCH ------------------------------- #

def search_details():
    website_val=website_entry.get()
    try:
        with open("my_passwords.json", mode='r') as data_file:
            data=json.load(data_file)
    except (FileNotFoundError,json.decoder.JSONDecodeError):
        messagebox.showerror(title=f"Details not found for {website_val}",
                                message="No details found! Please check the Webstie")
    else:
        if website_val in data:
            password_val=data[website_val]['password']
            email=data[website_val]['email']
            messagebox.showinfo(title=f"Details found for {website_val}",message=f"Email: {email}\nPassword: {password_val}")
        else:
            messagebox.showerror(title=f"Details not found for {website_val}",
                                message="No details found! Please check the Webstie")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def insert_entries():
    if website_entry.get()=="" or user_entry.get()=="" or password_entry.get()=="":
        messagebox.showerror(title="Error!",message="One or more field is empty")
        return
    is_ok=messagebox.askyesno(title="Proceed?",message="Do you want to save?")
    if is_ok:
        website_val=website_entry.get()
        email=user_entry.get()
        password_val=password_entry.get()
        new_data={
            website_val:{
                "email":email,
                "password":password_val
            }
        }
        with open("my_passwords.json",mode='r') as data_file:
            try:
                data=json.load(data_file)
            except FileNotFoundError:
                data=new_data
            else:
                data.update(new_data)
        with open("my_passwords.json", mode='w') as data_file:
            json.dump(data,data_file,indent=4)
        messagebox.showinfo(title="Success!",
                            message=f"Your details with:\nWebsite: {website_val}\nEmail: {email}\nPassword: {password_val}\n got saved!")
        website_entry.delete(0,END)
        user_entry.delete(0,END)
        password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("My password manager")
window.config(padx=50,pady=50)
logo=PhotoImage(file="logo.png")

canvas=Canvas(width=200,height=200)
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)

website=Label(text="Website:")
website.grid(row=1,column=0)
website_entry=Entry(width=34)
website_entry.focus()
website_entry.grid(row=1,column=1)

mail_username=Label(text="Email/Username:")
mail_username.grid(row=2,column=0)
user_entry=Entry(width=52)
user_entry.grid(row=2,column=1,columnspan=2)

password=Label(text="Password:")
password.grid(row=3,column=0)
password_entry=Entry(width=34)
password_entry.grid(row=3,column=1)

search_button=Button(text="Search",width=14,command=search_details)
search_button.grid(row=1,column=2)

generate_password=Button(text="Generate Password",width=14,command=generate_my_password)
generate_password.grid(row=3,column=2)

add=Button(text="Add",width=44,command=insert_entries)
add.grid(row=4,column=1,columnspan=2)


window.mainloop()
