import time
import requi,login,reserve,trans
booked_seats =[]
def check(y):
    x = requi.movies.find_one({'Name':reserve.M_name})
    seats_available= x["seats_available"]
    try : 
        global seats_day
        seats_day=seats_available[login.date]  
    except KeyError:
        seats_available[login.date] = [[0]]
        seats_day = seats_available[login.date]
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
        
def rebook_check(x):
    pass
    global booked_seats
    if x in booked_seats:
        print(f"Seat Number {x} is already booked , enter new seat number ")
        x = int(input())
        return rebook_check(x)
    else :
        return x
    
def seat_book():    
    dat = login.date                                
    uname = login.uname
    M_name = reserve.M_name
    total_seats = 64
    requi.os.system("cls")
    print(f"Logged in as {uname}")
    x = requi.movies.find_one({'Name':M_name})    
    print("RS - Reserved Seats")
    seats = list(map(check,list(i for i in range(1,65)))) #rs= disabled buttons 
    k=0
    for i in range(1,9):
        for j in range(1,9):
            print(seats[k],sep=",",end=" ")
            k+=1
        print()
    while True:
        num_of_seats = int(input("How many seats would you like to reserve? "))
        seats_available=0
        l1 =[]
        x = requi.movies.find_one({'Name':reserve.M_name}) 
        try :         
            seats_available= x["seats_available"]
            seats_day=seats_available[login.date]
        except KeyError:
            seats_day=[[0]]
        
        for seats in seats_day:
            for i in seats:  
                l1.append(i)
        seats_available = 64-len(l1)
        if num_of_seats>seats_available or num_of_seats<1:              
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
    num_seats = list(map(rebook_check,num_seats))  
    print("Seats for reserving: ",num_seats)
    stat_check=trans.pay(num_of_seats)
    if stat_check["transaction_status"]==False:
        print("Payment Aborted , Tickets were not booked ")
        print("Thanks for Using ,Will be logging out shortly :) ")
        time.sleep(2)
        exit()
    elif stat_check["transaction_status"]==True:
        print("Reserving Seats")
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
    else :
        print("Transaction Error")