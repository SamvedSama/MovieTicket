import requi,seatbook,login
M_Reserved = {}
def reserve(movie_name): 
    global M_name
    login.uname
    M_name = movie_name
    requi.os.system("cls")
    print(f"Logged in as {(login.uname)}")
    print(f"Reserving seats for {M_name}")
    requi.M_name = M_name
    x  = requi.collection.find_one({"name":login.uname})
    y=x["movie_reserved"]
    if y!=None:
        global M_Reserved
        try :
            M_Reserved=y[login.date]
        except KeyError or TypeError :
            y[login.date]=M_Reserved
            M_Reserved[M_name]=None
        seatbook.seat_book()
    else :
        y= M_Reserved
        y[login.date]=M_Reserved
        M_Reserved=y[login.date]
        seatbook.seat_book()
