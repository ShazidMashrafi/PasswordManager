from tkinter import *
from tkinter import messagebox
import random
import string

#Screen

screen = Tk()
screen.config(padx = 50 , pady = 50)


#Global Variables

uppers = IntVar()
nums = IntVar()
syms = IntVar()


#----------------------------------------------------Password Generator ----------------------------------------------------------#

def generate():

    password_entry.delete(0, END)

    uppercase = list(string.ascii_uppercase)
    lowercase = list(string.ascii_lowercase)
    numbers = list(string.digits)
    symbols = ['@', '#', '$', '%', '&', '_', '!', '.', '?', '*']

    len = int(length_entry.get())

    if len < 8:
        messagebox.showerror(title = "Password too short", message = "Password must be at least 8 characters.")
    
    else:
        n_uppercase = int(len * .15) if uppers.get() else 0
        n_numbers = int(len * .30) if nums.get() else 0
        n_symbols = int(len * .15) if syms.get() else 0
        n_lowercase = len - (n_uppercase + n_numbers + n_symbols)

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
        messagebox.showerror(title = "Invalid Input", message = "Don't leave any field empty!")
    
    elif special_character(email):
        messagebox.showerror(title = "Invalid username!", message = "No special characters are allowed in username.")
    
    else:
        is_ok = messagebox.askokcancel(title = website, message = f"You have entered: \nEmail: {email}\nPassword: {password}\n"
                                                            f"Are you sure to save?")
        if is_ok:
            with open("Passwords.txt", "a") as f:
                f.write(f"{website} | {email} | {password}\n")

            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)



#--------------------------------------------------- UI Setup ------------------------------------------------------------------#

logo = PhotoImage(file = "Assets//logo.png")
screen.iconphoto(False, logo)
screen.title("Password Manager")

canvas = Canvas(width = 480, height = 320)

photo = PhotoImage(file = "Assets//banner.png")
banner = Label(screen, image = photo)
banner.place(x = 60, y = -30)

canvas.grid(column = 1, row = 0)


#Label

website = Label(text = "Website : ")
website.grid(column = 0, row = 1)

email = Label(text = "Email or Username : ")
email.grid(column = 0, row = 2)

password = Label(text = "Password : ")
password.grid(column = 0, row = 3)

# gen = Label(text = "Generate : ")
# gen.grid(column = 0, row = 4)


#Entries

website_entry = Entry(width = 50)
website_entry.grid(column = 1, row = 1)
website_entry.focus()

email_entry = Entry(width = 50)
email_entry.grid(column = 1, row = 2)

password_entry = Entry(width = 50)
password_entry.grid(column = 1, row = 3)


#Password variables

frame2 = Frame(screen, width = 400, height = 20)
frame2.grid(column = 1, row = 4)

length = Label(frame2, text = "Password length : ")
length.grid(column = 0, row = 4)

length_entry = Entry(frame2, width = 4)
length_entry.grid(column = 1, row = 4)

include = Label(frame2, text = "Include : ")
include.grid(column = 2, row = 4, padx = (20, 2))

upper_box = Checkbutton(frame2, text = "Uppercase", variable = uppers)
upper_box.grid(column = 3, row = 4)

num_box = Checkbutton(frame2, text = "Numbers", variable = nums)
num_box.grid(column = 4, row = 4)

sym_box = Checkbutton(frame2, text = "Symbols", variable = syms)
sym_box.grid(column = 5, row = 4)


#Buttons

generate_button = Button(text = "Generate Password", command = generate)
generate_button.grid(column = 1, row = 5, columnspan = 2, pady = (5, 10))

add_button = Button(text = "Save", width = 20, command = save)
add_button.grid(column = 1, row = 6, columnspan = 3)



screen.mainloop()