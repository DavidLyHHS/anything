from tkinter import *
import tkinter as tk
import random
import datetime as dt

date = dt.datetime.now()

window = Tk()
window.geometry('510x590')
window.resizable(False, False)
window.configure(bg="light blue")

def raise_frame(frame):
    frame.tkraise()

session = Frame(window, width=510, height=590, padx=10, pady=10)
booking = Frame(window, width=510, height=590, padx=10, pady=10)
ticketing = Frame(window)
confirmation = Frame(window)

for frame in (session, booking, ticketing, confirmation):
    frame.grid(row=0, column=0, sticky='news')

def movie_heading(location):
    Label(location, text="Movie Seat Booking Program", font=("Arial", "16", "bold"), padx=10, pady=10, bg="red").place(x=0, y=0, height=50, width=420)

movie_heading(session)
movie_heading(booking)
movie_heading(ticketing)
movie_heading(confirmation)

Label(session, text="SESSIONS TODAY: " f"{date:%A, %B %d, %Y}", font=("Arial", "16", "bold"), padx=13, pady=10, width=35, bg="red", borderwidth=5).place(x=0, y=60)

class create_mheading:
    def __init__(self, location, text, bg, x, y):
        self.location = location
        self.text = text
        self.bg = bg
        self.x = x
        self.y = y
        self.mheading = tk.Label(self.location, text = self.text, bg = self.bg, 
                             padx=50, pady=50, font=("Arial", "16", "bold"), relief="groove", borderwidth=3) 
        self.mheading.place(x = self.x, y=self.y)

m_movie_one = create_mheading(session, "Movie 1","red",0,130)
m_movie_two = create_mheading(session, "Movie 2","red",0,280)
m_movie_three = create_mheading(session, "Movie 3","red",0,430)

class create_minformation:
    def __init__(self, location, text, bg, x, y):
        self.location = location
        self.text = text
        self.bg = bg
        self.x = x
        self.y = y
        self.mheading = tk.Label(self.location, text = self.text, bg = self.bg, 
                             padx=105, pady=30, font=("Arial", "16", "bold"), relief="groove", borderwidth=3) 
        self.mheading.place(x = self.x, y=self.y)

i_movie_one = create_minformation(session, "Movie 1","red",195,130)
i_movie_two = create_minformation(session, "Movie 2","red",195,280)
i_movie_three = create_minformation(session, "Movie 3","red",195,430)

def on_click(text, value):
    tk.Label(booking, text=text, font='Helvetica 10', bg="red").place(x=200, y=60, height=20, width=200)
    if value == "Movie 1":
        tk.Label(booking, text="Movie 1", font='Helvetica 10', bg="red").place(x=0, y=60, height=20, width=180)
    elif value == "Movie 2":
        tk.Label(booking, text="Movie 2", font='Helvetica 10', bg="red").place(x=0, y=60, height=20, width=180)
    else:
        tk.Label(booking, text="Movie 3", font='Helvetica 10', bg="red").place(x=0, y=60, height=20, width=180)

class create_mbutton:
    def __init__(self, location, text, bg, x, y, value):
        self.location = location
        self.text = text
        self.bg = bg
        self.x = x
        self.y = y
        self.mbuttons = tk.Button(self.location, text = self.text, bg = self.bg, 
                             padx=0, pady=1, font=("Arial", "13", "bold"), relief="groove", borderwidth=3, command=lambda:(raise_frame(booking),on_click(text, value)))
        self.mbuttons.place(x = self.x, y=self.y)

m1s1 = create_mbutton(session, "Session 1", "blue", 195, 225, "Movie 1")
m1s2 = create_mbutton(session, "Session 2", "blue", 295, 225, "Movie 1")
m1s3 = create_mbutton(session, "Session 3", "blue", 395, 225, "Movie 1")
m2s1 = create_mbutton(session, "Session 1", "blue", 195, 375, "Movie 2")
m2s2 = create_mbutton(session, "Session 2", "blue", 295, 375, "Movie 2")
m2s3 = create_mbutton(session, "Session 3", "blue", 395, 375, "Movie 2")
m3s1 = create_mbutton(session, "Session 1", "blue", 195, 525, "Movie 3")
m3s2 = create_mbutton(session, "Session 2", "blue", 295, 525, "Movie 3")
m3s3 = create_mbutton(session, "Session 3", "blue", 395, 525, "Movie 3")

class create_seats:
    def __init__(self, location, text, bg, x, y):
        self.location = location
        self.text = text
        self.bg = bg
        self.x = x
        self.y = y
        self.seats = tk.Button(self.location, text = self.text, bg = self.bg, 
                             padx=3, pady=3, font=("Arial", "13", "bold"), relief="groove", borderwidth=3, command=lambda:(raise_frame(booking),seat_select(text)))
        self.seats.place(x = self.x, y=self.y)

position_x = 0
position_y = 0
seats_list = {}
for row in range(ord("A"), ord("F") + 1):
    if chr(row) == "A":
        position_x= 115
    elif chr(row) =="B": 
        position_x= 160
    elif chr(row) =="C": 
        position_x= 205
    elif chr(row) =="D": 
        position_x= 250
    elif chr(row) =="E": 
        position_x= 295
    else:
        position_x= 340
    for column in range(1, 11):
        if column == 1:
            position_y = 135
        elif column ==2:
            position_y = 180
        elif column ==3:
            position_y = 225
        elif column ==4:
            position_y = 270
        elif column ==5:
            position_y = 315
        elif column ==6:
            position_y = 360
        elif column ==7:
            position_y = 405
        elif column ==8:
            position_y = 450
        else:
            position_y = 495
        seats_list[(chr(row)+str(column))] = create_seats(booking, (chr(row)+str(column)), "blue", position_x, position_y)
        
        #print(seats_list["A2"])
        #seats_list = list(set(seats_list))
for seats in seats_list:
    print(seats)
if "L2" in seats_list:
    print("good morning")
else:
    print("hi")


selected_seats = []
def seat_select(text):
    display_seats = Label(booking, text=selected_seats, padx=13, pady=10, width=35, bg="red", borderwidth=5).place(x=0, y=550)
    if text in seats_list and text not in selected_seats:
        selected_seats.append(text)
        selected_seats.sort()
    else:
        selected_seats.remove(text)

#print(seats['A2'])
        #print(seats_list[('A2')])
        #seats_list[(A1)].configure(font="10")
#seats_list[(1, 1)] = create_seats(booking, "A1", "blue", 395, 525, value="Movie 3")
#seats_list[(1, 1)] = create_seats(x=50, y=40)

# Function for closing window
def Close():
    window.destroy()
  
# Button for closing
exit_button = Button(session, text="Exit", command=Close, bg="tomato2").place(x=440, y=15)
exit_button = Button(booking, text="Exit", command=Close, bg="tomato2").place(x=440, y=15)

Label(booking, text='BOOKING').pack()
Button(booking, text='Go to TICKETING', command=lambda:raise_frame(ticketing)).pack()

Label(ticketing, text='TICKETING').pack(side='left')
Button(ticketing, text='Go to CONFIRMATION', command=lambda:raise_frame(confirmation)).pack(side='left')

Label(confirmation, text='CONFIRMATION').pack()
Button(confirmation, text='Go to to SESSION', command=lambda:raise_frame(session)).pack()

raise_frame(session)
window.mainloop()