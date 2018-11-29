#Name:Sergey Vershinin
#Date: November'13 2018
#ask a user enter a string

mess = input("Enter a non-empty string: ")

while len(mess) < 1:
    print("That was empty. Try again.")
    mess = input("Enter a non-empty string: ")
print("You entered: ", mess)
