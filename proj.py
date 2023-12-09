from tkinter import *
import sys 
from datetime import date,timedelta

class PaymentGateway:
    def process_payment(self, amount):
        return amount>0

root=Tk()
root.geometry("300x300")
root.title("Welcome to Bookito: A one stop solution to ticket booking")
MyLabel=Label(root,text="Welcome to Bookito").pack()
MyLabel1=Label(root,text="Follow the below instructions for smooth user experience").pack()
MyLabel2 = Label(root,text="Please select one of the following options to proceed ").pack()
MyLabel3=Label(root,text="\n").pack()

def Create():
    global Create_screen
    Create_screen=Toplevel(root)
    Create_screen.title("Create user")
    l=Label(Create_screen,text="Create your account here",font=('Çalibri',12))
    l.grid(row=0,sticky=N)
    l1=Label(Create_screen,text="Please enter your name:",font=('Çalibri',12))
    l1.grid(row=2,sticky=W)
    l2=Label(Create_screen,text="Please enter your email here",font=('Çalibri',12))
    l2.grid(row=3,sticky=W)
    l3=Label(Create_screen,text="Please enter your email again here:",font=('Calibri',12))
    l3.grid(row=4,sticky=W)
    l4=Label(Create_screen,text="Please enter your password here:",font=('Calibri',12))
    l4.grid(row=5,sticky=W)
    l5=Label(Create_screen,text="Please enter your password again here",font=('Calibri',12))
    l5.grid(row=6,sticky=W)
    global user
    global mail
    global mail2
    global password
    global password2
    user=StringVar()
    mail=StringVar()
    mail2=StringVar()
    password=StringVar()
    password2=StringVar()
    e1=Entry(Create_screen,text=user,width=20)
    e1.grid(row=2,column=2)
    e2=Entry(Create_screen,text=mail,width=20)
    e2.grid(row=3,column=2)
    e3=Entry(Create_screen,text=mail2,width=20)
    e3.grid(row=4,column=2)
    e4=Entry(Create_screen,text=password,show='*',width=20)
    e4.grid(row=5,column=2)
    e5=Entry(Create_screen,text=password2,show='*',width=20)
    e5.grid(row=6,column=2)
    b1=Button(Create_screen,text="Create",command=finish_create,padx=30)
    b1.grid(row=8)
    global notif1
    notif1=Label(Create_screen,font=('Calibri',12))
    notif1.grid(row=10,sticky=N)

def finish_create():
    global a
    global b
    global c
    global d
    global e
    a=user.get()
    b=password.get()
    c=password2.get()
    d=mail.get()
    e=mail2.get()
    if b==c and d.endswith("@gmail.com") and d==e:
        notif1.config(fg="green",text="User created Successfully")
        Create_screen.after(3000,Create_screen.destroy)
    else:
        notif1.config(fg="red",text="Either password entered or email doesnt match the criteria, please try again.")
        
def Login():
    global Login_screen
    Login_screen=Toplevel(root)
    Login_screen.title("Login page")
    l=Label(Login_screen,text="Welcome to the login page",font=('Çalibri',12))
    l.grid(row=0,sticky=N)
    l1=Label(Login_screen,text="Enter Username:",font=('Çalibri',12))
    l1.grid(row=2,sticky=W)
    l2=Label(Login_screen,text="Enter Email you signed up with:",font=('Çalibri',12))
    l2.grid(row=3,sticky=W)
    l3=Label(Login_screen,text="Enter Password:",font=('Calibri',12))
    l3.grid(row=4,sticky=W) 
    global usr
    global fmail
    global pwd
    usr=StringVar()
    fmail=StringVar()
    pwd=StringVar()
    e1=Entry(Login_screen,text=usr,width=20)
    e1.grid(row=2,column=2)
    e2=Entry(Login_screen,text=fmail,width=20)
    e2.grid(row=3,column=2)
    e3=Entry(Login_screen,text=pwd,show='*',width=20)
    e3.grid(row=4,column=2)
    global notif2
    notif2=Label(Login_screen,font=('Calibri',12))
    notif2.grid(row=7,sticky=N)
    b1=Button(Login_screen,text="Login",command=finish_login,padx=30)
    b1.grid(row=5)

def finish_login():
    global a1
    a1=usr.get()
    a2=pwd.get()
    a3=fmail.get()
    if a1==a and a2==b and a3==d:
        notif2.config(fg="green",text="Login Successful")
        Login_screen.destroy()
        global acct_dashboard
        acct_dashboard=Toplevel(root)
        acct_dashboard.title("Account dashboard")
        Label(acct_dashboard,text="Select your choice from the given below:",font=('Calibri',12)).grid(row=0,sticky=N)
        Button(acct_dashboard,text="Book a ticket",command=book,padx=20).grid(row=2)
        Button(acct_dashboard,text="View booked tickets",padx=20).grid(row=3)
        Button(acct_dashboard,text="Logout",command=Logout,padx=20).grid(row=4)
    else:
        notif2.config(fg="red",text="Invalid username or password! Try again")

def Kantara():
    global Kantara_screen
    Kantara_screen=Toplevel(root)
    Kantara_screen.title("Kantara")
    l=Label(Kantara_screen,text="Select number of tickets:",font=('Çalibri',12))
    l.grid(row=0,sticky=N)
    n=IntVar()
    n.set(1) 
    global tickets   
    tickets= OptionMenu(Kantara_screen,n,1,2,3,4,5,6,7,8).grid(row=1) #Creates a menu box
    l=Label(Kantara_screen,text=n.get(),font=('Çalibri',12))
    l.grid(row=2,sticky=N)

def KGF_2():
    global KGF_2_screen
    KGF_2_screen=Toplevel(root)
    KGF_2_screen.title("KGF 2")
    l=Label(KGF_2_screen,text="Select number of tickets:",font=('Çalibri',12))
    l.grid(row=0,sticky=N)
    n=IntVar()
    n.set(1)  
    global tickets  
    tickets= OptionMenu(KGF_2_screen,n,1,2,3,4,5,6,7,8) #Creates a menu box
    l=Label(KGF_2_screen,text=n.get(),font=('Çalibri',12)).grid(row=1)
    l.grid(row=2,sticky=N)

def Jailer():
    global Jailer_screen
    Jailer_screen=Toplevel(root)
    Jailer_screen.title("Jailer")
    l=Label(Jailer_screen,text="Select number of tickets:",font=('Çalibri',12))
    l.grid(row=0,sticky=N)
    n=IntVar()
    n.set(1) 
    global tickets   
    tickets= OptionMenu(Jailer_screen,n,1,2,3,4,5,6,7,8).grid(row=1) #Creates a menu box
    l=Label(Jailer_screen,text=n.get(),font=('Çalibri',12))
    l.grid(row=2,sticky=N)

def Three_Idiots():
    global three_idiots_screen
    Three_Idiots_screen=Toplevel(root)
    Three_Idiots_screen.title("Three Idiots")
    l=Label(Three_Idiots_screen,text="Select number of tickets:",font=('Çalibri',12))
    l.grid(row=13,sticky=N)
    n=IntVar()
    n.set(1)  
    global tickets  
    tickets= OptionMenu(Three_Idiots_screen,n,1,2,3,4,5,6,7,8).grid(row=1) #Creates a menu box
    l=Label(Three_Idiots_screen,text=n.get(),font=('Çalibri',12))
    l.grid(row=2,sticky=N)

def Avengers_Endgame():
    global Avengers_Endgame_screen
    Avengers_Endgame_screen=Toplevel(root)
    Avengers_Endgame_screen.title("Avengers Endgame")
    l=Label(Avengers_Endgame_screen,text="Select number of tickets:",font=('Çalibri',12))
    l.grid(row=0,sticky=N)
    n=IntVar()
    n.set(1)   
    global tickets 
    tickets= OptionMenu(Avengers_Endgame_screen,n,1,2,3,4,5,6,7,8).grid(row=1) #Creates a menu box
    l=Label(Avengers_Endgame_screen,text=n.get(),font=('Çalibri',12))
    l.grid(row=2,sticky=N)

def Display():
    global Display_screen
    Display_screen=Toplevel(root)
    Display_screen.title("Display movies")
    l=Label(Display_screen,text="The Movies available are:",font=('Çalibri',12))
    l.grid(row=0,sticky=N)
    l=Label(Display_screen,text="Kantara",font=('Çalibri',12))
    l.grid(row=1,sticky=W)
    l=Label(Display_screen,text="KGF 2",font=('Çalibri',12))
    l.grid(row=2,sticky=W)
    l=Label(Display_screen,text="Jailer",font=('Çalibri',12))
    l.grid(row=3,sticky=W)
    l=Label(Display_screen,text="3 Idiots",font=('Çalibri',12))
    l.grid(row=4,sticky=W)
    l=Label(Display_screen,text="Avengers:Endgame",font=('Çalibri',12))
    l.grid(row=5,sticky=W)

def proceed_to_seat_selection(movie_name,num_tickets):
    global Proceed_screen
    Proceed_screen=Toplevel(root)
    Proceed_screen.title("Seat Selection")
    Label(Proceed_screen,text="Select your seats:",font=('Calibri', 12)).grid(row=0)

    # Create buttons for seat selection
    row_index=1
    col_index=0
    buttons=[]  # List to store references to the seat buttons
    selected_seats=set()  # Set to store selected seat numbers

    def toggle_seat(seat_number):
        nonlocal selected_seats
        if seat_number in selected_seats:
            buttons[seat_number-1].config(state='normal',bg='SystemButtonFace',command=lambda num=seat_number: toggle_seat(num))
            selected_seats.remove(seat_number)
        else:
            buttons[seat_number-1].config(state='disabled',bg='gray',command=lambda: None)
            selected_seats.add(seat_number)

    for i in range(64):
        seat_button=Button(Proceed_screen,text="{}".format(i+1),width=5,
                             command=lambda num=i+1: toggle_seat(num))
        seat_button.grid(row=row_index,column=col_index)
        buttons.append(seat_button)  # Store the button reference in the list
        col_index+=1
        if col_index==8:
            row_index+=1
            col_index=0

    def pay_now():
        if len(selected_seats)!=num_tickets:
            Label(Proceed_screen,text="Please select {} seats.".format(num_tickets),font=('Calibri', 12),
                  fg="red").grid(row=12)
        else:
            # Mock implementation of payment processing
            payment_gateway=PaymentGateway()
            if payment_gateway.process_payment(num_tickets*500):
                Label(Proceed_screen,text="Payment successful!,{} has been paid".format(num_tickets*500),font=('Calibri', 12),fg="green").grid(row=12)
                # Add code here to store the booking details or update a database
            else:
                Label(Proceed_screen,text="Payment failed.There was an error! Please try again", font=('Calibri', 12),
                      fg="red").grid(row=12)

    def cancel_selection():
        nonlocal selected_seats   # used for referring to a variable in the nearest outer scope
        for seat_number in selected_seats:
            buttons[seat_number-1].config(state='normal',bg='SystemButtonFace',command=lambda num=seat_number: toggle_seat(num))
        selected_seats=set()

    # Buttons for payment and cancellation
    Button(Proceed_screen,text="Pay Now",command=pay_now).grid(row=11, column=0)
    Button(Proceed_screen,text="Cancel",command=cancel_selection).grid(row=11, column=1)


def book():
    global Book_screen
    Book_screen = Toplevel(root)
    Book_screen.title("Bookings")
    Label(Book_screen, text=f"Logged in as {a1}", font=('Calibri', 12)).grid(row=0)
    Label(Book_screen, text="Select Movie:", font=('Calibri', 12)).grid(row=1)
    movie_var = StringVar()
    movie_var.set("Kantara")  # Default movie selection
    movie_options = ["Kantara", "KGF 2", "Jailer", "Three Idiots", "Avengers: Endgame"]
    movie_dropdown = OptionMenu(Book_screen, movie_var, *movie_options)
    movie_dropdown.grid(row=1, column=1)
    Label(Book_screen, text="Select number of tickets:", font=('Calibri', 12)).grid(row=2)
    num_tickets_var = IntVar()
    num_tickets_var.set(1)
    num_tickets_options = [i for i in range(1, 9)]  # 1 to 8 tickets
    num_tickets_dropdown = OptionMenu(Book_screen, num_tickets_var, *num_tickets_options)
    num_tickets_dropdown.grid(row=2, column=1)
    Label(Book_screen, text="Enter the date you want to watch it on:", font=('Calibri', 12)).grid(row=3)
    date_var = StringVar()
    tomorrow= date.today()+timedelta(days=1)
    date_var.set(tomorrow)
    date_options=[tomorrow+timedelta(days=i) for i in range(7)]
    date_dropdown = OptionMenu(Book_screen, date_var, *date_options)
    date_dropdown.grid(row=3, column=1)

    # Button to proceed to seat selection
    proceed_button = Button(Book_screen, text="Proceed to seat selection",command=lambda: proceed_to_seat_selection(movie_var.get(), 
                                               num_tickets_var.get())).grid(row=6)

def Logout():
    Logout_screen=Toplevel(root)
    Logout_screen.title("Log Out")
    Label(Logout_screen,text="Successfully Logged out",font=('Calibri',12)).grid(row=0)
    root.destroy()

def Exit():
    print("Successfully logged out")
    sys.exit()

myButton1=Button(root,text="Create user",padx=20,command=Create)
myButton1.pack()
myButton2=Button(root,text="Login",padx=20,command=Login)
myButton2.pack()
myButton3=Button(root,text="Display movies list",padx=20,command=Display)
myButton3.pack()
myButton4=Button(root,text="Exit",padx=20,command=Exit)
myButton4.pack()
root.mainloop()
