#Numbers -> words example from lecture
#Fill in the function

def num2words(num):
    word = ""
    if num == 1:
        word = "one"
        return(word) 
    if num ==2:
        word = "two"
        return(word)
    if num ==6:
        word = "six"
        return(word)
    
   

#    return(word)
    
#Sample calls to function:

def main():
    num = int(input("Enter a number: "))
    w = num2words(num)
    print(num, "is", w) 
    
    
if __name__ == "__main__":
     main()
    
#print(1, "is", num2words(1))
#print(6, "is", num2words(6))
