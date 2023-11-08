#ques1= write a class train which has methods to book a ticket,get status(no.of seats)
#and get fare information of trains running indian railwys.

#ques2=can you chnge the self parameter inside a class to something else(say'ayush').
# try changing self or slf or harry and see the effect.

#ans2=yes we can use all of these but you have to change these things on both the places.

class seats:
    pass 

class train:
    def __init__(slf,name,seats,fare,speed):
        slf.name=name
        slf.fare=fare
        slf.seats=seats
        slf.speed=speed

    def getstatus(slf):
        print("the name of the train is:",slf.name)
        print("the speed of the train:",slf.speed)

    def seatsinfo(slf):
        print("the avaliable seats in train are:",slf.seats)  

    def fareinfo(slf):
        print("the fare for one way in the train is:",slf.fare)
    
    def bookticket(slf):
        if slf.seats>0:
            print("you ticket has been booked!! and your seat number is",slf.seats)
            slf.seats=slf.seats-1
        else:
            print("sorry train is fully booked!! kindly book your ticket in taktal")

train1=train("Rajdhani Express",500,1000,130)
train2=train("Humsafar Express",700,790,120)
train3= train("Duronto Express",550,800,150)
train4=train("Tejas Express",450,850,140)

train1.getstatus()
train1.fareinfo()
train1.bookticket()
train1.seatsinfo()

train2.getstatus()
train2.fareinfo()
train2.bookticket()
train2.seatsinfo()

train3.getstatus()
train3.fareinfo()
train3.bookticket()
train3.seatsinfo()

train4.getstatus()
train4.fareinfo()   
train4.bookticket() 
train4.seatsinfo() 