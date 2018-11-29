#this program greats by hour

import itertools

for h in itertools.repeat(1):
    hour = input("Enter hour (in 24 hour time): ")

    i = int(hour)
    if 0 < i< 12:
        print("Good Morning")
    elif  12 <= i < 17:
        print ("Good Evening")
    elif 17<= i <=24:
        print("Good Night")
    else:
        print("Use a Human's time range")
    

