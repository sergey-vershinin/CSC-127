#Name:Sergey Vershinin
#date:10/21/2018
#this program greats by hour




hour = input("Enter hour (in 24 hour time): ")

i = int(hour)
if 0 < i< 12:
    print("Good Morning")
elif  12 <= i < 17:
    print ("Good Afternoon")
elif 17 <= i <= 24:
    print("Good Evening")
