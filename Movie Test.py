from tkinter import *
import tkinter as tk
import random
import datetime as dt
import random
 
# These two lists will be used for creating a random booked seat
letter_list = ["A", "B", "C", "D", "E", "F"]
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
# using random.choice() to get a random letter and number from the tw lists
random_let = random.choice(letter_list)
random_num = random.choice(number_list)
 
# Create a seat that is already booked by joining the two randomly selected letter/number
booked_seat = (str(random_let)+str(random_num))

# Tracks users current date on device
date = dt.datetime.now()

# Creates a window and customises it
window = Tk()
window.geometry('510x590')
window.title("Movie Seat Booking Program")
window.resizable(False, False)

# Brings a frame to the front if called
def raise_frame(frame):
    frame.tkraise()

# Creates frames and customises it
session = Frame(window, bg="plum", width=510, height=590, padx=10, pady=10)
booking = Frame(window, bg="plum", width=510, height=590, padx=10, pady=10)
ticketing = Frame(window, bg="plum", width=510, height=590, padx=10, pady=10)
confirmation = Frame(window, bg="plum", width=510, height=590, padx=10, pady=10)

# Places frames on a grid
for frame in (session, booking, ticketing, confirmation):
    frame.grid(row=0, column=0, sticky='news')

# Creates a heading for the program 
def program_heading(location):
    Label(location, text="Movie Seat Booking Program", font=("Arial", "16", "bold"), padx=10, pady=10, bg="dark orchid").place(x=0, y=0, height=50, width=420)

# Places the heading created for the program onto all the frames
program_heading(session)
program_heading(booking)
program_heading(ticketing)
program_heading(confirmation)

# Label to display the current date on the users device
Label(session, text="SESSIONS TODAY: " f"{date:%A, %B %d, %Y}", font=("Arial", "16", "bold"), padx=13, pady=10, width=35, bg="dark orchid", borderwidth=5).place(x=0, y=60)

# Creates a class for creating labels for the different movie types
class movie_types:
    def __init__(self, location, text, bg, x, y):
        self.location = location
        self.text = text
        self.bg = bg
        self.x = x
        self.y = y
        self.mheading = tk.Label(self.location, text = self.text, bg = self.bg, 
                             padx=50, pady=50, font=("Arial", "16", "bold"), relief="groove", borderwidth=3) 
        self.mheading.place(x = self.x, y=self.y)

# Uses the movie_types class to create three movie labels
position_y=-20
for movie in range(1, 4):
    position_y = position_y+150
    movie_num = str("Movie ") +str(movie)
    movie_types(session, movie_num,"dark orchid",0,position_y)

# Creates a class for making labels for the different movie informations
class movie_information:
    def __init__(self, location, text, bg, x, y):
        self.location = location
        self.text = text
        self.bg = bg
        self.x = x
        self.y = y
        self.mheading = tk.Label(self.location, text = self.text, bg = self.bg, 
                             padx=105, pady=30, font=("Arial", "16", "bold"), relief="groove", borderwidth=3) 
        self.mheading.place(x = self.x, y=self.y)

# Uses the movie_information class to create three movie information labels
position_y = -20
for information in range(3):
    position_y = position_y+150
    movie_information(session, "Information","dark orchid",195,position_y)

# Creates a class for making buttons for the different sessions and their respective movies
class movie_choice:
    def __init__(self, location, text, bg, x, y, value):
        self.location = location
        self.text = text
        self.bg = bg
        self.x = x
        self.y = y
        self.mbuttons = tk.Button(self.location, text = self.text, bg = self.bg, 
                             padx=0, pady=1, font=("Arial", "13", "bold"), relief="groove", borderwidth=3, command=lambda:(raise_frame(booking),on_click(text, value)))
        self.mbuttons.place(x = self.x, y=self.y)

# Uses the movie_choice class in a range to create nine different buttons (three session buttons for each of the three movies)
position_y = 75
movie_number = 0
for movie in range(1, 4):
    position_x = 95
    position_y = position_y+150
    movie_number = movie_number+1
    for session_number in range(1, 4):
        position_x=position_x+100
        session_num = str(session_number)+str(":00PM")
        movie_num = str("Movie " + str(movie_number))
        movie_choice(session, session_num, "darkmagenta", position_x, position_y, movie_num)
        movie_number = int(movie_number)
        movie_number = int(session_number)

# When movie_choice class buttons are clicked, labels are made according to button clicked (text, value)
def on_click(value, text):
    tk.Label(booking, text=text, font='Helvetica 10', bg="red").place(x=0, y=60, height=20, width=200)
    tk.Label(booking, text=value, font='Helvetica 10', bg="red").place(x=220, y=60, height=20, width=200)
    tk.Label(ticketing, text=text, font='Helvetica 10', bg="red").place(x=0, y=60, height=20, width=200)
    tk.Label(ticketing, text=value, font='Helvetica 10', bg="red").place(x=220, y=60, height=20, width=200)
    tk.Label(confirmation, text=text, font='Helvetica 10', bg="red").place(x=0, y=60, height=20, width=200)
    tk.Label(confirmation, text=value, font='Helvetica 10', bg="red").place(x=220, y=60, height=20, width=200)

# Creates a class for making buttons for the movie seats
class seats:
    def __init__(self, location, text, bg, x, y):
        self.location = location
        self.text = text
        self.bg = bg
        self.x = x
        self.y = y
        self.seats = tk.Button(self.location, text = self.text, bg = self.bg, 
                             padx=3, pady=3, font=("Arial", "7", "bold"), relief="groove", borderwidth=3, command=lambda:(raise_frame(booking),seat_select(self, text)))
        self.seats.place(x = self.x, y=self.y)

# Uses the seats class to create buttons for sixty named seats
position_x = 0
position_y = 95
seats_list = []
for row in range(ord("A"), ord("F") + 1):
    position_y = 95
    position_x = position_x +45
    for column in range(1, 11):
        if random_let == chr(row) and random_num == (column):
            position_y=position_y+45
            seats_list.append(seats(booking, chr(row)+str(column), "red", position_x, position_y))
        elif column == 10:
            position_y=position_y+45
            seats_list.append(seats(booking, chr(row)+str(column), "yellow", position_x, position_y))
        else:
            position_y=position_y+45
            seats_list.append(seats(booking, chr(row)+str(column), "grey", position_x, position_y))

# This list stores user selected seats based on what button created from the seat class they click
selected_seats = []
# Label allows user to know that their selected seats are what is being displayed on the screen
Label(booking, padx=20, bg="purple", text="Selected Seats:").place(x=0, y=100)
# Creates a definition that is called when a seat class button is clicked
def seat_select(self, text):
    # Appends seat choice to the selected_seats list and turns button clicked blue 
    # Appends only if the list has less than 10 items, and seat not already inside the list
    if booked_seat in text:
        print("Seat is already booked!")
    elif text not in selected_seats and len(selected_seats) < 10:
        self.seats.configure(bg="green")
        selected_seats.append(text)
        selected_seats.sort()
        # Displays current selected_seats list in a label
        display_seats = Label(booking, text=selected_seats, padx=5, pady=8, width=22, bg="red", borderwidth=5).place(x=135, y=90)
    # Removes seat choice from the selected_seats list and turns button clicked green
    # Removes only if the seat choice is already inside the list
    elif text in selected_seats and "10" not in text:
        self.seats.configure(bg="grey")
        selected_seats.remove(text)
        # Displays current selected_seats list in a label
        display_seats = Label(booking, text=selected_seats, padx=5, pady=8, width=22, bg="red", borderwidth=5).place(x=135, y=90)    
    elif text in selected_seats and "10" in text:
        self.seats.configure(bg="yellow")
        selected_seats.remove(text)
        # Displays current selected_seats list in a label
        display_seats = Label(booking, text=selected_seats, padx=5, pady=8, width=22, bg="red", borderwidth=5).place(x=135, y=90)
    # Removes seat choice from the selected_seats list and turns button clicked green
    # If the other conditions do not apply, a definition for a help menu will be called
    else:
        help() 

# A definition for a help window for their seat booking
def help():
    top= Toplevel(window)
    top.geometry("720x250")
    top.title("Help Menu")
    Label(top, text= "Select and deselect seats by clicking on the seat buttons.\n\nSelected seats appear near the top of the screen.\n\nMaximum of 10 seats per booking.\n\nIf you are unable to book a seat, it means that the seat is already booked (see key to the right).\n\nOnce you are done selecting seats, click the orange confirm button.\n\nIf you are unable to click confirm, make sure you have selected at least one seat.", font=('Arial 12 bold')).place(x=5,y=120,anchor="w")
    top.grab_set()

# A button for the user to press to manually show the help window when required
help_button = Button(booking, text="Help/Info", command=lambda:(help())).place(x=430, y=55)

# A label for the key about what the colour of the seat buttons mean
key_label = Label(booking, padx=20, bg="purple", text="Key for Seats:").place(x=355, y=100)

# A button for confirming the user seats selected
confirm_seat = Button(booking, bg="orange", text='Confirm Seats', command=lambda:(check_tickets(selected_seats), ticket_number(selected_seats))).place(x=380, y=380)

# This definition checks whether or not the user has selected at least one seat, the next frame will not be raised if there is no seats selected
def check_tickets(selected_seats):
    if len(selected_seats) == 0:
        help()
    else:
        raise_frame(ticketing)

# This class is for creating the key labels themselves with the different colourings
class create_key:
    def __init__(self, location, bg, x, y):
        self.location = location
        self.bg = bg
        self.x = x
        self.y = y
        self.key = tk.Label(self.location, bg = self.bg, 
                            height=2, width=4, relief="groove", borderwidth=3) 
        self.key.place(x = self.x, y=self.y)

# These are the labels themselves created using the create_key label
available = create_key(booking, "grey", 325, 140)
booked = create_key(booking, "red", 325, 185)
clicked = create_key(booking, "green", 325, 230)
disability = create_key(booking, "yellow", 325, 275)

# This class is for creating the named labels of the keys
class create_key_name:
    def __init__(self, location, text, x, y):
        self.location = location
        self.text = text
        self.x = x
        self.y = y
        self.key_name = tk.Label(self.location, text = self.text,
                            height=2, width=17, relief="groove", borderwidth=3) 
        self.key_name.place(x = self.x, y=self.y)

# Using the create_key_labels to create four labels which associate a key colour with meaning
available_text = create_key_name(booking, "   =   Available Seat", 370, 140)
booked_text = create_key_name(booking, "   =    Booked Seat", 370, 185)
clicked_text = create_key_name(booking, "   =   Selected Seat", 370, 230)
disability_text = create_key_name(booking, "   =  Disability Seat", 370, 275)

# This class will be used for creating ticket labels that show the user how many seats they selected
class create_ticket_number:
    def __init__(self, location, bg, x, y):
        self.location = location
        self.bg = bg
        self.x = x
        self.y = y
        self.ticket_number = tk.Label(self.location, bg = self.bg, 
                             height=2, width=4, relief="groove", borderwidth=3) 
        self.ticket_number.place(x = self.x, y = self.y)

# This definition is for checking the amount of seats selected, and making a corresponding amount of labels to show this
ticket_list = {}
def ticket_number(selected_seats):
    position_x=120
    for i in range(len(selected_seats)):
        position_x = position_x + 32
        ticket_list[(i)] = create_ticket_number(ticketing, "green", position_x, 120)

# This label lets the user know what the create_ticket_number class is displaying 
to_book = Label(ticketing, text="Tickets left to book: ").place(x=38, y=130)

# Turns the user input into a string
student_var=tk.StringVar()
# This is an entry box for the user to input the amount of student tickets they want to book
student_ticket = Entry(ticketing, textvariable = student_var, width="10").place(x=250, y=230)

# Turns the user input into a string
adult_var=tk.StringVar()
# This is an entry box for the user to input the amount of adult tickets they want to book
adult_ticket = Entry(ticketing, textvariable = adult_var, width="10").place(x=250, y=255)

# Turns the user input into a string
senior_var=tk.StringVar()
# This is an entry box for the user to input the amount of senior tickets they want to book
senior_ticket = Entry(ticketing, textvariable = senior_var, width="10").place(x=250, y=280)

# This definition is used to gather the user input from the entry boxes used and then create a summary based on the input
def submit_check():
    student=student_var.get()
    adult=adult_var.get()
    senior=senior_var.get()
    if student.isnumeric():
        student = int(student)
    else:
        student_var.set('')
        student = 0
    if adult.isnumeric():
        adult = int(adult)
    else:
        adult_var.set('')
        adult= 0
    if senior.isnumeric():
        senior = int(senior)
    else:
        senior_var.set('')
        senior = 0

    try:
        student = int(student)
        adult = int(adult)
        senior = int(senior)
    except:
        print("An exception occurred")
    
    amount_of_tickets = student + adult + senior
    if amount_of_tickets != len((selected_seats)):
        student_var.set('')
        adult_var.set('')
        senior_var.set('')
        ticketing_help()
    else:
        student_price = student*12
        student_pricing = str(student) +"x " +"Student Ticket(s) = $" + str(student_price)
        Label(ticketing, text=student_pricing, bg="yellow", width="30", font= ('Century 15 bold')).place(x=30, y=375)
        Label(confirmation, text=student_pricing, bg="yellow", width="30", font= ('Century 15 bold')).place(x=30, y=375)

        adult_price =adult*18
        adult_pricing = str(adult) +"x " +"Adult Ticket(s) = $" + str(adult_price)
        Label(ticketing, text=adult_pricing, bg="yellow", width="30", font= ('Century 15 bold')).place(x=30, y=400)
        Label(confirmation, text=adult_pricing, bg="yellow", width="30", font= ('Century 15 bold')).place(x=30, y=400)

        senior_price = senior*14
        senior_pricing = str(senior) +"x " +"Senior Ticket(s) = $" + str(senior_price)
        Label(ticketing, text=senior_pricing, bg="yellow", width="30", font= ('Century 15 bold')).place(x=30, y=425)
        texty = Label(confirmation, text=senior_pricing, bg="yellow", width="30", font= ('Century 15 bold')).place(x=30, y=425)

        total = int(student_price) + int(adult_price) + int(senior_price)
        total_price = "Total cost = $" + str(total)
        Label(ticketing, text=total_price, bg="yellow", width="30", font= ('Century 15 bold')).place(x=30, y=450)
        Label(confirmation, text=total_price, bg="yellow", width="30", font= ('Century 15 bold')).place(x=30, y=450)

        order_summary = Label(ticketing, bg="yellow", width="30", text="Order Summary:", font= ('Century 15 bold')).place(x=30, y=340)
        order_summary = Label(confirmation, bg="yellow", width="30", text="Order Summary:", font= ('Century 15 bold')).place(x=30, y=340)
        Button(ticketing, text='Confirm Order', fg='White', bg= 'dark green',height = 1, width = 10, command=lambda:raise_frame(confirmation)).place(x=205, y=500)
        receit = open("receit.txt", "w")
        for i in range(10):
            receit.write("\n")
        receit.close()
        receit = open("receit.txt", "r")
        list_of_lines = receit.readlines()
        list_of_lines[6] = student_pricing+"\n"
        list_of_lines[7] = adult_pricing+"\n"
        list_of_lines[8] = senior_pricing+"\n\n"
        list_of_lines[9] = total_price+"\n"
        receit = open("receit.txt", "w")
        receit.writelines(list_of_lines)
        receit.close()

# This button is used to submit when the user has finished inputting the amount of tickets they want for each ticket type
submit = Button(ticketing, text='Submit', fg='White', bg= 'dark green',height = 1, width = 12,command= submit_check).place(x=330, y=275)

# This is a help menu that pops up when clicked or as an error message for the users ticket booking
def ticketing_help():
    ticket_help= Toplevel(window)
    ticket_help.geometry("420x40")
    ticket_help.title("Ticketing Help")
    Label(ticket_help, text= "Invalid reponse or incorrect number of tickets booked!", font=('Arial 12 bold')).place(x=5,y=20, anchor="w")
    ticket_help.grab_set()

# This class will be used to associate ticket types with prices in a label for the user
class create_ticket_type:
    def __init__(self, location, bg, text, x, y, padx):
        self.location = location
        self.bg = bg
        self.text = text
        self.x = x
        self.y = y
        self.padx = padx
        self.ticket_type = tk.Label(self.location, bg = self.bg, text = self.text, padx = self.padx
                            ) 
        self.ticket_type.place(x = self.x, y=self.y)

# These are labels associated ticket types for the prices using the create_ticket_type class
student_ticket_label = create_ticket_type(ticketing, "orange", "Student Ticket Price = $12", 100, 230, 0)
adult_ticket_label = create_ticket_type(ticketing, "yellow", "Adult Ticket Price     = $18", 100, 255, 0)
senior_ticket_label = create_ticket_type(ticketing, "green", "Senior Ticket Price    = $14", 100, 280, 0)
ticket_chooser_label = create_ticket_type(ticketing, "green", "Choose your ticket(s)", 100, 200, 100)

# This label tells the user that all the boxes below are input boxes for user information
input_information = Label(confirmation, text="Please enter in user details in the boxes below: ").place(x=100, y=90)

# Turns the user input into a string
name_var=tk.StringVar()
# This is an entry box for the user to input their name
name_entry = Entry(confirmation, textvariable = name_var, width="29").place(x=175, y=125)
# Labels the entry box for name input
name_label = Label(confirmation, text="Enter name: ").place(x=100, y=125)

# Turns the user input into a string
email_var=tk.StringVar()
# This is an entry box for the user to input their email address
email_entry = Entry(confirmation, textvariable = email_var, width="22").place(x=217, y=150)
# Labels the entry box for email input
email_label = Label(confirmation, text="Enter email address: ").place(x=100, y=150)

# Turns the user input into a string
card_var=tk.StringVar()
# This is an entry box for the user to input their credit card number
card_entry = Entry(confirmation, textvariable = card_var, width="30").place(x=168, y=175)
# Labels the entry box for credit card input
card_label = Label(confirmation, text="Enter card: ").place(x=100, y=175)

# Turns the user input into a string
month_var=tk.StringVar()
# This is an entry box for the user to input the expiry month of their credit card
month_entry = Entry(confirmation, textvariable = month_var, width="3").place(x=285, y=200)
# Labels the entry box for the expiry date of the users credit card
expiry_label = Label(confirmation, text="Enter card expiry date (MM/DD): ").place(x=100, y=200)

# Turns the user input into a string
year_var=tk.StringVar()
# This is an entry box for the user to input the expiry year of their credit card
year_entry = Entry(confirmation, textvariable = year_var, width="3").place(x=330, y=200)

# Labels inbetween the entry boxes for credit card expiry month and year
slash_label = Label(confirmation, text=" / ").place(x=310, y=200)

# Turns the user input into a string
code_var=tk.StringVar()
# This is an entry box for the user to input the amount of student tickets they want to book
code_entry = Entry(confirmation, textvariable = code_var, width="4").place(x=240, y=225)
# Labels the entry box for the card security code of the users credit card
code_label = Label(confirmation, text="Enter card security code: ").place(x=100, y=225)

# This definition checks that the responses from the entry boxes are valid
def info_submit_check():
    email_validity = False
    name_validity = False
    card_validity = False
    month_validity = False
    year_validity = False
    code_validity = False
    email=email_var.get()
    name=name_var.get()
    card=card_var.get()
    month=month_var.get()
    year=year_var.get()
    code=code_var.get()
    if "@" not in email:
        email_var.set('')
    else:
        email_validity = True
    if name.isdigit():
        name_var.set('')
    else:
        name_validity = True
    new_card = card.replace("-", "")
    if new_card.isnumeric():
        int(new_card)
        if len(new_card) == 16:
            card_validity = True
        else:
            card_var.set('')
    else:
        card_var.set('')
    if month.isnumeric():
        if int(month) > 0 and int(month) < 13:
            month_validity = True
        else:
             month_var.set('')
    else:
        month_var.set('')
    if year.isnumeric():
        int(year)
        if int(year) > 22 and int(year) < 29:
            year_validity = True
        else:
            year_var.set('')
    else:
        year_var.set('')
    if code.isnumeric():
        if len(code) == 3:
            code_validity = True
        else:
            code_var.set('')
    else:
        code_var.set('')
    
    # If all user input is valid, a file will be created to read and write the data
    if email_validity == True and name_validity == True and card_validity==True and month_validity==True and year_validity==True and code_validity==True:
        print("hi")
        receit = open("receit.txt", "r")
        list_of_lines = receit.readlines()
        list_of_lines[0] = name+"\n"
        list_of_lines[1] = email+"\n\n"
        list_of_lines[2] = "Seats booked:\n"
        for seat in selected_seats:
            list_of_lines[3] = seat +" "
        receit.close()
        receit = open("receit.txt", "w")
        receit.writelines(list_of_lines)
        receit.close()

        #receit.write(name+"\n")
       # receit.write(email+"\n\n")
        #receit.write("Seats booked:\n")
        #for seat in selected_seats:
            #receit.write(seat +" ")
        #receit.write(x[0]+"\n")
        #receit.write(x[1]+"\n")
        #receit.write(x[2]+"\n")
        #receit.close()
    else:
        error()

# This button is used to submit when the user has finished inputting the amount of tickets they want for each ticket type
info_submit = Button(confirmation, text='Submit', fg='White', bg= 'dark green',height = 1, width = 12,command= info_submit_check).place(x=190, y=275)

# This is a definition which displays an error message if the user details is invalid
def error():
    error= Toplevel(window)
    error.geometry("400x40")
    error.title("Error Message")
    Label(error, text= "Invalid response. Please re-check your user details.", font=('Arial 12 bold')).place(x=5,y=20,anchor="w")
    error.grab_set()

# Function for closing window
def Close():
    window.destroy()
  
# Button for closing
exit_button = Button(session, text="Exit", command=Close, bg="tomato2").place(x=440, y=15)
exit_button = Button(booking, text="Exit", command=Close, bg="tomato2").place(x=440, y=15)
exit_button = Button(ticketing, text="Exit", command=Close, bg="tomato2").place(x=440, y=15)
exit_button = Button(confirmation, text="Exit", command=Close, bg="tomato2").place(x=440, y=15)

# This raises the first frame seen when the user opens the program (session)
raise_frame(session)
# This runs the program
window.mainloop()