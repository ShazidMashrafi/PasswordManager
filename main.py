from tkinter import *
from tkinter import messagebox
import random

# Creating the main window of our program
root = Tk()


# Global Variables
upper = IntVar()
digit = IntVar()
sym = IntVar()


# ----------------------------------------------------Password Generator ----------------------------------------------------------#

# Function to generate password.
def generate():

    # Delete the previous password entry.
    password_entry.delete(0, END)

    # All uppercase letters in a list.
    uppers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
                    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    # All lowercase letters in a list.
    lowers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # All digits in a list.
    digits = ['0', '1', '2', '3','4', '5', '6', '7', '8', '9']

    # Allowed symbols in a list.
    syms = ['@', '#', '$', '%', '&', '_', '!', '.', '?', '*']

    # Get the desired length of password from length entry box.
    len_str = length_entry.get()

    # If length box is empty show an error saying to input length of password
    if len_str == '':
        messagebox.showerror(title = "Password length undefined",
                             message = "Please enter the length of password.")
    # If entered length is less the 8, pop up an error box saying that password must be at least 8 characters.
    else:
        len = int(len_str)
        if len < 8:
            messagebox.showerror(title = "Password too short",
                                 message = "Password must be at least 8 characters.")

        # If entered length is 8 characters or more then
        else:
            n_upper = 0
            n_digit = 0
            n_sym = 0

            #if "uppercase" is selected allocate 15% of the total length to uppercase letters, else 0.
            if upper.get():
                n_upper = int(len * .15)

            #if "numbers" is selected allocate 30% of the total length to numbers, else 0.
            if digit.get():
                n_digit = int(len * .30) 

            #if "symbols" is selected allocate 15% of the total length to symbols, else 0.
            if sym.get():
                n_sym = int(len * .15) 

            # Allocate the remaining length to lowercase letters.
            n_lower = len - (n_upper + n_digit + n_sym)

            # An empty list to store all the characters of password.
            password_list = []

            # Generate lowercase characters.
            for _ in range(n_lower):
                password_list.append(random.choice(lowers))

            # Generate uppercase characters.
            for _ in range(n_upper):
                password_list.append(random.choice(uppers))

            # Generate symbols.
            for _ in range(n_sym):
                password_list.append(random.choice(syms))

            # Generate numbers.
            for _ in range(n_digit):
                password_list.append(random.choice(digits))

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

# Function to check if there are any special characters in the username or email.
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
        messagebox.showerror(title = "Invalid Input",
                             message = "Don't leave any field empty!")
        
    # Check if there are any special characters in username/email.
    elif special_character(email):
        messagebox.showerror(title = "Invalid Email/Username!",
                             message = "No special characters are allowed in username.")
    
    # If password length is lower than 8, show error saying to enter a longer password
    elif len(password) < 8:
        messagebox.showerror(title = "Password too short",
                             message = "Password must be at least 8 characters.")
    else:

        # Confirmation dialog to save the password or not.
        is_ok = messagebox.askokcancel(title = "Confirm save", message = f"You have entered:\n\n"
                                                                         f"Website: {website}\n"
                                                                         f"Email/Username: {email}\n"
                                                                         f"Password: {password}\n\n"
                                                                         f"Are you sure to save?")
        
        # If user chooses to save
        if is_ok:

            # Declare an empty list
            data = []

            # Open the txt file as read mode
            with open("Passwords.txt", "r") as file:

                # Iterate through lines and split every line by "|" and append to "data".
                for lines in file.readlines():
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
                    if data[i][0] == "Website : " + website and data[i][1] == "Email/Username : " + email:
                        is_yes = messagebox.askyesno(title = "Existing account", message = f"Entry for:\n\n"
                                                                                           f"Website : {website}\n"
                                                                                           f"Email/Username : {email}\n\n"
                                                                                           f"Already exists! Do you want to update the password?\n"
                                                                                           f"Not updating password will create a new entry.")
                        
                        # If match is found set the value of "found" to true
                        found = True
                        
                        # If user wants to update then replace the old password with the new one
                        if is_yes:
                            data[i][2] = "Password : " + password
                            break

                        # If the user doesn't want to update then consider it as a new entry
                        else:
                            data.append(["Website : " + website, "Email/Username : " + email, "Password : " + password])
                            break
                
                # If no match is found add the new entry
                if not found:
                    data.append(["Website : " + website, "Email/Username : " + email, "Password : " + password])
            
            # If data is empty, add the new entry to "data" list
            else:
                data.append(["Website : " + website, "Email/Username : " + email, "Password : " + password])
            
            # Save all the elements of "data" in the txt file
            with open("Passwords.txt", "w") as file:
                for entry in data:
                    file.write(f"{entry[0]} | {entry[1]} | {entry[2]}\n")
           
            # Password saving successful dialog box         
            messagebox.showinfo("Success", "Password has been saved successfully")
        
            # Delete the entries after saving.
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            length_entry.delete(0,END)
        

# -------------------------------------------------------- GUI ------------------------------------------------------------------#

# ------------ Window ----------- #
        
# Make the window size fixed
root.resizable(False, False)

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Initial size of the main window
window_width = 800
window_height = 600

# Calculate center position of the screen
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

# Set the size and position of the window
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

# Create padding on all sides of the window
root.config(padx = 50, pady = 50)

# Selecting a png file for the logo of the GUI.
logo = PhotoImage(file = "Assets//logo.png")
root.iconphoto(True, logo)

# Giving a title to our GUI.
root.title("Password Manager")

# Selecting an image for our main window
photo = PhotoImage(file = "Assets//banner.png")
banner = Label(root, image = photo)
banner.grid(row = 0, column = 0,columnspan = 5, padx = (100, 0))



# --------- Labels ------------ #

# Label of "website" entry box on row 1 and column 0.   
website = Label(text = "Website name: ")
website.grid(row = 1, column = 0)

# Label of "email/username" entry box on row 2 and column 0.
email = Label(text = "Email/Username : ")
email.grid(row = 2, column = 0)

#Label of "Password" entry box on row 3 and column 0.
password = Label(text = "Password : ")
password.grid(row = 3, column = 0)


# ----------- Entry Boxes --------- #

# "website entry box" of width 75 on row 1 and column 1.
website_entry = Entry(width = 75)
website_entry.grid(row = 1, column = 1)
website_entry.focus()

# "email entry box" of width 75 on row 2 and column 1.
email_entry = Entry(width = 75)
email_entry.grid(row = 2, column = 1)

# "password entry box" of width 75 on row 1 and column 1.
password_entry = Entry(width = 75)
password_entry.grid(row = 3, column = 1)


# ----------- Password options ---------- #

# Marking a frame for the options to be in, placing the frame on row 4 and column 1 of the canvas.
frame = Frame(root, width = 400, height = 20)
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

# "Uppercase" check button on row 4 and column 3. This will be the value of "upper" variable.
upper_box = Checkbutton(frame, text = "Uppercase", variable = upper)
upper_box.grid(row = 4, column = 3)

# "Numbers" check button on row 4 and column 4. This will be the value of "digit" variable.
num_box = Checkbutton(frame, text = "Digit", variable = digit)
num_box.grid(row = 4, column = 4)

# "Symbols" check button on row 4 and column 5. This will be the value of "sym" variable.
sym_box = Checkbutton(frame, text = "Symbol", variable = sym)
sym_box.grid(row = 4, column = 5)


# ------------ Buttons -------------- #

# "Password generate" button on row 5 and column 1 with columnspan of 2 and horizontal padding. 
# This button will call "generate" function.
generate_button = Button(text = "Generate Password", command = generate)
generate_button.grid(row = 5, column = 1, columnspan = 2, pady = (5, 10))

# "Save" button on row 6 column 1 with a columnspan of 3. This will call "save" function.
add_button = Button(text = "Save", width = 20, command = save)
add_button.grid(row = 6, column = 1, columnspan = 3)


root.mainloop()

# End of the program