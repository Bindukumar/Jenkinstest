inputlist = [11,1,2,3,4,5,10,0]

print "hello from assignment"
print "welcome!"

def getwhatyouwant(inputlist):
    cindex = 0
    
    newlist=[]
    while cindex < (len(inputlist)-1):
        i=0
        x = (len(inputlist) - cindex)
        while i < (x-1):
            j = [inputlist[cindex] + inputlist[i + cindex + 1],(inputlist[cindex],inputlist[i + cindex + 1], cindex, i + cindex + 1)]      
            newlist.append(j)
            i=i+1
        cindex +=1

    final = min(newlist)
    print "minimum value is : " , final[0] , "Mininum values got from addtion of :" , final[1][:2],  "Mininum values original index are :" ,final[1][2:]
    
getwhatyouwant(inputlist)
