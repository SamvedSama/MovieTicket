from tkinter import *
import sys,requi,reserve,login,ticket,admin,datetime,random,string
from datetime import date,timedelta


#Creating a user field wiht book count and all that shit 
#Movie database in gui
#

class PaymentGateway:
    def process_payment(self, amount):
        # Mock implementation for testing purposes
        # In a real scenario, integrate with a payment gateway API
        # Here, you can assume the payment is successful if the card number starts with '4' (Visa)
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
    global e,M_Reserved
    a=user.get()                    #Username
    b=password.get()                #Pass1
    c=password2.get()               #Pass2
    d=mail.get()                    #Email1
    e=mail2.get()                   #Email2
    if b==c and d.endswith("@gmail.com") and d==e:
        #updates new user in db
        date = requi.dat
        M_Reserved={}
        c2 = requi.encrypt(password)
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
    l=Label(Login_screen,text="Welcome to the login page",font=('Çalibri',12))
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
    b1=Button(Login_screen,text="Login",command=finish_login,padx=30)
    b1.grid(row=5)

def finish_login():
    global a1,a3
    a1=usr.get()
    a2=pwd.get()
    a3=fmail.get()
    x = requi.mydb.collection.find_one({'name':a1},{"_id":0})
    b = x["password"]
    d = x["email"]
    if a1==[x["name"]] and a2==b and a3==d:
        notif2.config(fg="green",text="Login Successful")
        Login_screen.destroy()
        global acct_dashboard
        acct_dashboard=Toplevel(root)
        acct_dashboard.title("Account dashboard")
        Label(acct_dashboard,text="Select your choice from the given below:",font=('Calibri',12)).grid(row=0,sticky=N)
        Button(acct_dashboard,text="Book a ticket",command=book,padx=20).grid(row=2)
        Button(acct_dashboard,text="View booked tickets",padx=20).grid(row=3)#make viewbooked
        Button(acct_dashboard,text="Logout",command=Logout,padx=20).grid(row=4)
    elif a1=="Admin" and a2=='':
        admin.admin()
    else:
        notif2.config(fg="red",text="Invalid username or password! Try again")

def Display():
    global Display_screen
    requi.os.system("cls")
    global movie_options
    Display_screen=Toplevel(root)
    Display_screen.title("Display movies")
    l=Label(Display_screen,text="The Movies available are:",font=('Çalibri',12))
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

    # Create buttons for seat selection
    row_index=1
    col_index=0
    buttons=[]  # List to store references to the seat buttons
    selected_seats=[]  # Set to store selected seat numbers

    def check(y):
        global m_name,book_date
        global selected_seats
        x = requi.movies.find_one({'Name':m_name})
        seats_available= x["seats_available"]
        try : 
            global seats_day
            seats_day=seats_available[book_date]  
        except KeyError:
            seats_available[book_date] = [[0]]
            seats_day = seats_available[book_date]
        s=seats_day
        global booked_seats
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
        global num_seats
        if len(selected_seats)!=num_tickets:
            Label(Proceed_screen,text=f"Please select {num_tickets} seats.",font=('Calibri', 12),
                  fg="red").grid(row=12)
        else:
            # Mock implementation of payment processing
            # payment_gateway=PaymentGateway()
            payment_gateway = pay(num_seats)
            if payment_gateway["transaction_status"]==True:
                update_db()
                # Add code here to store the booking details or update a database
            else:
                Label(Proceed_screen,text="Payment failed.There was an error! Please try again", font=('Calibri', 12),
                      fg="red").grid(row=12)

    def cancel_selection():
        global selected_seats   # used for referring to a variable in the nearest outer scope
        for seat_number in selected_seats:
            buttons[seat_number-1].config(state='normal',bg='SystemButtonFace',command=lambda num=seat_number: toggle_seat(num))
        selected_seats=set()

    # Buttons for payment and cancellation
    Button(Proceed_screen,text="Pay Now",command=pay_now).grid(row=11, column=0)
    Button(Proceed_screen,text="Cancel",command=cancel_selection).grid(row=11, column=1)


def book():
    global Book_screen,book_date,num_seats
    global m_name,movie_options
    movie_options = []
    Book_screen = Toplevel(root)
    Book_screen.title("Bookings")
    Label(Book_screen, text=f"Logged in as {a1}", font=('Calibri', 12)).grid(row=0)
    Label(Book_screen, text="Select Movie:", font=('Calibri', 12)).grid(row=1)
    movie_var = StringVar()
    buffer_movie=requi.movies.find({},{"_id":0,"seats_available":0})                    #Accessing db and showing moves in db for dropdown
    for i in buffer_movie:
        for key in i:
            movie_options.append(i[key])
    movie_var.set(movie_options[0])
    movie_dropdown = OptionMenu(Book_screen, movie_var, *movie_options)
    movie_dropdown.grid(row=1, column=1)
    m_name = movie_var.get()    #User movie selection
    Label(Book_screen, text="Select number of tickets:", font=('Calibri', 12)).grid(row=2)
    num_tickets_var = IntVar()
    num_tickets_var.set(1)
    
    num_tickets_options = [i for i in range(1, 9)]  # 1 to 8 tickets
    num_tickets_dropdown = OptionMenu(Book_screen, num_tickets_var, *num_tickets_options)
    num_tickets_dropdown.grid(row=2, column=1)
    num_seats = num_tickets_var.get()
    Label(Book_screen, text="Enter the date you want to watch it on:", font=('Calibri', 12)).grid(row=3)
    date_var = StringVar()
    tomorrow= date.today()+timedelta(days=1)
    date_var.set(tomorrow)
    date_options=[tomorrow+timedelta(days=i) for i in range(7)]
    date_dropdown = OptionMenu(Book_screen, date_var, *date_options)
    date_dropdown.grid(row=3, column=1)
    book_date = date_var.get()
    l1 = ""
    book_date = book_date.split("-")
    for i in book_date[::-1]:
        l1 += i + '/'
    l1 = l1[0:-1]
    book_date = l1
    


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
def update_db():
        global a1,book_date,m_name,selected_seats
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
        ticket.ticket_gen()
        print("Seats Reserved")
        a = requi.movies.find_one({"Name":M_name})
        b = a["seats_available"]
        try :
            c = b[login.date]
        except KeyError:
            b[login.date]=[]
            c = b[login.date]
        c.append(num_seats)
        b[login.date]=c
        y = requi.movies.find_one({'Name':M_name})                                          
        requi.movies.update_one({'Name':M_name},{'$set':{'seats_available' : b}})
        requi.collection.update_one({"name":uname},{'$inc':{"book_count": 1 }})
def pay(seat_num):
    ticket_price = 500
    global total_cost,status
    total_cost = seat_num * ticket_price
    x = requi.collection.find_one({'name':login.uname})
    try:
        if x["book_count"]>=5 and x["book_count"]<15:
            total_cost = 0.95*total_cost
            Label(Proceed_screen,text="5% Discount applied ",font=('Calibri', 12),fg="green").grid(row=12)             
        elif x["book_count"]>=15:
            total_cost = 0.8*total_cost
            Label(Proceed_screen,text="20% Discount applied ",font=('Calibri', 12),fg="green").grid(row=12) 
    except KeyError:
        pass
    
    #INSERT RADIO BUTTON BS

    Label(Proceed_screen,text=f"Amount Payable is {total_cost} ",font=('Calibri', 12),fg="green").grid(row=12) 
    
    
    print("Proceed with payment ?(Y/N/Yes/No) ")
    choice=input()
    if choice.lower() in "yyes":
        status=True
    else:
        status=False
    return generate_random_transaction()




def generate_random_transaction():
    global status
    transaction_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    amount = total_cost
    transaction_data = {"transaction_id": transaction_id,"amount": amount,"transaction_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"transaction_status":status}
    return transaction_data


myButton1=Button(root,text="Create user",padx=20,command=Create)
myButton1.pack()
myButton2=Button(root,text="Login",padx=20,command=Login)
myButton2.pack()
myButton3=Button(root,text="Display movies list",padx=20,command=Display)
myButton3.pack()
myButton4=Button(root,text="Exit",padx=20,command=Exit)
myButton4.pack()
root.mainloop()
