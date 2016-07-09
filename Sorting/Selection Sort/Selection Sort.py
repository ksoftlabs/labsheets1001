list=[33,2,15,89,489,46486,21,25,24]

print("The unsorted list is as follows",list) 
for i in range(8,0,-1):
   maxIndex=0
   for location in range(1,i+1):
       if list[location]>list[maxIndex]:
           maxIndex = location
   #swapping
   temp = list[i]
   list[i] = list[maxIndex]
   list[maxIndex] = temp

   print (list)
print("The sorted list is as follows",list)
