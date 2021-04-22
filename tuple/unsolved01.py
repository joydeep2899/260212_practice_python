# program to find the repeated items of a tuple
tup=(10,20,40,40,77,88,88,90,99,99)
dupind=[]

repvalues=(dupind)


for  i in range(len(tup)-1): 
          for k in range(i+1,len(tup)):
                         if( tup[i]==tup[k] ) :
                                     if(tup[i] not in dupind):
                                                dupind.insert(len(dupind),tup[i])


print(" the repeated values are ",dupind)