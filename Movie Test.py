from tkinter import *
import tkinter as tk
import random
import datetime as dt

# Tracks users current date on device
date = dt.datetime.now()

# Creates a window and customises it
window = Tk()
window.geometry('510x590')
window.resizable(False, False)
window.configure(bg="teal")

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
        session_num = str("Session " + str(session_number))
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
                             padx=3, pady=3, font=("Arial", "13", "bold"), relief="groove", borderwidth=3, command=lambda:(raise_frame(booking),seat_select(self, text)))
        self.seats.place(x = self.x, y=self.y)

# Uses the seats class to create buttons for sixty named seats
position_x = 0
position_y = 95
seats_list = {}
for row in range(ord("A"), ord("F") + 1):
    position_y = 95
    position_x = position_x +45
    for column in range(1, 11):
        position_y=position_y+45
        seats_list[(chr(row)+str(column))] = seats(booking, (chr(row)+str(column)), "green", position_x, position_y)

# This list stores user selected seats based on what button created from the seat class they click
selected_seats = []
# Label allows user to know that their selected seats are what is being displayed on the screen
Label(booking, padx=20, bg="purple", text="Selected Seats:").place(x=0, y=100)
# Creates a definition that is called when a seat class button is clicked
def seat_select(self, text):
    # Appends seat choice to the selected_seats list and turns button clicked blue 
    # Appends only if the list has less than 10 items, and seat not already inside the list
    if text not in selected_seats and len(selected_seats) < 10:
        self.seats.configure(bg="blue")
        selected_seats.append(text)
        selected_seats.sort()
        # Displays current selected_seats list in a label
        display_seats = Label(booking, text=selected_seats, padx=5, pady=8, width=22, bg="red", borderwidth=5).place(x=135, y=90)
    # Removes seat choice from the selected_seats list and turns button clicked green
    # Removes only if the seat choice is already inside the list
    elif text in selected_seats:
        self.seats.configure(bg="green")
        selected_seats.remove(text)
        # Displays current selected_seats list in a label
        display_seats = Label(booking, text=selected_seats, padx=5, pady=8, width=22, bg="red", borderwidth=5).place(x=135, y=90)
    # If the other conditions do not apply, a definition for a help menu will be called
    else:
        help() 

# A definition for a help window for their seat booking
def help():
    top= Toplevel(window)
    top.geometry("750x250")
    top.title("Help")
    Label(top, text= "There is a maximum of 10 seats per booking! Sorry for the inconvenience!", font=('Mistral 18 bold')).place(x=150,y=80)
    top.grab_set()

# A button for the user to press to manually show the help window when required
help_button = Button(booking, text="Help/Info", command=lambda:(help())).place(x=430, y=55)

key_label = Label(booking, padx=20, bg="purple", text="Key for Seats:").place(x=355, y=100)

confirm_seat = Button(booking, bg="orange", text='Confirm Seats', command=lambda:(raise_frame(ticketing), ticket_number(selected_seats))).place(x=380, y=380)

class create_key:
    def __init__(self, location, bg, x, y):
        self.location = location
        self.bg = bg
        self.x = x
        self.y = y
        self.key = tk.Label(self.location, bg = self.bg, 
                            height=2, width=4, relief="groove", borderwidth=3) 
        self.key.place(x = self.x, y=self.y)

available = create_key(booking, "green", 325, 140)
booked = create_key(booking, "red", 325, 185)
clicked = create_key(booking, "blue", 325, 230)
disability = create_key(booking, "grey", 325, 275)

class create_key_name:
    def __init__(self, location, text, x, y):
        self.location = location
        self.text = text
        self.x = x
        self.y = y
        self.key_name = tk.Label(self.location, text = self.text,
                            height=2, width=17, relief="groove", borderwidth=3) 
        self.key_name.place(x = self.x, y=self.y)

available_text = create_key_name(booking, "   =   Available Seat", 370, 140)
booked_text = create_key_name(booking, "   =    Booked Seat", 370, 185)
clicked_text = create_key_name(booking, "   =   Selected Seat", 370, 230)
disability_text = create_key_name(booking, "   =  Disability Seat", 370, 275)

class create_ticket_number:
    def __init__(self, location, bg, x, y):
        self.location = location
        self.bg = bg
        self.x = x
        self.y = y
        self.ticket_number = tk.Label(self.location, bg = self.bg, 
                             height=2, width=4, relief="groove", borderwidth=3) 
        self.ticket_number.place(x = self.x, y = self.y)

ticket_list = {}
def ticket_number(selected_seats):
    position_x=120
    for i in range(len(selected_seats)):
        position_x = position_x + 32
        ticket_list[(i)] = create_ticket_number(ticketing,"green", position_x, 120)

    for ticket in ticket_list:
        print(ticket)

to_book = Label(ticketing, text="Tickets left to book: ").place(x=38, y=130)

student_var=tk.StringVar()
student_ticket = Entry(ticketing, textvariable = student_var, width="10").place(x=250, y=230)

adult_var=tk.StringVar()
adult_ticket = Entry(ticketing, textvariable = adult_var, width="10").place(x=250, y=255)

senior_var=tk.StringVar()
senior_ticket = Entry(ticketing, textvariable = senior_var, width="10").place(x=250, y=280)

def on_calculate_student():
    student=student_var.get()
    adult=adult_var.get()
    senior=senior_var.get()
    if student.isnumeric():
        student = int(student)
    else:
        student = 0
    if adult.isnumeric():
        adult = int(adult)
    else:
        adult= 0
    if senior.isnumeric():
        senior = int(senior)
    else:
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
        student_pricing = "Student Ticket " + str(student) +"x = $" + str(student_price)
        banana = Label(ticketing, text=student_pricing, bg="yellow", width="30", font= ('Century 15 bold')).place(x=50, y=375)
        banana = Label(confirmation, text=student_pricing, bg="yellow", width="30", font= ('Century 15 bold')).place(x=50, y=375)

        adult_price =adult*18
        adult_pricing = "Adult Ticket " + str(adult) +"x = $" + str(adult_price)
        Label(ticketing, text=adult_pricing, bg="yellow", width="30", font= ('Century 15 bold')).place(x=50, y=400)
        Label(confirmation, text=adult_pricing, bg="yellow", width="30", font= ('Century 15 bold')).place(x=50, y=400)

        senior_price = senior*14
        senior_pricing = "Senior Ticket " + str(senior) +"x = $" + str(senior_price)
        Label(ticketing, text=senior_pricing, bg="yellow", width="30", font= ('Century 15 bold')).place(x=50, y=425)
        Label(confirmation, text=senior_pricing, bg="yellow", width="30", font= ('Century 15 bold')).place(x=50, y=425)

        total = int(student_price) + int(adult_price) + int(senior_price)
        total_price = "Total cost = $" + str(total)
        Label(ticketing, text=total_price, bg="yellow", width="30", font= ('Century 15 bold')).place(x=50, y=450)
        Label(confirmation, text=total_price, bg="yellow", width="30", font= ('Century 15 bold')).place(x=50, y=450)

        order_summary = Label(ticketing, bg="yellow", width="30", text="Order Summary:", font= ('Century 15 bold')).place(x=50, y=340)
        order_summary = Label(confirmation, bg="yellow", width="30", text="Order Summary:", font= ('Century 15 bold')).place(x=50, y=340)
        Button(ticketing, text='Confirm Order', fg='White', bg= 'dark green',height = 1, width = 10, command=lambda:raise_frame(confirmation)).place(x=225, y=500)

submit = Button(ticketing, text='Submit', fg='White', bg= 'dark green',height = 1, width = 12,command= on_calculate_student).place(x=330, y=275)

def ticketing_help():
    ticket_help= Toplevel(window)
    ticket_help.geometry("750x250")
    ticket_help.title("Help")
    Label(ticket_help, text= "Invalid reponse or incorrect number of tickets booked!", font=('Mistral 18 bold')).place(x=150,y=80)
    ticket_help.grab_set()

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

student_ticket_label = create_ticket_type(ticketing, "orange", "Student Ticket Price = $12", 100, 230, 0)
adult_ticket_label = create_ticket_type(ticketing, "yellow", "Student Ticket Price = $18", 100, 255, 0)
senior_ticket_label = create_ticket_type(ticketing, "green", "Student Ticket Price = $14", 100, 280, 0)
ticket_chooser_label = create_ticket_type(ticketing, "green", "Choose your ticket(s)", 100, 200, 100)

# Function for closing window
def Close():
    window.destroy()
  
# Button for closing
exit_button = Button(session, text="Exit", command=Close, bg="tomato2").place(x=440, y=15)
exit_button = Button(booking, text="Exit", command=Close, bg="tomato2").place(x=440, y=15)
exit_button = Button(ticketing, text="Exit", command=Close, bg="tomato2").place(x=440, y=15)

Label(confirmation, text='CONFIRMATION').pack()
Button(confirmation, text='Go to to SESSION', command=lambda:raise_frame(session)).pack()

raise_frame(session)
window.mainloop()