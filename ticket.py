from PIL import Image, ImageDraw, ImageFont
import seatbook,reserve,login

def ticket_gen():    
    ticket_width = 400
    ticket_height = 500
    ticket_color = "white"
    ticket = Image.new("RGB",(ticket_width, ticket_height), ticket_color)
    draw = ImageDraw.Draw(ticket)
    text_color = "black"
    font = ImageFont.truetype("arial.ttf", 20) 
    user = seatbook.uname
    date = seatbook.dat
    movie_name = reserve.M_name
    email = login.email
    seat_number = ''
    for i in seatbook.num_seats:
        seat_number += str(i)+ ','
    seat_number=seat_number[:-2]
    ticket_info = f"----------- Welcome to Bookito ----------\n----------- Reservation System ----------\n\nCustomer Name :{user}\nEmail : {email} \nDate : {date}\n\n============================\n\nMovie: {movie_name}\nSeat: {seat_number}\n\n============================\n\n       Thank You For Choosing Us \n               Enjoy Your Movie"
    text_position = (20, 50) 
    draw.text(text_position, ticket_info, fill=text_color, font=font)
    ticket.save("movie_ticket.png")  
    return None