import login,requi
movie_list=[]
def admin():
    while True:
        print("Logged in as Admin")
        print("Select Choice")
        print("1.Show Movies")
        print("2.Add Movie")
        print("3.Delete Movie")
        print("4.Show Bookings for a Movie")
        print("5.Logout") 
        try:
            ch = int(input("Enter Choice (1/2/3/4/5)"))
    
            if ch == 1:
                display_movies()
            elif ch == 2:
                add_movie()
            elif ch == 3:
                delete_movie()
            elif ch == 4:
                show_bookings()
            elif ch == 5:
                print("Successfully logged out")
                exit()
        except ValueError:
            print("Please enter only numbers 1-5")
def add_movie():
    print("Adding Movie")
    title = input("Enter Title: ")
    movie_list.append(title)
    requi.movies.insert_one({'Name':title ,"seats_available" : {} })
    print("Movie Successfully Added")
    admin()
    return None
def delete_movie():
    while True:    
        global movie_list
        display_movies()
        print("Enter Movie Name You Want To Delete")
        ch = input()    
        if ch in movie_list: 
            movie_list.remove(ch)
            requi.movies.delete_one({"Name":ch })
            print("Movie Deleted Successfully ")
            break
        else :
            print("Movie Does Not Exist")

def display_movies():
    requi.os.system("cls")
    global movie_list
    buffer_movie=requi.movies.find({},{"_id":0,"seats_available":0})
    for i in buffer_movie:
        for key in i:
            print(f"{i[key]}")
            movie_list.append(i[key])
def show_bookings():
    print("Which Movie Do You want to check bookings for :")
    ch = input()
    x = requi.movies.find({"Name":ch},{"_id":0,"Name":0})
    for i in x :
        print(i)
