# question 1 
num=int(input("ENTER A NUMBER"))
if num>0:
    print("The square of num is",num**2)
    print("The square of num is",num**3)
else:
    print("Enter a poisitive number")


# question 2   
a=int(input("ENTER A NUMBER   "))
b=int(input("ENTER ANOTHER NUMBER   "))
if a>b:
    print("FIRST NUMBER IS GREATOR NUMBER")
else:
    print("SECOND NUMBER IS GREATOR NUMBER") 


# question 3
i=int(input("ENTER A NUMBER"))
if i%2==0:
    print("NUMBER IS EVEN ")
else:
    print("NUMBER IS ODD ")
        

#question 4
j=int(input("ENTER A NUMBER"))
if(j % 7 ==0):
    print("NUMBER IS DIVISIBLE BY 7")
else:
    print("NUMBER IS NOT DIVISIBLE BY 7")    

#question 5
x=float(input("ENTER YOUR MARKS OF PHYSICS"))
y=float(input("ENTER YOUR MARKS OF CHEMISTRY"))
z=float(input("ENTER YOUR MARKS OF BIOLOGY"))
avg=((x+y+z)/3)
if avg>=80:
    print("DISTINCTION")
elif avg>=60 and avg<80:
    print("FIRST DIVISION") 
elif avg>=45 and avg<60:
    print("SECOND DIVISION") 
elif avg>=40 and avg<45:
    print("PASS") 
else:
    print("NOT PROMOTED")    