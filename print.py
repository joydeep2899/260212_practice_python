#print("HELLO WORLD",sep="\n")



for i in range(10):
     for j in range(10):
                if(j in range((10//2)-1,(10//2)+i)     ):
                     print("*",end="")
                else:
                     print(" ",end="")     
     print("\n")                
     