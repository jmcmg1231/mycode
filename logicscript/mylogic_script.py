#!/usr/bin/env python3

movie_list = ["g. Great Outdoors", "b. InnerSpace", "a. Planes, Trains and Automobiles", "f. Funny Farm", "c. Delirious", "d. Captain Ron", "e. Stripes"]

questions = {"A Chicago advertising man must struggle to travel home from New York for Thanksgiving, with a lovable oaf of a shower-curtain-ring salesman as his only companion.": "a", "A test pilot is miniaturized in a secret experiment, and accidentally injected into a hapless store clerk.":"b", "A soap opera writer gets hit on the head and wakes up as a character in his own show.": "c", "A Chicagoan inherits an old yacht. He, his wife, daughter and son fly to a Caribbean island and hire a dubious Captain Ron to sail them on an adventure to Miami." : "d", "Two friends who are dissatisfied with their jobs decide to join the army for a bit of fun.": "e", "A couple swap city life for the country, but their picturesque new hometown turns out to be just a little bit different to what they were expecting.": "f", "A Chicago man and his family go camping with his obnoxious brother-in-law.": "g"}



for key in questions:
    print(key)
    for ml in movie_list:
        print(ml)
    movie_name = input("Enter a,b,c,d,e,f, or g: ")
    movie_name = movie_name.lower()

    if questions.get(key)  ==  movie_name:
        print("You answer is correct")
    else:
        print("Your answer is incorrect")
