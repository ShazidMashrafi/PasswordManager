from tkinter import *
from tkinter import messagebox
import random
import string



#----------------------------------------------------Password Generator ----------------------------------------------------------#

def generate():

    uppercase = list(string.ascii_uppercase)
    lowercase = list(string.ascii_lowercase)
    numbers = list(string.digits)
    symbols = ['@', '#', '$', '%', '&', '_', '!', '.', '?', '*']

    n_uppercase = random.randint(4, 5)
    n_lowercase = random.randint(4, 5)
    n_symbols = random.randint(2,4)
    n_numbers = random.randint(2,4)

    password_list = [random.choice(lowercase) for _ in range(n_lowercase)]
    password_list += [random.choice(uppercase) for _ in range(n_uppercase)]
    password_list += [random.choice(symbols) for _ in range(n_symbols)]
    password_list += [random.choice(numbers) for _ in range(n_numbers)]

    random.shuffle(password_list)

    password = ""

    for char in password_list:
        password += char
    
    password_entry.insert(END, password)
    password_entry.clipboard_clear()
    password_entry.clipboard_append(password)



#--------------------------------------------------------Save Password ----------------------------------------------------------#

def special_character(s):
    for c in s:
        if not (c.isalpha() or c.isdigit() or c == '_' or c == '.' or c == '@' or c == '-'):
            return True
    return False


def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title="Invalid Input", message="Don't leave any field empty!")
    
    elif special_character(email):
        messagebox.showerror(title="Invalid username!", message="No special characters are allowed in username.")
    
    else:
        is_ok = messagebox.askokcancel(title = website, message=f"You have entered: \nEmail: {email}\nPassword: {password}\n"
                                                            f"Are you sure to save?")
        if is_ok:
            with open("Passwords.txt", "a") as f:
                f.write(f"{website} | {email} | {password}\n")

            website_entry.delete(0,END)
            password_entry.delete(0,END)



#--------------------------------------------------- UI Setup ------------------------------------------------------------------#

screen = Tk()
screen.config(padx = 50 , pady = 50)
logo = PhotoImage(file = "Assets//logo.png")
screen.iconphoto(False, logo)
screen.title("Password Manager")

canvas = Canvas(width = 480, height = 320)

frame = Frame(screen, width=480, height = 320)
frame.place(x=30, y=-30)

photo = PhotoImage(file ="Assets//banner.png")
banner = Label(frame, image = photo)
banner.place(x=0, y=0)

canvas.grid(column = 1, row = 0)


#Label

website = Label(text = "Website: ")
website.grid(column = 0, row = 1)

email = Label(text = "Email/Username: ")
email.grid(column = 0, row = 2)

password = Label(text = "Password: ")
password.grid(column = 0, row = 3)


#Entries

website_entry = Entry(width = 50)
website_entry.grid(column = 1, row = 1, columnspan = 2)
website_entry.focus()

email_entry = Entry(width = 50)
email_entry.grid(column = 1, row = 2, columnspan = 2)

password_entry = Entry(width = 50)
password_entry.grid(column = 1, row = 3, columnspan = 2)


#Buttons

generate_button = Button(text="Generate Password", command = generate)
generate_button.grid(column = 1, row = 4)

add_button = Button(text = "Add", width = 20, command = save)
add_button.grid(column = 1, row = 5, columnspan = 2) 



screen.mainloop()