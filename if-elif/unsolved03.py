'''write a python  program to check if input number is 
  real number 
  float number 
  string number 
  complex number 
  zero (0)
 
'''


num=input("enter a input number  to check it's type ")

numtype=""
if(num>'0' and num<='9'): 
              numtype="real number "
              if (num.__contains__('+')):
                   numtype="complex number "
              if (num.__contains__('.')):
                   numtype="float number "
elif (num=='0' and len(num)==1):
                      numtype="zero "             
else:
       numtype="string "        
print(numtype)                