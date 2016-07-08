list=[3,15,2,154,21,5,349,321,6,6413,366]

for passnum in range(len(list)-1,0,-1):
    for i in range(0,passnum):
        
        if list[i]>list[i+1]:
            temp=list[i]
            list[i]=list[i+1]
            list[i+1]=temp

    print (list)


