#CSci 127 Teaching Staff
#March 2018
#A template for a program that computes LIRR transit fares.
#Modified by:  Sergey Vershinin

def computeFare(zone, ticketType, age):
     """
     Takes as two parameters: the zone and the ticket type.
     Returns the LIRR Transit fare, as follows:
     If the zone is 1 and the ticket type is "peak", the fare is 8.75.
     If the zone is 1 and the ticket type is "off-peak", the fare is 6.25.
     If the zone is 2 or 3 and the ticket type is "peak", the fare is 10.25.
     If the zone is 2 or 3 and the ticket type is "off-peak", the fare is 7.50.
     If the zone is 4 and the ticket type is "peak", the fare is 12.00.
     If the zone is 4 and the ticket type is "off-peak", the fare is 8.75.
     If the zone is 5, 6, or 7 and the ticket type is "peak", the fare is 13.50.
     If the zone is 5, 6, or 7 and the ticket type is "off-peak", the fare is 9.75.
     If the zone is greater than 8, return a negative number (since your calculator does not handle inputs that high).
     """
     
     fare = 0
     if zone == 1 and ticketType == "peak":
         fare = "8.75"
     if zone == 1 and ticketType == "off-peak":
         fare = "6.25"
     if zone == 1 and age == "senior":
         fare = 3.25
     

     if zone == 2 and ticketType == "peak":
        fare = "7.50"
     if zone == 2  and ticketType == "off-peak":
        fare = "5.75"
     if zone == 2 age == "senior":
        fare = "3.75"
     

     if zone == 3 and ticketType == "peak":
        fare = "9.75"
     if zone == 3 and ticketType == "off-peak":
        fare = "7"
     if zone == 3 and age == "senior":
        fare = "3.75"
     
    
     if (zone == 4 or zone == 6 or zone == 7 )and ticketType == "peak":
        fare = "13.50"
        
     if (zone == 5 or zone == 6 or zone == 7 ) and ticketType == "off-peak":
        fare = "9.75"
     

     if zone >= 8 and ticketType == "peak":
         fare = "-13.50"
         
     if zone >=8 and ticketType == "off-peak":
         fare = "-9.75"
     

     return(fare)

def main():
     z = int(input('Enter the number of zones: '))
     t = input('Enter the ticket type (peak/off-peak): ').lower()
     s = input('Enter the "age-type" ticket: ').lower()
     fare = computeFare(z,t,s)
     print('The fare is', fare)

#Allow script to be run directly:
if __name__ == "__main__":
     main()
                   
