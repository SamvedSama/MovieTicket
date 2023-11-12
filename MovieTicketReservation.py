import tkinter
import random
import pymongo 
import json

usrinfo = {}

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["User_Details"]
mycol = mydb["user"]


def welcome():
    print("Welcome to Movie Ticket Reservation System")

def create_user():
    user = input("Please enter your name: ")
    password = input("Please enter your password here: ")
    mydb.mycol.insert_one({user:password})
    print("User Successfully Created")

def login_user():
    user = input("Please enter your name: ")
    password = input("Please enter your password here: ")
    if mycol.find({"name":user,"password":password})==(user,password):
        print(f"Logged in as {user} successfully! ")
    else:
        print("Entered password or username is incorrect")
def display_movies():
    movie_list = ["Kantaara","KGF","Modiji","Motte","Chak De India"]
    for i in range(len(movie_list)):
        print(i,end="")

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