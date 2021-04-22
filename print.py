#print("HELLO WORLD",sep="\n")


def print_trapezium():
             print("printing a trapzeium")
             for i in range(10):
                   for j in range(10):
                        if(j in range((10//2)-i,(10//2)+i+1)     ):
                           print("*",end="")
                        else:
                          print(" ",end="")     
                   print("\n")                



def print_triangle(n):
           print("printing a triangle")
           for i in range(n):
                for j in range(i):
                        print("*",end="")
                print("\n")
                                        
               



      
if __name__=="__main__":
              print_trapezium()
              print_triangle(10) 
              