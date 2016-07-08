noStudents = int(input("Enter number of students : "))
studentCount=0

while (studentCount < noStudents):
    print ("For student",studentCount+1)
    marks=float(input("Enter marks for student :"))

    if (marks > 100):
        print ("Wrong input")
    elif (marks > 75):
        print ("A Grade")
    elif (marks > 65):
        print ("B Grade")
    elif (marks > 50):
        print ("C Grade")
    elif (marks >= 30):
        print ("D Grade")
    elif (0 <= marks < 30): 
        print ("Fail")
    else:
        print ("Wrong input")

    studentCount = studentCount + 1
    cont=input("Do you want to continue? (y=yes, n=no)")
    


