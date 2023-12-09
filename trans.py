import requi,login
import random
import string
from datetime import datetime

total_cost = 0

def pay(seat_num):
    ticket_price = 500
    global total_cost,status
    total_cost = seat_num * ticket_price
    x = requi.collection.find_one({'name':login.uname})
    try:
        if x["book_count"]>=5 and x["book_count"]<15:
            total_cost = 0.95*total_cost
            print("Discount of 5% applied")
        elif x["book_count"]>=15:
            total_cost = 0.8*total_cost
            print("Discount of 20% applied")
    except KeyError:
        pass
    print(f"Amount payable for {seat_num} is {total_cost}")
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
