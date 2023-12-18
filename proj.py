from tkinter import *
import sys,requi,datetime,random,string
from datetime import date,timedelta
from PIL import Image, ImageDraw, ImageFont


root=Tk()
root.geometry("2000x1000")
MyLabel4=Label(root,text="\n").pack()
root.title("Welcome to Bookito: A one stop solution to ticket booking")
MyLabel3=Label(root,text="\n").pack()
MyLabel=Label(root,text="Welcome to Bookito",font=('Verdana',25,'bold')).pack()
MyLabel3=Label(root,text="\n").pack()
MyLabel1=Label(root,text="Follow the below instructions for smooth user experience",font=('Helvetica',20,'bold')).pack()
MyLabel3=Label(root,text="\n").pack()
MyLabel2 = Label(root,text="Please select one of the following options to proceed ",font=('Helvetica',20,'bold')).pack()
MyLabel3=Label(root,text="\n").pack()
MyLabel3=Label(root,text="\n").pack()

def Create():
    global Create_screen
    Create_screen=Toplevel(root)
    Create_screen.geometry("400x350")
    Create_screen.title("Create user")
    l=Label(Create_screen,text="Create your account here",font=('Çalibri',12,'bold'))
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
    b1=Button(Create_screen,text="Create",command=finish_create,padx=30,font=('Georgia',10,'bold'))
    b1.grid(row=9)
    global notif1
    notif1=Label(Create_screen,font=('Calibri',12))
    notif1.grid(row=10,sticky=N)


def finish_create():
    global a
    global b
    global c
    global d
    global e,M_Reserved
    a=user.get()                                                                #Username
    b=password.get()                                                            #Pass1
    c=password2.get()                                                           #Pass2
    d=mail.get()                                                                #Email1
    e=mail2.get()                                                               #Email2
    if b==c and d.endswith("@gmail.com") and d==e:
        #updates new user in db
        date = requi.dat
        M_Reserved={}
        c2 = requi.encrypt(b)
        dic = {date:M_Reserved}
        requi.mydb.collection.insert_one({'name':a,'password':c2,'email':e})
        requi.collection.update_one({"name":a},{'$set':{"movie_reserved": dic }})
        requi.collection.update_one({"name":a},{'$set':{"book_count": 0 }})   
        #updated db    
        notif1.config(fg="green",text="User created Successfully")
        Create_screen.after(1000,Create_screen.destroy)
    else:
        notif1.config(fg="red",text="Either password entered or email doesnt match the criteria, please try again.")
        
def Login():
    global Login_screen
    Login_screen=Toplevel(root)
    Login_screen.title("Login page")
    l=Label(Login_screen,text="Welcome to the login page",font=('Çalibri',12,'bold'))
    l.grid(row=0,sticky=N)
    l1=Label(Login_screen,text="Enter Username:",font=('Çalibri',12))
    l1.grid(row=2,sticky=W)
    l2=Label(Login_screen,text="Enter Email you signed up with:",font=('Çalibri',12))
    l2.grid(row=3,sticky=W)
    l3=Label(Login_screen,text="Enter Password:",font=('Calibri',12))
    l3.grid(row=4,sticky=W) 
    global usr # usr username
    global fmail #fmail email
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
    b1=Button(Login_screen,text="Login",command=finish_login,padx=30,font=('Georgia',10,'bold'))
    b1.grid(row=5)

def finish_login():
    global a1,a3
    a1=usr.get()
    a2=pwd.get()
    a3=fmail.get()  
    if a1=="Admin" and a2=="sairam" and a3=="sairam@gmail.com":
        notif2.config(fg="green",text="Welcome, Admin")
        Login_screen.destroy()
        global admin_dash
        admin_dash=Toplevel(root)
        admin_dash.title("Admin Dashboard")
        Label(admin_dash,text="Logged in as admin",font=('Calibri',12)).grid(row=0)
        Button(admin_dash,text="Show Movies",command=Display,padx=20,font=('Georgia',10,'bold')).grid(row=2)
        Button(admin_dash,text="Add movies",command=add_mov,padx=20,font=('Georgia',10,'bold')).grid(row=3)
        Button(admin_dash,text="Delete movies",command=del_mov,padx=20,font=('Georgia',10,'bold')).grid(row=4)
        Button(admin_dash,text="Logout as admin",command=Exit,padx=20).grid(row=5)
    else :  
        x = requi.mydb.collection.find_one({'name':a1},{"_id":0})
        b = x["password"]
        d = x["email"]
        encpwd=requi.encrypt(a2)   

        if a1==x["name"] and encpwd==b and a3==d:
            notif2.config(fg="green",text="Login Successful")
            Login_screen.destroy()
            acct_dashboard=Toplevel(root)
            acct_dashboard.title("Account dashboard")
            Label(acct_dashboard,text="Select your choice from the given below:",font=('Calibri',12)).grid(row=0,sticky=N)
            Button(acct_dashboard,text="Book a ticket",command=book,padx=20,font=('Georgia',10,'bold')).grid(row=2)
            Button(acct_dashboard,text="View booked tickets",command=view_bookings,padx=20,font=('Georgia',10,'bold')).grid(row=3)#make viewbooked
            Button(acct_dashboard,text="Logout",command=Logout,padx=20,font=('Georgia',10,'bold')).grid(row=4)        
        else:
            notif2.config(fg="red",text="Invalid username or password! Try again")
    

def view_bookings():
    global date_var,viewbook,z
    y = requi.collection.find_one({'name':a1})
    viewbook=Toplevel(root)
    viewbook.title("View Bookings")
    Label(viewbook,text="Select the Date You want to check your movies for ",font=('Çalibri',12,'bold')).grid(row=0)
    try:
        if y['movie_reserved']=="":
            print(f"No Seats Booked By {a1}")
        else:
            date_var = StringVar()
            tomorrow= date.today()+timedelta(days=1)
            date_options=[tomorrow+timedelta(days=i) for i in range(7)]
            date_dropdown = OptionMenu(viewbook, date_var, *date_options,command=date_var_select)
            date_dropdown.grid(row=3, column=1)
            z=y['movie_reserved']
            Button(viewbook,text="View Seats",command=view_bookings_final,padx=20,font=('Georgia',10,'bold')).grid(row=4)
    except KeyError:
        Label(viewbook,text=f"No Seats Booked by {a1}",font=('Çalibri',12)).grid(row=4)
        
def view_bookings_final():
    global book_date
    selected_date=str(date_var.get())
    l1 = ""
    book_date = selected_date.split("-")
    for i in book_date[::-1]:
        l1 += i + '/'
    l1 = l1[0:-1]
    book_date = l1
    try:
        rec = str(z[book_date])
        Label(viewbook,text=f"Seats Booked by {a1} are {rec[1:-1]}",font=('Çalibri',12)).grid(row=6)
    except KeyError:
        Label(viewbook,text=f"No Seats Booked by {a1}",font=('Çalibri',12)).grid(row=6)
            
def mov():
        admin_mov=Toplevel(root)
        admin_mov.title("Display movies")
        for i in movie_options:
            Label(admin_mov,text=i,font=('Çalibri',12)).grid(row=movie_options.index(i)+1)

def add_mov():
    global ad_mov
    ad_mov=Toplevel(root)
    ad_mov.title("Add movies")
    Label(ad_mov,text="Add movies here",font=('Çalibri',12)).grid(row=0)
    Label(ad_mov,text="Enter the movie u want to add:",font=('Çalibri',12)).grid(row=2,column=0)
    global x 
    x=StringVar()
    Entry(ad_mov,text=x,width=20).grid(row=2,column=1)
    global movi
    Button(ad_mov,text="Add",padx=20,command=add_here,font=('Georgia',10,'bold')).grid(row=4)


def del_mov():
    global dell_mov
    dell_mov=Toplevel(root)
    dell_mov.title("Delete movies")
    Label(dell_mov,text="Delete movies here")
    Label(dell_mov,text="Enter the movie u want to delete:",font=('Çalibri',12)).grid(row=2,column=0)
    global y 
    y=StringVar()
    Entry(dell_mov,text=y,width=20).grid(row=2,column=1)
    global m_del
    Button(dell_mov,text="Delete",padx=20,command=delete_here,font=('Georgia',10,'bold')).grid(row=4)

def delete_here():
    m_del=y.get()
    if m_del in movie_options:
            requi.movies.delete_one({"Name":m_del})
            Label(dell_mov,fg="green",text=f"{m_del} has been removed").grid(row=5)
    else :  
            Label(dell_mov,fg="red",text=f"{m_del} does not exist").grid(row=5)

def add_here():
    movi=x.get()
    requi.movies.insert_one({'Name':movi ,"seats_available" : {} })    
    Label(ad_mov,fg="green",text=f"{movi} has been added").grid(row=5)

def Display():
    global Display_screen
    global movie_options
    Display_screen=Toplevel(root)
    Display_screen.title("Display movies")
    l=Label(Display_screen,text="The Movies available are:",font=('Çalibri',12,'bold'))
    l.grid(row=0,sticky=N)
    movie_options=[]
    buffer_movie=requi.movies.find({},{"_id":0,"seats_available":0})                    #Accessing db and showing moves in db for dropdown
    for i in buffer_movie:
        for key in i:
            movie_options.append(i[key])
    for i in range(len(movie_options)):
        l=Label(Display_screen,text=movie_options[i],font=('Çalibri',12))
        l.grid(row=i+1,sticky=W)
        
def proceed_to_seat_selection(movie_name,num_tickets):
    global Proceed_screen,m_name,selected_seats
    Proceed_screen=Toplevel(root)
    Proceed_screen.title("Seat Selection")
    Label(Proceed_screen,text="Select your seats:",font=('Calibri', 12)).grid(row=0)
    row_index=1
    col_index=0
    buttons=[]  # List to store references to the seat buttons
    selected_seats=[]  # Set to store selected seat numbers
    
    def check(y):
        global book_date,booked_seats
        global selected_seats
        x = requi.movies.find_one({'Name':m_name})
        seats_available= x["seats_available"]               #Gives all bookings done, which date they are done and the seats which were booked
        try : 
            global seats_day
            seats_day=seats_available[book_date]  
        except KeyError:
            seats_available[book_date] = [[0]]
            seats_day = seats_available[book_date]
        s=seats_day
        l1 =[]
        for i in range(len(s)) :
            for j in s[i]:
                l1.append(j)
        booked_seats=l1
        if y in l1 :
            return 'RS'
        else :
            return y
    seats = list(map(check,list(i for i in range(1,65))))

    def toggle_seat(seat_number):
        global selected_seats
        selected_seats=list(selected_seats)
        if seat_number in selected_seats:
            buttons[seat_number-1].config(state='normal',bg='SystemButtonFace',command=lambda num=seat_number: toggle_seat(num))
            selected_seats.remove(seat_number)
        else:
            buttons[seat_number-1].config(state='disabled',bg='gray',command=lambda: None)
            selected_seats.append(seat_number)
    for i in range(len(seats)):
        if seats[i] == 'RS': #doesnt allow for rebook
            seat_button=Button(Proceed_screen,text=f"{seats[i]}",width=5,
                                command=lambda num=i+1: toggle_seat(num),state = 'disabled')
        else :
                seat_button=Button(Proceed_screen,text=f"{seats[i]}",width=5,
                                command=lambda num=i+1: toggle_seat(num),state = 'normal')    
        seat_button.grid(row=row_index,column=col_index)
        buttons.append(seat_button)  # Store the button reference in the list
        col_index+=1
        if col_index==8:
            row_index+=1
            col_index=0
            
    def pay_now():
        if len(selected_seats)!=num_tickets:
            Label(Proceed_screen,text=f"Please select {num_tickets} seats.",font=('Calibri', 12),
                  fg="red").grid(row=12)
        else:
            pay(num_tickets)
            
    def cancel_selection():
        global selected_seats   # used for referring to a variable in the nearest outer scope
        for seat_number in selected_seats:
            buttons[seat_number-1].config(state='normal',bg='SystemButtonFace',command=lambda num=seat_number: toggle_seat(num))
        selected_seats=set()
    # Buttons for payment and cancellation
    Button(Proceed_screen,text="Pay Now",command=pay_now,font=('Georgia',10,'bold')).grid(row=11, column=0)
    Button(Proceed_screen,text="Cancel",command=cancel_selection,font=('Georgia',10,'bold')).grid(row=11, column=1)
    
def book():
    global Book_screen,book_date,num_seats
    global m_name,movie_options                 #not accessing data from drop down
    movie_options = []
    Book_screen = Toplevel(root)
    Book_screen.title("Bookings")
    Label(Book_screen, text=f"Logged in as {a1}", font=('Calibri', 12)).grid(row=0)
    Label(Book_screen, text="Select Movie:", font=('Calibri', 12)).grid(row=1)
    global movie_var
    movie_var = StringVar()
    buffer_movie=requi.movies.find({},{"_id":0,"seats_available":0})                    #Accessing db and showing moves in db for dropdown
    for i in buffer_movie:
        for key in i:
            movie_options.append(i[key])
    movie_dropdown = OptionMenu(Book_screen, movie_var, *movie_options,command=movie_name_select)
    movie_dropdown.grid(row=1, column=1)
    Label(Book_screen, text="Select number of tickets:", font=('Calibri', 12)).grid(row=2)
    global num_tickets_var
    num_tickets_var = IntVar()
    num_tickets_options = [i for i in range(1, 9)]  # 1 to 8 tickets
    num_tickets_dropdown = OptionMenu(Book_screen, num_tickets_var, *num_tickets_options,command=num_tickets_select)
    num_tickets_dropdown.grid(row=2, column=1)
    Label(Book_screen, text="Enter the date you want to watch it on:", font=('Calibri', 12)).grid(row=3)
    global date_var
    date_var = StringVar()
    tomorrow= date.today()+timedelta(days=1)
    date_options=[tomorrow+timedelta(days=i) for i in range(7)]
    date_dropdown = OptionMenu(Book_screen, date_var, *date_options,command=date_var_select)
    date_dropdown.grid(row=3, column=1)
    proceed_button = Button(Book_screen, text="Proceed to seat selection",command=lambda: proceed_to_seat_selection(m_name, 
                                               num_seats,font=('Georgia',10,'bold'))).grid(row=6)
def movie_name_select(_=None):
    global m_name
    m_name = movie_var.get()
    
def num_tickets_select(_=None):
    global num_seats
    num_seats = num_tickets_var.get()
    
def date_var_select(_=None):
    global book_date
    book_date = date_var.get()
    l1 = ""
    book_date = book_date.split("-")
    for i in book_date[::-1]:
        l1 += i + '/'
    l1 = l1[0:-1]
    book_date = l1

def Logout():
    Logout_screen=Toplevel(root)
    Logout_screen.title("Log Out")
    Label(Logout_screen,text="Successfully Logged out",font=('Calibri',12)).grid(row=0)
    root.destroy()

def Exit():
    print("Successfully logged out")
    sys.exit()

def update_db():
        global a1,book_date,selected_seats
        num_seats = selected_seats
        uname=a1
        dat=book_date
        M_name = m_name
        y = requi.collection.find_one({"name":uname})
        d = y["movie_reserved"]
        try :
            movie_seats=d[dat]
        except KeyError :
            d[dat]={M_name:[]}
            movie_seats=d[dat]
        seat_numbers=list()
        try :
            seat_numbers=movie_seats[M_name]
        except KeyError:
            movie_seats[M_name]=[]    
        for i in num_seats:
                seat_numbers.append(i)
        movie_seats[M_name]=seat_numbers
        d[dat] = movie_seats
        requi.collection.update_one({"name":(uname)},{'$set':{"movie_reserved":d}})  
        a = requi.movies.find_one({"Name":M_name})
        b = a["seats_available"]
        try :
            c = b[book_date]
        except KeyError:
            b[book_date]=[]
            c = b[book_date]
        c.append(num_seats)
        b[book_date]=c
        y = requi.movies.find_one({'Name':M_name})                                          
        requi.movies.update_one({'Name':M_name},{'$set':{'seats_available' : b}})
        requi.collection.update_one({"name":uname},{'$inc':{"book_count": 1 }})
        Label(ask_screen,text=f"Tickets Successfully booked close all windows and relogin to check booked seats",font=('Calibri', 12),fg="green").grid(row=3)
    
def pay(seat_num):
    ticket_price = 500
    global total_cost
    total_cost = seat_num * ticket_price
    x = requi.collection.find_one({'name':a1})

    global ask_screen
    ask_screen=Toplevel(root)
    ask_screen.title("Confirmation")
    try:
        if x["book_count"]>=5 and x["book_count"]<15:
            total_cost = 0.95*total_cost
            Label(ask_screen,text="5% Discount applied ",font=('Calibri', 12),fg="green").grid(row=1)             
        elif x["book_count"]>=15:
            total_cost = 0.8*total_cost
            Label(ask_screen,text="20% Discount applied ",font=('Calibri', 12),fg="green").grid(row=2) 
    except KeyError:
        pass
    Label(ask_screen,text=f"Amount Payable is {total_cost} ",font=('Calibri', 12),fg="green").grid(row=0)
    Button(ask_screen,text="Yes",command=generate_random_transaction,font=('Georgia',10,'bold')).grid(row=1)
    Button(ask_screen,text="No",command=No,font=('Georgia',10,'bold')).grid(row=2)
     
def ticket_gen():    #Change from seatbook to gui
    ticket_width = 400
    ticket_height = 500
    ticket_color = "white"
    ticket = Image.new("RGB",(ticket_width, ticket_height), ticket_color)
    draw = ImageDraw.Draw(ticket)
    text_color = "black"
    font = ImageFont.truetype("arial.ttf", 20) 
    user = a1
    date = book_date
    movie_name = m_name
    email = a3
    seat_number = ''
    for i in list(selected_seats):
        seat_number += str(i)+ ','
    seat_number=seat_number[:-1]
    ticket_info = f"----------- Welcome to Bookito ----------\n----------- Reservation System ----------\n\nTicket Number : {transaction_data['transaction_id']}\nCustomer Name :{user}\nEmail : {email} \nDate : {date}\n\n============================\n\nMovie: {movie_name}\nSeat: {seat_number}\n\n============================\n\n       Thank You For Choosing Us \n               Enjoy Your Movie"
    text_position = (20, 50) 
    draw.text(text_position, ticket_info, fill=text_color, font=font)
    ticket.save("movie_ticket.png") 

def No():
    Label(ask_screen,text="Payment Cancelled", font=('Calibri', 0),
                      fg="red").grid(row=3)
    
def generate_random_transaction():
    global transaction_data
    transaction_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    amount = total_cost
    transaction_data = {"transaction_id": transaction_id,"amount": amount,"transaction_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"transaction_status":True}
    if transaction_data["transaction_status"]==True:
                ticket_gen()
                update_db()
                # Add code here to store the booking details or update a database
    else:
        Label(ask_screen,text="Payment failed.There was an error! Please try again", font=('Calibri', 12),
                fg="red").grid(row=12)

myButton1=Button(root,text="Create user",padx=35,command=Create,font=('Georgia',10,'bold'))
myButton1.pack()
MyLabel3=Label(root,text="\n").pack()
myButton2=Button(root,text="Login",padx=40,command=Login,font=('Georgia',10,'bold'))
myButton2.pack()
MyLabel3=Label(root,text="\n").pack()
myButton3=Button(root,text="Display movies list",padx=15,command=Display,font=('Georgia',10,'bold'))
myButton3.pack()
MyLabel3=Label(root,text="\n").pack()
myButton4=Button(root,text="Exit",padx=40,command=Exit,font=('Georgia',10,'bold'))
myButton4.pack()
MyLabel3=Label(root,text="\n").pack()
root.mainloop()
