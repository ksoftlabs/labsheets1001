import math

a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b :"))
c=int(input("Enter the value of c :"))

discRoot=math.sqrt(b*b-4*a*c)
root1=(-b+discRoot)/(2*a)
root2=(-b-discRoot)/(2*a)

print("Roots are",root1,"and",root2) 
