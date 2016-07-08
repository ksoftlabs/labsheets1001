list = [15,2,158,184,12,5413,216,3]
sorted=False
count=0

while (not sorted):
    sorted=True
    for element in range (0,len(list)-1):
        count=count+1
        if list[element] > list[element+1]:
            sorted=False
            temp=list[element]
            list[element]=list[element+1]
            list[element+1]=temp
    print (list)
            
