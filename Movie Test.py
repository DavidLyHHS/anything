"""This file is a movie seat booking program."""

import tkinter as tk
import random
import datetime as dt

# These two lists will be used for creating a random booked seat
letter_list = ["A", "B", "C", "D", "E", "F"]
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# using random.choice() to get a random letter and number from the two lists
random_let = random.choice(letter_list)
random_num = random.choice(number_list)

# Joins random_let and random_num, makes a random booked_seat
booked_seat = str(random_let) + str(random_num)

# Creates lines for the txt file
receit = open("receit.txt", "w")
for i in range(9):
    receit.write("\n")
receit.close()

# Tracks users current date on device
date = dt.datetime.now()

# Creates a window and customises it
window = tk.Tk()
window.geometry("510x590")
window.title("Movie Seat Booking Program")
window.resizable(False, False)


def raise_frame(frame):
    """Brings a frame to the front."""
    frame.tkraise()


# Create frames and customises it
session = tk.Frame(window, bg="#D6D6D6",
                   width=510, height=590, padx=10, pady=10)
booking = tk.Frame(window, bg="#D6D6D6",
                   width=510, height=590, padx=10, pady=10)
ticketing = tk.Frame(window, bg="#D6D6D6",
                     width=510, height=590, padx=10, pady=10)
confirmation = tk.Frame(window, bg="#D6D6D6",
                        width=510, height=590, padx=10, pady=10)

# Places frames on a grid
for frame in (session, booking, ticketing, confirmation):
    frame.grid(row=0, column=0, sticky="news")


def program_heading(location):
    """Create a heading for the program."""
    tk.Label(
        location,
        text="Movie Seat Booking Program",
        fg="white",
        font=("Arial", "16", "bold"),
        padx=10,
        pady=10,
        bg="#313D5A",
    ).place(x=0, y=0, height=50, width=420)


# Places the heading created for the program onto all the frames
program_heading(session)
program_heading(booking)
program_heading(ticketing)
program_heading(confirmation)

# Label to display the current date on the users device
session_label = tk.Label(
    session,
    fg="white",
    font=("Arial", "16", "bold"),
    text="SESSIONS TODAY: " f"{date:%A, %B %d, %Y}",
    padx=13,
    pady=10,
    width=35,
    bg="#313D5A",
    borderwidth=5,
).place(x=0, y=60)


class MovieTypes:
    """Create a class for creating labels for the different movie types."""

    def __init__(self, location, text, bg, x, y):
        """Choose frame, text, background colour, x and y positions."""
        self.location = location
        self.text = text
        self.bg = bg
        self.x = x
        self.y = y
        self.mheading = tk.Label(
            self.location,
            text=self.text,
            bg=self.bg,
            padx=20,
            pady=20,
            fg="white",
            font=("Arial", "16", "bold"),
            relief="groove",
            borderwidth=3,
        )
        self.mheading.place(x=self.x, y=self.y)


# Create three movie labels
position_y = -20
movie_number = 0
for movie in range(1, 4):
    movie_number = movie_number + 1
    position_y = position_y + 150
    if movie_number == 1:
        movie_num = str("Misadventure\nof Cancan")
    elif movie_number == 2:
        movie_num = str("The Duke of\nthe Hoops II")
    else:
        movie_num = str("Henry Totter:\nChalice of Sea")
    MovieTypes(session, movie_num, "#313D5A", 0, position_y)


class MovieInformation:
    """Create labels for the different movie informations."""

    def __init__(self, location, text, bg, x, y):
        """Choose frame, frame, text, background colour, x and y positions."""
        self.location = location
        self.text = text
        self.bg = bg
        self.x = x
        self.y = y
        self.mheading = tk.Label(
            self.location,
            text=self.text,
            bg=self.bg,
            padx=90,
            pady=30,
            fg="white",
            font=("Arial", "16", "bold"),
            relief="groove",
            borderwidth=3,
        )
        self.mheading.place(x=self.x, y=self.y)


# Create three movie information labels
position_y = -20
for information in range(3):
    position_y = position_y + 150
    MovieInformation(session, "Information", "#313D5A", 195, position_y)


class MovieChoice:
    """Make buttons for the different sessions and their respective movies."""

    def __init__(self, location, text, bg, x, y, value):
        """Choose frame, text, background, x and y positions and value."""
        self.location = location
        self.text = text
        self.bg = bg
        self.x = x
        self.y = y
        self.mbuttons = tk.Button(
            self.location,
            text=self.text,
            bg=self.bg,
            padx=0,
            pady=1,
            font=("Arial", "13", "bold"),
            relief="groove",
            borderwidth=3,
            command=lambda: (raise_frame(booking), on_click(text, value)),
        )
        self.mbuttons.place(x=self.x, y=self.y)


# Create nine buttons (three session buttons for each of the three movies)
position_y = 75
movie_number = 0
for movie in range(1, 4):
    position_x = 95
    position_y = position_y + 150
    movie_number = movie_number + 1
    for session_number in range(1, 4):
        position_x = position_x + 100
        session_num = str(session_number) + str(":00PM")
        if movie_number == 1:
            movie_num = str("Misadventure of Cancan")
        elif movie_number == 2:
            movie_num = str("The Duke of the Hoops II")
        else:
            movie_num = str("Henry Totter: Chalice of Sea")
        MovieChoice(session, session_num, "#73628A",
                    position_x, position_y, movie_num)


# Make session and movie labels for other frames
def on_click(value, text):
    """Value is movie chosen and text is session chosen."""
    tk.Label(
        booking, text=text, fg="white", font="Helvetica 10", bg="#313D5A"
    ).place(x=0, y=60, height=20, width=200)
    tk.Label(
        booking, text=value, fg="white", font="Helvetica 10", bg="#313D5A"
    ).place(x=220, y=60, height=20, width=200)
    tk.Label(
        ticketing, text=text, fg="white", font="Helvetica 10", bg="#313D5A"
    ).place(x=0, y=60, height=20, width=200)
    tk.Label(
        ticketing, text=value, fg="white", font="Helvetica 10", bg="#313D5A"
    ).place(x=220, y=60, height=20, width=200)
    tk.Label(
        confirmation, text=text, fg="white", font="Helvetica 10", bg="#313D5A"
    ).place(x=0, y=60, height=20, width=200)
    tk.Label(
        confirmation, text=value, fg="white", font="Helvetica 10", bg="#313D5A"
    ).place(x=220, y=60, height=20, width=200)
    receit = open("receit.txt", "r")
    list_of_lines = receit.readlines()
    list_of_lines[0] = text + " at " + value + "\n"
    receit = open("receit.txt", "w")
    receit.writelines(list_of_lines)
    receit.close()


class Seats:
    """Make buttons for the movie seats."""

    def __init__(self, location, text, bg, x, y):
        """Choose frame, text, background, x and y positions and value."""
        self.location = location
        self.text = text
        self.bg = bg
        self.x = x
        self.y = y
        self.seats = tk.Button(
            self.location,
            text=self.text,
            bg=self.bg,
            padx=3,
            pady=3,
            font=("Arial", "7", "bold"),
            relief="groove",
            borderwidth=3,
            command=lambda: (raise_frame(booking), seat_select(self, text)),
        )
        self.seats.place(x=self.x, y=self.y)


# Uses the seats class to create buttons for sixty named seats
position_x = 0
position_y = 95
seats_list = []
for row in range(ord("A"), ord("F") + 1):
    position_y = 95
    position_x = position_x + 45
    for column in range(1, 11):
        if random_let == chr(row) and random_num == (column):
            position_y = position_y + 45
            seats_list.append(Seats(booking, chr(row)+str(column),
                                    "red", position_x, position_y))
        elif column == 10:
            position_y = position_y + 45
            seats_list.append(Seats(booking, chr(row)+str(column),
                                    "yellow", position_x, position_y))
        else:
            position_y = position_y + 45
            seats_list.append(Seats(booking, chr(row)+str(column),
                                    "grey", position_x, position_y))

# Stores user selected seats
selected_seats = []
# Label for selected seats
tk.Label(booking, padx=20, fg="white",
         bg="#313D5A", text="Selected Seats:").place(x=0, y=100)


def seat_select(self, text):
    """Add and remove seats from selected_seats list based on conditions."""
    if booked_seat in text:
        print("Seat is already booked!")
    elif text not in selected_seats and len(selected_seats) < 10:
        self.seats.configure(bg="green")
        selected_seats.append(text)
        selected_seats.sort()
        tk.Label(booking, text=selected_seats, padx=5, pady=8, width=22,
                 fg="white", bg="#313D5A", borderwidth=5).place(x=135, y=90)
    elif text in selected_seats and "10" not in text:
        self.seats.configure(bg="grey")
        selected_seats.remove(text)
        tk.Label(booking, text=selected_seats, padx=5, pady=8, width=22,
                 fg="white", bg="#313D5A", borderwidth=5).place(x=135, y=90)
    elif text in selected_seats and "10" in text:
        self.seats.configure(bg="yellow")
        selected_seats.remove(text)
        tk.Label(booking, text=selected_seats, padx=5, pady=8, width=22,
                 fg="white", bg="#313D5A", borderwidth=5).place(x=135, y=90)
    else:
        help()


def help():
    """Help window for seat booking."""
    top = tk.Toplevel(window)
    top.geometry("450x250")
    top.title("Help Menu")
    tk.Label(top, text="Select and deselect seats by clicking seat buttons."
             "\n\nSelected seats appear near the top of the screen.\n\n"
             "Maximum of 10 seats per booking.\n\n"
             "If unable to book seat, seat is already booked (See key)\n\n"
             "Once done selecting seats, click the confirm button.\n\n"
             "Make sure you have selected at least one seat.",
             font=('Arial 12 bold')).place(x=5, y=120, anchor="w")
    top.grab_set()

# A button for the user to press to manually show the help window when required
help_button = tk.Button(booking, text="Help/Info",
                        command=lambda: (help())).place(x=430, y=55)

# A label for the key about what the colour of the seat buttons mean
key_label = tk.Label(booking, padx=20, fg="white", bg="#313D5A",
                     text="Key for Seats:").place(x=355, y=100)

# A button for confirming the user seats selected
confirm_seat = tk.Button(booking, bg="dark green", fg="white",
                         text='Confirm Seats',
                         command=lambda: (check_tickets(selected_seats),
                                          ticket_number(selected_seats))
                         ).place(x=380, y=380)


def check_tickets(selected_seats):
    """Check for at least one selected seat."""
    if len(selected_seats) == 0:
        help()
    else:
        raise_frame(ticketing)


class CreateKey:
    """Create key labels with the different colourings."""

    def __init__(self, location, bg, x, y):
        """Choose frame, background colour, x and y positions."""
        self.location = location
        self.bg = bg
        self.x = x
        self.y = y
        self.key = tk.Label(self.location, bg=self.bg,
                            height=2, width=4, relief="groove", borderwidth=3)
        self.key.place(x=self.x, y=self.y)


# These are the labels themselves created using the create_key label
CreateKey(booking, "grey", 325, 140)
CreateKey(booking, "red", 325, 185)
CreateKey(booking, "green", 325, 230)
CreateKey(booking, "yellow", 325, 275)


class CreateKeyName:
    """Create named labels of the keys."""

    def __init__(self, location, text, x, y):
        """Choose frame, text, x and y positions."""
        self.location = location
        self.text = text
        self.x = x
        self.y = y
        self.key_name = tk.Label(self.location, text=self.text,
                                 height=2, width=17,
                                 relief="groove", borderwidth=3)
        self.key_name.place(x=self.x, y=self.y)


# Create four labels which associate a key colour with meaning
CreateKeyName(booking, "   =   Available Seat", 370, 140)
CreateKeyName(booking, "   =    Booked Seat", 370, 185)
CreateKeyName(booking, "   =   Selected Seat", 370, 230)
CreateKeyName(booking, "   =  Disability Seat", 370, 275)


class CreateTicketNumber:
    """Create ticket labels that show the user how many seats they selected."""

    def __init__(self, location, bg, text, x, y):
        """Choose frame, background colour, text, x and y positions."""
        self.location = location
        self.bg = bg
        self.text = text
        self.x = x
        self.y = y
        self.ticket_number = tk.Label(self.location, bg=self.bg,
                                      text=self.text,
                                      height=2, width=4, fg="white",
                                      relief="groove", borderwidth=3)
        self.ticket_number.place(x=self.x, y=self.y)


ticket_list = {}


def ticket_number(selected_seats):
    """Check seats selected, labels equal amount selected."""
    position_x = 120
    count = 0
    for i in range(len(selected_seats)):
        count = count + 1
        position_x = position_x + 32
        ticket_list[(i)] = CreateTicketNumber(ticketing,
                                              "#313D5A", count,
                                              position_x, 120)


# Lets the user know what the create_ticket_number class is displaying
to_book = tk.Label(ticketing, fg="white", bg="#313D5A",
                   text="Tickets left to book: ").place(x=33, y=130)

# Turns the user input into a string
student_var = tk.StringVar()
# User input for amount of student tickets they want to book
student_ticket = tk.Entry(ticketing, textvariable=student_var,
                          width="10").place(x=250, y=230)

# Turns the user input into a string
adult_var = tk.StringVar()
# User input for amount of adult tickets they want to book
adult_ticket = tk.Entry(ticketing, textvariable=adult_var,
                        width="10").place(x=250, y=255)

# Turns the user input into a string
senior_var = tk.StringVar()
# User input for amount of senior tickets they want to book
senior_ticket = tk.Entry(ticketing, textvariable=senior_var,
                         width="10").place(x=250, y=280)


def submit_check():
    """Create summary based on all entry user input."""
    student = student_var.get()
    adult = adult_var.get()
    senior = senior_var.get()
    if student.isnumeric():
        student = int(student)
    else:
        student_var.set('')
        student = 0
    if adult.isnumeric():
        adult = int(adult)
    else:
        adult_var.set('')
        adult = 0
    if senior.isnumeric():
        senior = int(senior)
    else:
        senior_var.set('')
        senior = 0
    amount_of_tickets = student + adult + senior
    if amount_of_tickets != len((selected_seats)):
        student_var.set('')
        adult_var.set('')
        senior_var.set('')
        ticketing_help()
    else:
        student_price = student*12
        student_pricing = str(student) + "x " +\
            "Student Ticket(s) = $" + str(student_price)
        tk.Label(ticketing, text=student_pricing, fg="white", bg="#313D5A",
                 width="30", font=('Century 15 bold')).place(x=30, y=375)
        tk.Label(confirmation, text=student_pricing, fg="white", bg="#313D5A",
                 width="30", font=('Century 15 bold')).place(x=30, y=375)

        adult_price = adult*18
        adult_pricing = str(adult) + "x " +\
            "Adult Ticket(s) = $" + str(adult_price)
        tk.Label(ticketing, text=adult_pricing, fg="white", bg="#313D5A",
                 width="30", font=('Century 15 bold')).place(x=30, y=400)
        tk.Label(confirmation, text=adult_pricing, fg="white", bg="#313D5A",
                 width="30", font=('Century 15 bold')).place(x=30, y=400)

        senior_price = senior*14
        senior_pricing = str(senior) + "x " +\
            "Senior Ticket(s) = $" + str(senior_price)
        tk.Label(ticketing, text=senior_pricing, fg="white", bg="#313D5A",
                 width="30", font=('Century 15 bold')).place(x=30, y=425)
        tk.Label(confirmation, text=senior_pricing, fg="white", bg="#313D5A",
                 width="30", font=('Century 15 bold')).place(x=30, y=425)

        total = int(student_price) + int(adult_price) + int(senior_price)
        total_price = "Total cost = $" + str(total)
    

        tk.Label(ticketing, text=total_price, fg="white", bg="#313D5A",
                 width="30", font=('Century 15 bold')).place(x=30, y=450)
        tk.Label(confirmation, text=total_price, fg="white",
                 bg="#313D5A", width="30",
                 font=('Century 15 bold')).place(x=30, y=450)
        tk.Label(ticketing, fg="white", bg="#313D5A", width="30",
                 text="Order Summary:", font=('Century 15 bold')
                 ).place(x=30, y=340)
        tk.Label(confirmation, fg="white", bg="#313D5A", width="30",
                 text="Order Summary:",
                 font=('Century 15 bold')).place(x=30, y=340)
        tk.Button(ticketing, text='Confirm Order', fg='White',
                  bg='dark green', height=1, width=10,
                  command=lambda: raise_frame(confirmation)
                  ).place(x=205, y=500)
        receit = open("receit.txt", "r")
        list_of_lines = receit.readlines()
        list_of_lines[4] = student_pricing+"\n"
        list_of_lines[5] = adult_pricing+"\n"
        list_of_lines[6] = senior_pricing+"\n"
        list_of_lines[7] = total_price+"\n"
        receit.close()
        receit = open("receit.txt", "w")
        receit.writelines(list_of_lines)
        receit.close()


# Submit for user input for amount of tickets per type
tk.Button(ticketing, text='Submit', fg='White', bg='dark green',
          height=1, width=12, command=submit_check).place(x=330, y=275)


def ticketing_help():
    """Help menu when clicked or when error occurs."""
    ticket_help = tk.Toplevel(window)
    ticket_help.geometry("420x40")
    ticket_help.title("Ticketing Help")
    tk.Label(ticket_help,
             text="Invalid reponse or incorrect number of tickets booked!",
             font=('Arial 12 bold')).place(x=5, y=20, anchor="w")
    ticket_help.grab_set()


class CreateTicketType:
    """Associates ticket types with prices in a label."""

    def __init__(self, location, bg, fg, text, x, y, padx):
        """Choose frame, background and foreground, x and y position, padx."""
        self.location = location
        self.bg = bg
        self.fg = fg
        self.text = text
        self.x = x
        self.y = y
        self.padx = padx
        self.ticket_type = tk.Label(self.location, bg=self.bg, fg=self.fg,
                                    text=self.text, padx=self.padx)
        self.ticket_type.place(x=self.x, y=self.y)


# Ticket to price labels
CreateTicketType(ticketing, "#313D5A", "white",
                 "Student Ticket Price = $12", 100, 230, 0)
CreateTicketType(ticketing, "#313D5A", "white",
                 "Adult Ticket Price     = $18", 100, 255, 0)
CreateTicketType(ticketing, "#313D5A", "white",
                 "Senior Ticket Price    = $14", 100, 280, 0)
CreateTicketType(ticketing, "#313D5A", "white",
                 "Choose your ticket(s)", 100, 200, 100)

# Tells user that input boxes below are for user information
tk.Label(confirmation, fg="white", bg="#313D5A",
         text="Please enter in user details in the boxes below: "
         ).place(x=100, y=90)

# Turns the user input into a string
name_var = tk.StringVar()
# This is an entry box for the user to input their name
name_entry = tk.Entry(confirmation, textvariable=name_var, width="29")
name_entry.place(x=175, y=125)
name_entry.insert(0, "Please type here...")
# Labels the entry box for name input
tk.Label(confirmation, bg="#313D5A", fg="white", text="Enter name: "
         ).place(x=100, y=125)

# Turns the user input into a string
email_var = tk.StringVar()
# This is an entry box for the user to input their email address
email_entry = tk.Entry(confirmation, textvariable=email_var, width="22")
email_entry.place(x=217, y=150)
email_entry.insert(0, "Please type here...")
# Labels the entry box for email input
tk.Label(confirmation, bg="#313D5A", fg="white", text="Enter email address: "
         ).place(x=100, y=150)

# Turns the user input into a string
card_var = tk.StringVar()
# This is an entry box for the user to input their credit card number
card_entry = tk.Entry(confirmation, textvariable=card_var, width="30")
card_entry.place(x=168, y=175)
card_entry.insert(0, "XXXX-XXXX-XXXX-XXXX")
# Labels the entry box for credit card input
tk.Label(confirmation, bg="#313D5A", fg="white", text="Enter card: "
         ).place(x=100, y=175)

# Turns the user input into a string
month_var = tk.StringVar()
# Entry box for the user to input the expiry month of their credit card
expiry_entry = tk.Entry(confirmation, textvariable=month_var, width="3")
expiry_entry.place(x=285, y=200)
expiry_entry.insert(0, "XX")
# Labels the entry box for the expiry date of the users credit card
tk.Label(confirmation, bg="#313D5A", fg="white",
         text="Enter card expiry date (MM/YY): ").place(x=100, y=200)
# Turns the user input into a string
year_var = tk.StringVar()
# Entry box for the user to input the expiry year of their credit card
year_entry = tk.Entry(confirmation, textvariable=year_var, width="3")
year_entry.place(x=330, y=200)
year_entry.insert(0, "XX")
# Labels inbetween the entry boxes for credit card expiry month and year
tk.Label(confirmation, bg="#313D5A", fg="white", text=" / "
         ).place(x=310, y=200)
# Turns the user input into a string
code_var = tk.StringVar()
# Entry box for user to input their card security code
code_entry = tk.Entry(confirmation, textvariable=code_var,
          width="4", show="*")
code_entry.place(x=240, y=225)
code_entry.insert(0, "XXX")
# Labels the entry box for the card security code of the users credit card
tk.Label(confirmation, bg="#313D5A", fg="white",
         text="Enter card security code: ").place(x=100, y=225)


def name_temp(e):
   """Deletes temporary text"""
   name_entry.delete(0,"end")


def email_temp(e):
   """Deletes temporary text"""
   email_entry.delete(0,"end")


def card_temp(e):
   """Deletes temporary text"""
   card_entry.delete(0,"end")


def expiry_temp(e):
   """Deletes temporary text"""
   expiry_entry.delete(0,"end")


def year_temp(e):
   """Deletes temporary text"""
   year_entry.delete(0,"end")


def code_temp(e):
   """Deletes temporary text"""
   code_entry.delete(0,"end")

 
# Binds the FocusIn event to the entry boxes
name_entry.bind("<FocusIn>", name_temp)
email_entry.bind("<FocusIn>", email_temp)
card_entry.bind("<FocusIn>", card_temp)
expiry_entry.bind("<FocusIn>", expiry_temp)
year_entry.bind("<FocusIn>", year_temp)
code_entry.bind("<FocusIn>", code_temp)


def info_submit_check():
    """Check the validity of the user responses."""
    email_validity = False
    name_validity = False
    card_validity = False
    month_validity = False
    year_validity = False
    code_validity = False
    email = email_var.get()
    name = name_var.get()
    card = card_var.get()
    month = month_var.get()
    year = year_var.get()
    code = code_var.get()
    if "@" not in email:
        email_var.set('')
        tk.Label(confirmation, bg="#D6D6D6", fg="red",
                 text="Please include '@'.").place(x=350, y=150)
    else:
        tk.Label(confirmation, bg="#D6D6D6", fg="#D6D6D6",
                 text="Please include '@'.").place(x=350, y=150)
        email_validity = True
    if name.isalpha():
        tk.Label(confirmation, bg="#D6D6D6", fg="#D6D6D6",
                 text="Please only enter letters.").place(x=350, y=125)
        name_validity = True
    else:
        name_var.set('')
        tk.Label(confirmation, bg="#D6D6D6", fg="red",
                 text="Please only enter letters.").place(x=350, y=125)
    new_card = card.replace("-", "")
    final_card = new_card.replace(" ", "")
    if final_card.isnumeric():
        int(final_card)
        if len(final_card) == 16:
            card_validity = True
            tk.Label(confirmation, bg="#D6D6D6", fg="#D6D6D6",
                     text="Please enter 16 digits.").place(x=350, y=175)
        else:
            tk.Label(confirmation, bg="#D6D6D6", fg="red",
                     text="Please enter 16 digits.").place(x=350, y=175)
            card_var.set('')
    else:
        tk.Label(confirmation, bg="#D6D6D6", fg="red",
                 text="Please enter 16 digits.").place(x=350, y=175)
        card_var.set('')
    if month.isnumeric():
        if int(month) > 0 and int(month) < 13:
            tk.Label(confirmation, bg="#D6D6D6", fg="#D6D6D6",
                     text="MM (1 - 12), YY (23 - 27)").place(x=350, y=200)
            month_validity = True
        else:
            tk.Label(confirmation, bg="#D6D6D6", fg="red",
                     text="MM (1 - 12), YY (23 - 27)").place(x=350, y=200)
            month_var.set('')
    else:
        tk.Label(confirmation, bg="#D6D6D6", fg="red",
                     text="MM (1 - 12), YY (23 - 27)").place(x=350, y=200)
        month_var.set('')
    if year.isnumeric():
        int(year)
        if int(year) > 22 and int(year) < 29:
            tk.Label(confirmation, bg="#D6D6D6", fg="#D6D6D6",
                     text="MM (1 - 12), YY (23 - 27)").place(x=350, y=200)
            year_validity = True
        else:
            tk.Label(confirmation, bg="#D6D6D6", fg="red",
                     text="MM (1 - 12), YY (23 - 27)").place(x=350, y=200)
            year_var.set('')
    else:
        tk.Label(confirmation, bg="#D6D6D6", fg="red",
                 text="MM (1 - 12), YY (23 - 27)").place(x=350, y=200)
        year_var.set('')
    if code.isnumeric():
        if len(code) == 3:
            tk.Label(confirmation, bg="#D6D6D6", fg="#D6D6D6",
                     text="Integers only (MUST BE 3)").place(x=350, y=225)
            code_validity = True
        else:
            tk.Label(confirmation, bg="#D6D6D6", fg="red",
                     text="Integers only (MUST BE 3)").place(x=350, y=225)
            code_var.set('')
    else:
        tk.Label(confirmation, bg="#D6D6D6", fg="red",
                 text="Integers only (MUST BE 3)").place(x=350, y=225)
        code_var.set('')

    # If all user input is valid, read and write the data into text file
    if((((((email_validity is True and
            name_validity is True and
            card_validity is True and
            month_validity is True and
            year_validity is True and
            code_validity is True)))))):
        receit = open("receit.txt", "r")
        list_of_lines = receit.readlines()
        list_of_lines[2] = name + "\n"
        list_of_lines[3] = email + "\n\n"
        receit.close()
        receit = open("receit.txt", "w")
        receit.writelines(list_of_lines)
        receit.write("Seats booked:\n")
        for seat in selected_seats:
            receit.write(seat + ", ")
        receit.close()
        order_confirmed()
    else:
        error()


def order_confirmed():
    """Order confirmed message window."""
    order_confirmed = tk.Toplevel(window)
    order_confirmed.geometry("600x40")
    order_confirmed.title("Order Confirmed!")
    tk.Label(order_confirmed, text="Your booking has been confirmed! "
             "Please check 'receit.txt' for your receit.",
             font=('Arial 12 bold')).place(x=5, y=20, anchor="w")
    order_confirmed.grab_set()


# Submit button after user has finished inputting personal information
tk.Button(confirmation, text='Submit', fg='White', bg='dark green',
          height=1, width=12, command=info_submit_check
          ).place(x=190, y=275)


def error():
    """Display error message if user details are invalid."""
    error = tk.Toplevel(window)
    error.geometry("400x40")
    error.title("Error Message")
    tk.Label(error, text="Invalid response. "
             "Please re-check your user details.", font=('Arial 12 bold')
             ).place(x=5, y=20, anchor="w")
    error.grab_set()


def close():
    """Close window."""
    window.destroy()


# Exit buttons for every frame
exit_button = tk.Button(session, text="Exit",
                        command=close, bg="tomato2").place(x=440, y=15)
exit_button = tk.Button(booking, text="Exit",
                        command=close, bg="tomato2").place(x=440, y=15)
exit_button = tk.Button(ticketing, text="Exit",
                        command=close, bg="tomato2").place(x=440, y=15)
exit_button = tk.Button(confirmation, text="Exit",
                        command=close, bg="tomato2").place(x=440, y=15)

# This raises the first frame seen when the user opens the program (session)
raise_frame(session)
# This runs the program
window.mainloop()
