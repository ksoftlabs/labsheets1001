stack=[]
contmain="y"
cont="y"

print ("-----------------------------------------------------")
print ("To insert a number to stack, press '1'.")
print ("To remove the top value from the stack, press '2'.")

while contmain=="y":
    
    ans=int(input("Enter a option (1/2) : "))

    if ans==1:
            while cont=="y":
                num=int(input("Enter a number to insert to the stack : "))
                stack.append(num)
                cont=input("Do you want to insert more? (y/n): ")
            print ("The stack is now as follows",stack)
            cont="y"
    elif ans==2:
            if len(stack)==0:
                print ("stack is empty")
            else:
                while cont=="y":
                    rem=stack.pop()
                    print (rem,"is removed from the stack")
                    cont=input("Do you want to remove more? (y/n): ")
                
            print ("The stack is now as follows",stack)
    contmain=input("Do you want to do more operations? (y/n): ")
