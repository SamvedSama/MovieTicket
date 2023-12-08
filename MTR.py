import login,creatinguser,requi,admin

def main_menu(): #New User View Booking returns error2
    creatinguser.welcome()
    while True:
        print("Choose your option from the below: ")
        print("1. Create a new user ")
        print("2. Login ")
        print("3. Display Movies List ")
        print("4. Exit ")
        try:
            ch = int(input("Enter your choice (1/2/3/4) here: "))
            if ch == 1:
                creatinguser.create_user()
            elif ch == 2:
                login.login_users()
            elif ch==3:
                admin.display_movies()
            elif ch==4:
                print("Thanks for using our Reservation System!")
                exit()
            else:
                print("Please enter a valid number from the given options only")
        except ValueError:
            print("Invalid Input! Please Enter a Number.")
main_menu()
requi.myclient.close()

#give an offer on repeated bookings                                     //Done
#make a flag based check system for amt transfer (form fills) for bills //CARD to be done (done almost)
#logs of each person in each persons field                              //Done
# being able to book 1week b4                                           //Done 
#check @gmail.com                                                       //Done

#print ticket                                                           

#think of multiple theatres                                             //Double comment think of this only when you are too jobless or suraj is willing to go manual labour
#Reduce lines by importing modules                                      //Done fixed bugs also (alot)
#ADD MULTIPLE DATES                                                     //Done 



#make admin                                                              
#comment to self : try catch every input
#requi to core


#Future Work :
#Display Genre
