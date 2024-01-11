from tkinter import *
from tkinter import messagebox
import random

# Main screen of GUI
screen = Tk()
screen.config(padx = 50, pady = 50)


# Global Variables
uppers = IntVar()
nums = IntVar()
syms = IntVar()


# ----------------------------------------------------Password Generator ----------------------------------------------------------#

# Function to generate password.
def generate():

    # Delete the previous password entry.
    password_entry.delete(0, END)

    # All uppercase letters in a list.
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
                    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    # All lowercase letters in a list.
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # All digits in a list.
    numbers = ['0', '1', '2', '3','4', '5', '6', '7', '8', '9']

    # Allowed symbols in a list.
    symbols = ['@', '#', '$', '%', '&', '_', '!', '.', '?', '*']

    # Get the desired length of password from length entry box.
    len_str= length_entry.get()

    if len_str == '':
        messagebox.showerror(title="Password length undefined",
                             message="Please enter the length of password.")
    # If entered length is less the 8, pop up an error box saying that password must be at least 8 characters.
    else:
        len = int(len_str)
        if len < 8:
            messagebox.showerror(title="Password too short",
                             message="Password must be at least 8 characters.")

        # If entered length is 8 characters or more then
        else:

            #if "uppercase" is selected allocate 15% of the total length to uppercase letters, else 0.
            n_uppercase = int(len * .15) if uppers.get() else 0

            #if "numbers" is selected allocate 30% of the total length to numbers, else 0.
            n_numbers = int(len * .30) if nums.get() else 0

            #if "symbols" is selected allocate 15% of the total length to symbols, else 0.
            n_symbols = int(len * .15) if syms.get() else 0

            # Allocate the remaining length to lowercase letters.
            n_lowercase = len - (n_uppercase + n_numbers + n_symbols)

            # An empty list to store all the characters of password.
            password_list = []

            # Generate lowercase characters.
            for _ in range(n_lowercase):
                password_list.append(random.choice(lowercase))

            # Generate uppercase characters.
            for _ in range(n_uppercase):
                password_list.append(random.choice(uppercase))

            # Generate symbols.
            for _ in range(n_symbols):
                password_list.append(random.choice(symbols))

            # Generate numbers.
            for _ in range(n_numbers):
                password_list.append(random.choice(numbers))

            # Shuffle the password list to make it random.
            random.shuffle(password_list)

            # An empty string for the final generated password.
            password = ""

            # store the characters from password list to password string.
            for char in password_list:
                password += char
            
            # Show the generated password in the password box.
            password_entry.insert(END, password)


# --------------------------------------------------------Save Password ----------------------------------------------------------#

# A function to check if there are any special characters in the username or email.
def special_character(s):

    for c in s:
        if not (c.isalpha() or c.isdigit() or c == '_' or c == '.' or c == '@' or c == '-'):
            # If there are no special character then the username or email can be used.
            return True

    # If there are any special characters, then the username or email can't be used. 
    return False

# Function to save the entries in a txt file.
def save():

    # Get the entries from GUI and save them in variables
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Check if any field in GUI is empty, if yes then pop up an error message.
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title="Invalid Input",
                             message="Don't leave any field empty!")

    # Check if there are any special characters in username/email.
    elif special_character(email):
        messagebox.showerror(title="Invalid username!",
                             message="No special characters are allowed in username.")

    else:

        # Confirmation dialog to save the password or not.
        is_ok = messagebox.askokcancel(title=website, message=f"You have entered: \nEmail: {email}\nPassword: {password}\n"
                                       f"Are you sure to save?")
        
        # If user chooses to save
        if is_ok:

            # Declare an empty list
            data = []

            # Open the txt file as read mode
            with open("Passwords.txt", "r") as f:

                # Iterate through lines and split every line by "|" and append to "data".
                for lines in f.readlines():
                    stripped_line = lines.strip()
                    split_line = stripped_line.split(' | ')
                    data.append(split_line)
            
            # If "data" is not empty 
            if data:
                # Declaring a variable as false initially
                found = False

                # Iterate through every elements in "data"
                for i in range(len(data)):
                    
                    # If the new entry matches an existing one ask the user to update the password or not
                    if data[i][0] == "Website : " + website and data[i][1] == "Username/Email : " + email:
                        is_yes = messagebox.askyesno(title=website, message=f'"{email}" for "{website}" already exists!\n'
                                       f'Do you want to update the password?')
                        
                        # If match is found set the value of "found" to true
                        found = True
                        
                        # If user wants to update then replace the old password with the new one
                        if is_yes:
                            data[i][2] = "Password : " + password
                            break

                        # If the user doesn't want to update then consider it as a new entry
                        else:
                            data.append(["Website : " + website, "Username/Email : " + email, "Password : " + password])
                            break
                
                # If no match is found add the new entry
                if not found:
                    data.append(["Website : " + website, "Username/Email : " + email, "Password : " + password])
            
            # If data is empty, add the new entry to "data" list
            else:
                data.append(["Website : " + website, "Username/Email : " + email, "Password : " + password])
            
            # Save all the elements of "data" in the txt file
            with open("Passwords.txt", "w") as f:
                for entry in data:
                    f.write(f"{entry[0]} | {entry[1]} | {entry[2]}\n")

        # Delete the entries after saving.
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)
        length_entry.delete(0,END)
        

# -------------------------------------------------------- GUI ------------------------------------------------------------------#

# Selecting a png file for the logo of the GUI.
logo = PhotoImage(file = "Assets//logo.png")
screen.iconphoto(False, logo)

# Giving a title to our GUI.
screen.title("Password Manager")

# Dimension of our GUI window.
canvas = Canvas(width = 480, height = 320)

# Selecting an png file for the main image in our GUI.
photo = PhotoImage(file = "Assets//banner.png")
banner = Label(screen, image = photo)
banner.place(x = 60, y = -30)

# Placing the image on row 0 and column 1
canvas.grid(row = 0, column = 1)


# Labels for out entry boxes inside GUI

# Label of "website" entry box on row 1 and column 0.   
website = Label(text = "Website name: ")
website.grid(row = 1, column = 0)

# Label of "email/username" entry box on row 2 and column 0.
email = Label(text = "Email address or Username : ")
email.grid(row = 2, column = 0)

#Label of "Password" entry box on row 3 and column 0.
password = Label(text = "Password : ")
password.grid(row = 3, column = 0)


# Entry Boxes

# "website entry box" of width 75 on row 1 and column 1.
website_entry = Entry(width = 75)
website_entry.grid(row = 1,column = 1)
website_entry.focus()

# "email entry box" of width 75 on row 2 and column 1.
email_entry = Entry(width = 75)
email_entry.grid(row = 2, column = 1)

# "password entry box" of width 75 on row 1 and column 1.
password_entry = Entry(width = 75)
password_entry.grid(row = 3, column = 1)


# Password options

# Marking a frame for the options to be in, placing the frame on row 4 and column 1 of the canvas.
frame = Frame(screen, width = 400, height = 20)
frame.grid(row = 4, column = 1)

# Label of "length entry" box on row 4 and column 0 of the frame.
length = Label(frame, text = "Password length : ")
length.grid(row = 4, column = 0)

# "length"  entry box of width 5 on row 4 and column 1 of the frame.
length_entry = Entry(frame, width = 5)
length_entry.grid(row = 4, column = 1)

# "Include" text, placing on row 4 and column 2 with padding on left and right.
include = Label(frame, text = "Include : ")
include.grid(row = 4, column = 2, padx = (20, 2))

# "Uppercase" check button on row 4 and column 3. This will be the value of "uppers" variable.
upper_box = Checkbutton(frame, text = "Uppercase", variable = uppers)
upper_box.grid(row = 4, column = 3)

# "Numbers" check button on row 4 and column 4. This will be the value of "nums" variable.
num_box = Checkbutton(frame, text = "Numbers", variable = nums)
num_box.grid(row = 4, column = 4)

# "Symbols" check button on row 4 and column 5. This will be the value of "syms" variable.
sym_box = Checkbutton(frame, text = "Symbols", variable = syms)
sym_box.grid(row = 4, column = 5)


# Buttons

# "Password generate" button on row 5 and column 1 with columnspan of 2 and horizontal padding. 
# This button will call "generate" function.
generate_button = Button(text = "Generate Password", command = generate)
generate_button.grid(row = 5, column = 1, columnspan = 2, pady = (5, 10))

# "Save" button on row 6 column 1 with a columnspan of 3. This will call "save" function.
add_button = Button(text = "Save", width = 20, command = save)
add_button.grid(row = 6, column = 1, columnspan = 3)


screen.mainloop()

# End of the program