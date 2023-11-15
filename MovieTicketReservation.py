import tkinter
import pymongo 
import getpass
import string
import os

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["User_Details"]
collection = mydb["collection"]
movies = mydb["Movies"]
dict = {}
dict1 = {}
uname = ''
pass5 = ''
M_name=''

def welcome():
    print("Welcome to Movie Ticket Reservation System")

def create_user():
    user = input("Please enter your name: ")
    password = input("Please enter your password here: ")
    password2 = input("Please enter your password again here: ")
    if password == password2 :
        c2 = encrypt(password)
        mydb.collection.insert_one({'name':user,'password':c2})
        collection.update_one({"name":uname},{'$set':{"movie_reserved": '' }})
        print("User Created Successfully")
    else :
        print("Passwords do not match, please try again.")

def encrypt(original_text):
    T1 = original_text
    chars=' '+ string.ascii_letters+string.digits+string.punctuation
    chars=list(chars)
    key = ['R', '#', 'M', '<', '[', 'n', 'g', '3', '%', 'D', 's', 'U', 'e', '{', '>', '}', '&', 'N', '/', '0', '4', '7', '6', 'E', '`', ';', 'I', 'v', '*', 'f', 'h', '\\', '~', 'X', 'A', 'd', 'S', '?', '^', 'u', 'Y', 'z', 'C', 'k', ',', 'J', 'r', 'x', '9', 'o', '$', "'", '"', 'O', 'q', 'm', 'c', '!', '.', 'j', 'a', 'b', 'K', 't', '_', 'l', '|', 'w', '1', 'P', '@', 'T', ' ', 'G', 'y', '=', 'Z', '5', 'B', 'L', ']', ')', '(', '8', 'Q', '2', ':', 'V', 'W', 'p', 'i', '+', 'H', 'F', '-']
    enc = ''
    for letter in T1 :
        index = chars.index(letter)
        enc += key[index]
    return enc

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

def book():
    print("Please select number corresponding to the movie from the options given below to book a seat or 6 to exit: ")
    movie_list = ["Kanthaara","KGF","Modiji","Motte","ChakDeIndia"]
    print("The movies available are: ")
    for i in range(len(movie_list)):
        print((i+1),".",movie_list[i])
    try:
            ch = int(input("Enter your choice (1/2/3/4/5/6) here: "))
            if ch!=6 :
                option = movie_list[ch-1]
                #print(movies.find_one({'Name': option}))
                M_name = option
            if 5>=ch>=1:
                reserve(option)
            elif ch==6:
                print("Logged out successfully")
                exit()
            else:
                print("Please enter a valid number from the given options only")
    except ValueError:
            print("Invalid Input! Please Enter a Number.")

def reserve(movie_name): #MongoDB new database consisting of movie names is to be made and user details after booking like ticket number and should be updated in the collection.
    global M_name,uname
    M_name = movie_name
    print(M_name)
    seats_available = 0
    x  = movies.find_one({"Name":f'{movie_name}'},{"_id":0,"Name":0})
    # print(x)
    os.system("cls")
    print("Seats Available  = ",x['seats_available'])
    collection.update_one({"name":uname},{'$set':{"movie_reserved":M_name}})
    seat_book()

def seat_book():
    global uname,pass5
    # q1 = mydb.collection.find_one({'name':uname})
    # print(q1)
    total_seats = 64
    seat_layout = []
    k=1
    x = movies.find_one({'Name':M_name})
    for i in range(1,9):
        row = []
        for j in range(1,9):
                for z in x['reserved_seats']:
                    if k in z :
                        row.append("Booked Seat")
                        k+=1
                    else:
                        row.append(k)
                        k+=1
        seat_layout.append(row)
    for ele in seat_layout:
        print(ele)
    while True:
        num_of_seats = int(input("How many seats would you like to reserve? "))
        if num_of_seats>total_seats:
                print("Please enter seats within available limit.")
        else:
            break
    print("Enter Seat Numbers You Want To Reserve: ")
    num_seats=[]
    for i in range(num_of_seats):
        x  = int(input())
        while x<1 or x>64:
            print("Wrong Seat Number Enter 1-64 ONLY: ")    
            x = int(input())
        else :
            num_seats.append(x)     
    print("Seats for reserving: ",num_seats)
    #transaction(num_of_seats)
    print("Reserving Seats")
    collection.update_one({'name':uname},{"$set" : {'Reserved' : num_seats}})
    print("Seats Reserved")
    y = movies.find_one({'Name':M_name})
    #print(y)
    movies.update_one({'Name':M_name},{'$inc':{'seats_available' : -(num_of_seats)}})
    movies.update_one({'Name':M_name},{'$push':{'reserved_seats': num_seats}})

def view_bookings():
    global uname
    try :
        x = movies.find_one({'Name':M_name})
        y = collection.find_one({'name':uname})
        print(y)
    except KeyError :
         print(f"No Seats Booked By {uname}")
def transaction():
     return None
def login_user():
    #echeck = input("Enter Email you signed Up with: ")
    user = input("Please enter your name: ")
    user = user.lstrip().rstrip()
    password = encrypt((getpass.getpass("Please enter your password here: ")).lstrip().rstrip()) 
    pwd = (password)
    query = {'name':user}
    x = mydb.collection.find_one(query,{"_id":0})
    try :
        if x['password']==pwd:
            global uname,pass5
            uname = user
            pass5 = pwd
            os.system("cls")
            print("Login Succesful ")
            after_login()
    except TypeError:
        print("User doesnt exist or Credentials do not match ")
def display_movies():
    movie_list = ["Kantaara","KGF","Modiji","Motte","ChakDeIndia"]
    print("The movies available are: ")
    for i in range(len(movie_list)):
            print((i+1),".",movie_list[i])

def main_menu():
    while True:  
        welcome()
        print("Choose your option from the below: ")
        print("1. Create a new user ")
        print("2. Login ")
        print("3. Display Movies List ")
        print("4. Exit ")
        try: #remove try catch after gui merge
            ch = int(input("Enter your choice (1/2/3/4) here: "))
            if ch == 1:
                create_user()
            elif ch == 2:
                login_user()
            elif ch==3:
                display_movies()
            elif ch==4:
                print("Thanks for using our Reservation System!")
                exit()
            else:
                print("Please enter a valid number from the given options only")
        except ValueError:
            print("Invalid Input! Please Enter a Number.")
            
main_menu()
myclient.close()
