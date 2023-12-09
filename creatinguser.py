import requi

def welcome():
    print("Welcome to Bookito")
    print("Follow the below instructions for smooth user experience ")

def create_user():
    date = requi.dat
    M_Reserved={}
    dic = {date:M_Reserved}
    user = input("Please enter your name: ").lstrip().rstrip()
    email = input("Please enter your email here: ")
    email2 = input("Please enter your email again here: ")
    password = input("Please enter your password here: ")
    password2 = input("Please enter your password again here: ")
    if password == password2 and email.endswith("@gmail.com") and email==email2:
        c2 = requi.encrypt(password)
        requi.mydb.collection.insert_one({'name':user,'password':c2,'email':email})
        requi.collection.update_one({"name":user},{'$set':{"movie_reserved": dic }})
        requi.collection.update_one({"name":user},{'$set':{"book_count": 0 }})
        requi.os.system("cls")
        print("User Created Successfully")
    else :
        requi.os.system("cls")
        print("Either password entered or email doesnt match the criteria, please try again.")
        print("Emails should end with '@gmail.com' only.")
