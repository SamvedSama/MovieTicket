import tkinter
import pymongo 
import getpass
import string

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["User_Details"]
collection = mydb["user"]
dict = {}
mydb2 = myclient["Movie_Details"]
movies = mydb2["Movies"]
dict1 = {}
uname = ''
pass5 = ''
eLog = ''
M_name=''
def welcome():
    print("Welcome to Movie Ticket Reservation System")






def create_user():
    user = input("Please enter your name: ")
    password = input("Please enter your password here: ")
    password2 = input("Please enter your password again here: ")
    email = input("Please enter your Email address: ")
    if password == password2 :
        c2 = encrypt(password)
        mydb.collection.insert_one({user:c2,'email':email})
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
    # while True:
        print("Select your choice from the given below: ")
        print("1.Book a Ticket" )
        print("2.View Booked tickets" )
        print("3.Logout" )
        try:
            ch = int(input("Enter your choice (1/2/3/4) here: "))
            if ch == 1:
                book()
            #elif ch==2:
                #view_bookings()
            #elif ch==3:
             #   print("Successfully logged out.")
              #  exit()
            else:
                print("Please enter a valid number from the given options only")
        except ValueError:
            print("Invalid Input! Please Enter a Number.")
def book():
    while True :
        print("Please select number corresponding to the movie from the options given below to book a seat or 6 to exit: ")
        movie_list = ["Kanthaara","KGF","Modiji","Motte","ChakDeIndia"]
        print("The movies available are: ")
        for i in range(len(movie_list)):
            print((i+1),".",movie_list[i])
        try:
                ch = int(input("Enter your choice (1/2/3/4/5/6) here: "))
                if ch!=6 :
                    option = movie_list[ch-1]
                    M_name = option
                if ch == 1:
                    reserve(option)
                    break
                elif ch == 2:
                    reserve(option)
                    break
                elif ch==3:
                    reserve(option)
                    break
                elif ch==4:
                    reserve(option)
                    break
                elif ch==5:
                    reserve(option)
                    break
                elif ch==6:
                    print("Logged out successfully")
                    exit()
                else:
                    print("Please enter a valid number from the given options only")
        except ValueError:
                print("Invalid Input! Please Enter a Number.")




def reserve(movie_name): #MongoDB new database consisting of movie names is to be made and user details after booking like ticket number and should be updated in the collection.
    total_seats = 64
    seats_available = 0
    x  = movies.find({"Name":f'{movie_name}'},{"_id":0,"Name":0})
    for y in x :
        for z in y :
            seats_available = y[z]
    print("Seats Available  = ",seats_available)
    seat_book()





def seat_book():
    total_seats = 64
    seat_layout = []
    k=1
    for i in range(1,9):
        row = []
        for j in range(1,9):
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
        while x<1 or x >64:
            print("Wrong Seat Number Enter 1-64 ONLY: ")    
            x = int(input())
        else :
            num_seats.append(x)     
  
    print("Seats for reserving: ",num_seats)
    print("Reserving Seats")
    mydb.collection.update_one({uname:pass5},{"$set" : {'Reserved' : num_seats}})
    print("Seats Reserved")
    #START HERE DB2 UPDATE NOT WORKING

def login_user():
    echeck = input("Enter Email you signed Up with: ")
    user = input("Please enter your name: ")
    password = (getpass.getpass("Please enter your password here: "))  
    pwd = encrypt(password)
    query = {'email':echeck,f'{user}':pwd}
    const={'_id':0}
    x = mydb.collection.find(query,const)
    for y in x:
        for z in y:
            dict[z]=y[z]
    if user in dict and dict[user]==encrypt(password):
        uname = user
        pass5 = password
        eLog = echeck
        print(f"Login as {user} Successful")
        after_login()
    else :
        print("Entered Credentials do not match") 







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
        try:
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