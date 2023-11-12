import tkinter
import random
import pymongo 
import json

usrinfo = {}
dict = {}

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["User_Details"]
collection = mydb["user"]
x = mydb.collection.find({},{'_id':0})

def welcome():
    print("Welcome to Movie Ticket Reservation System")

def create_user():
    user = input("Please enter your name: ")
    password = input("Please enter your password here: ")
    mydb.collection.insert_one({user:password})
    print("User Successfully Created")

def login_user():
    user = input("Please enter your name: ")
    password = input("Please enter your password here: ")
    for y in x:
        for z in y:
            if user==z and password==y[z]:
                print(f"Logged in as {user} successfully! ")
            else:
                print("Wrong Username or Password detected.")
def display_movies():
    movie_list = ["Kantaara","KGF","Modiji","Motte","ChakDeIndia"]
    print("The movie options are: ")
    for i in movie_list:
        print(i,end=" ")
    print()

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
                exit()
            else:
                print("Please enter a valid number from the given options only")
        except ValueError:
            print("Invalid Input! Please Enter a Number.")
            
main_menu()
myclient.close()
