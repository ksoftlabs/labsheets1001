def fact(number):
    if number==1:
        return 1
    else:
        return number*fact(number-1)

def fib(number):
    if number==0:
        return 0
    elif number==1:
        return 1
    else:
        return fib(number-1)+fib(number-2)

def gcd(number1,number2):
    temp =number2
    number2=number1%number2

    if number2==0:
        return temp
    else:
        return gcd(temp,number2)

def sumofnumbers(number):
    if number==1:
        return 1
    else:
        return number + sumofnumbers(number-1)

print("***** Menu ***** \n Factorial ==> 1 \n Fibonacci ==> 2 \n Greatest Common Devisor ==> 3 \n Sum of Numbers ==> 4")
choice = int(input("Enter Your Choice< 1 or 2 or 3 or 4 >  :"))

if choice==1:
    number=int(input("Enter the number :"))
    print(number,"!=",fact(number))
elif choice==2:
    number=int(input("Enter the number :"))
    print("Fibonacci Number for n =",number,"is",fib(number))
elif choice==3:
    number1=int(input("Enter the first number :"))
    number2=int(input("Enter the second number :"))
    print("GCD of",number1,"&",number2,"=",gcd(number1,number2))
elif choice==4:
    number=int(input("Enter the number :"))
    print ("Sum of first",number,"numbers =",sumofnumbers(number))
    
