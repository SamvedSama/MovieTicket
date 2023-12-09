import pymongo,string,os,getpass
from datetime import date
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["User_Details"]
collection = mydb["collection"]
movies = mydb["Movies"]
uname = ''
pass5 = ''
M_name= ''
dat =''
l1 = (str(date.today()).split('-'))
l1 = [i for i in  l1[::-1]]
for i in l1 :
    dat += i + '/'
dat = dat[0:-1]

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
