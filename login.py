import requi,reserve,datetime

def login_users():
    echeck = input("Enter Email you signed Up with: ")
    user = input("Please enter your name: ").lstrip().rstrip()
    pwd = requi.encrypt((requi.getpass.getpass("Please enter your password here: ")).lstrip().rstrip()) 
    query = {'name':user}
    x = requi.mydb.collection.find_one(query,{"_id":0})
    try:
        if x['password']==pwd and echeck==x["email"]:
            global uname,pass5
            uname = user
            pass5 = pwd
            requi.os.system("cls")
            print("Login Succesful")
            after_login()
        else:
            print("\n\tIncorrect Password! Try Again.")
    except TypeError:
       print("User doesnt exist or Credentials do not match ")

def after_login():
    while True:
        print("Select your choice from the given below: ")
        print("1.Book a Ticket" )
        print("2.View Booked tickets" )
        print("3.Logout" )
        try:
            ch = int(input("Enter your choice (1/2/3) here: "))
            if ch == 1:
                book()
            elif ch==2:
                view_bookings()
            elif ch==3:
                global uname,pass5
                uname = ''
                pass5 = ''
                print("Successfully logged out.")
                exit()
            else:
                print("Please enter a valid number from the given options only")
        except ValueError:
            print("Invalid Input! Please Enter a Number.")
date = None
def book():
    global uname,date
    requi.os.system("cls")                                #Insert date of booking
    print(f"Logged in as {uname}")
    print("Enter a date to book movies (book before midight for tomorrows show )")
    date = can_i_get_a_date()
    # Date only after 24 hours so if 3 todays date allow only 4 onwards
    print("Please select number corresponding to the movie from the options given below to book a seat or 6 to exit: ")
    movie_list = ["Kanthaara","KGF","Kingsman","Chain Kuli Ki Mainkuli","Chak De India"]
    print("The movies available are: ")
    for i in range(len(movie_list)):
        print((i+1),".",movie_list[i])
    try:
        ch = int(input("Enter your choice (1/2/3/4/5/6) here: "))
        if ch!=6 :
            option = movie_list[ch-1]
        if 5>=ch>=1:
            reserve.reserve(option)
        elif ch==6:
            print("Logged out successfully")
            exit()
        else:
            print("Please enter a valid number from the given options only")
    except ValueError:
            print("Invalid Input! Please Enter a Number.")

def view_bookings():
    global uname,date
    requi.os.system("cls")
    y = requi.collection.find_one({'name':uname})
    try:
        if y['movie_reserved']=="":
            print(f"No Seats Booked By {uname}")
        else:
            print("Enter Date to see Bookings")
            date=can_i_get_a_date()
            z=y['movie_reserved']
            print(f"Movie reserved by {uname} is {z[date]}")
    except KeyError:
        print(f"No Seats Booked by {uname}")
     
def display_movies():
    requi.os.system("cls")
    movie_list = ["Kanthaara","KGF","Kingsman","Chain Kuli Ki Mainkuli","Chak De India"]
    print("The movies available are: ")
    for i in range(len(movie_list)):
            print((i+1),".",movie_list[i])

def can_i_get_a_date():
    dat = input('Enter a date formatted as YYYY-MM-DD: ').split('-')
    if datetime.datetime(int(dat[0]),int(dat[1]),int(dat[2])) >= datetime.datetime.today():
            l1=''
            global date 
            for i in dat[::-1]:
                l1 += i + '/'
            l1 = l1[0:-1]
            date = l1
            return l1
    else :
        print("Sorry you cannot book tickets for past dates")
        return can_i_get_a_date()