#Name:Sergey Vershinin
#Date: 10/20/2018
#This program organize the names.

s =input("Please enter your list of names: ")

# Epstein, Susan; St. John, Katherine; Vazquez-Abad, Felisa; Xu, Jia; Zamfirescu, Christina

s1=s.split("; ")
print(s1)
glue=","
s2=glue.join(s1)
print(s2)

s3 = s2.split(",")
print(s3)

new = " "
ls=len(s3)
for i in range(0,ls):
    if i%2 ==0:
        new = s3[i+1]+ " " + s3[i]
        print(new)
   
