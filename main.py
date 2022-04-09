from tkinter import *
from tkinter import messagebox
import random
import pyperclip

#----------------------------- GLOBAL VARS ----------------------------------------#
FONT = ("Ubuntu", 10)
WHITE = "#FFFFFF"
GRAY= "#f9f9f9"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pword_input.delete(0, 'end')

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    
    password = "".join(password_list)

    pword_input.insert(0, password)

    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = web_input.get()
    uname = uname_input.get()
    password = pword_input.get()

    if website == "" or uname == "" or password == "":
        messagebox.showerror(title="Missing Fields Required!", message="You need to fill all required fields to save to file!")
    else:

        is_ok = messagebox.askokcancel(title= website, message=f"These are the details entered: \nEmail: {uname}\nPassword: {password}\nIs it ok to save?")

        if is_ok:

            with open('pword.txt', 'a') as file:
                file.write(f"{website} | {uname} | {password}\n")
            web_input.delete(0, 'end')
            uname_input.delete(0, 'end')
            pword_input.delete(0, 'end')
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=500, height=500)
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height = 200, bg=WHITE, highlightthickness=0)
logo_img = PhotoImage(file= 'logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row= 0, column= 1)

#Labels
website = Label(text="Website:", bg=WHITE, font=FONT)
website.grid(row= 1, column= 0)

uname = Label(text= "Email/Username:", bg=WHITE, font=FONT)
uname.grid(row= 2, column= 0)

pword = Label(text="Password:", bg=WHITE, font=FONT)
pword.grid(row= 3, column= 0)

#Buttons
gen_pword = Button(text="Generate Password", width= 14, bg=GRAY,  font=FONT, command= generate_password)
gen_pword.grid( row=3, column=2, columnspan=2 )

add_pword = Button(text="Add", width=36, bg=GRAY, font=FONT, command= add_password)
add_pword.grid(row=4, column= 1, columnspan= 2)

#Input
web_input = Entry(width=35, bg= WHITE)
web_input.grid(row= 1, column= 1, columnspan= 2)
web_input.focus()

uname_input = Entry(width= 35, bg= WHITE)
uname_input.grid(row= 2, column= 1, columnspan= 2)

pword_input = Entry(width= 21, bg= WHITE)
pword_input.grid(row= 3, column= 1)




window.mainloop()