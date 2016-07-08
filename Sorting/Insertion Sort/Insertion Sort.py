list=[33,2,15,89,489,46486,21,25,24]

for index in range(0,len(list)):

    currentvalue=list[index]
    position = index

    while position > 0 and list[position-1]>currentvalue:
        list[position]=list[position-1]
        position = position - 1

    list[position]=currentvalue
    print(list)

    
