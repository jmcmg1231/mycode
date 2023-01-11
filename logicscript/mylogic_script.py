#!/usr/bin/env python3

movie_list = ["Great Outdoors", "InnerSpace", "Planes, Trains and Automobiles","Funny Farm", "Father of the Bride", "Delirious", "Captain Ron", "Christmas Vacation", "Stripes" ]

actors = ["John Candy", "Steve Martin", "Martin Short","Chevy Chase"]

round = 0

while round < 8: 
    round = round + 1
    print ("Can you guess what this four  80s/90s movie and actor this is?")

    print("A Chicago advertising man must struggle to travel home from New York for Thanksgiving, with a lovable oaf of a shower-curtain-ring salesman as his only companion.")

    print("What is the name of the advertising man?")
    advert_man = input()
    if advert_man == "Steve Martin":
        print("You are correct." +advert_man+ " Is the advertising man")
        break
    else: 
        print("That is incorrect please try again")
        break
        print("What is the name of the movie")
        pta = input()
     if pta == "Planes, Trains and Automobiles":
        print("You are correct. " +pta+ " is the name of the movie")
        break
    else:
        print("Please try again")
        break


