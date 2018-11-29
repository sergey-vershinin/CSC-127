#CSci 127 Teaching Staff
#March 2018
#A template for a program that computes LIRR transit fares.
#Modified by:  Sergey Vershinin

def computeFare(zone, ticketType):
      
     fare = 0
     if zone == 1 and ticketType == "peak":
         fare = 6.75
     if zone == 1 and ticketType == "off-peak":
         fare = 5.00
     if zone == 1 and ticketType== "senior":
        fare = 3.25
     

     if zone == 2 and ticketType == "peak":
        fare = 7.50
     if zone == 2  and ticketType == "off-peak":
        fare = 5.75
     if zone == 2 and ticketType== "senior":
        fare = 3.25
     
     

     if zone == 3 and ticketType == "peak":
        fare = 9.25
     if zone == 3 and ticketType == "off-peak":
        fare = 7.00
     if zone == 3 and ticketType== "senior":
        fare = 4.50
     
     

     if zone > 3 and ticketType == "peak":
         fare = -1
         
     if zone > 3 and ticketType == "off-peak":
         fare = -1
     

     return(fare)

def main():
     z = int(input('Enter the number of zones: '))
     t = input('Enter the ticket type (peak/off-peak): ').lower()
     #s = input('Enter the "age-type" ticket: ').lower()
     fare = computeFare(z,t)
     print('The fare is', fare)

#Allow script to be run directly:
if __name__ == "__main__":
     main()
                   
