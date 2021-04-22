# write a program to change position of each element n with  n+1 in a list

a=[10,20,30,40]


'''
ans_list=[]
for i in range(len(a)):
     ans_list.insert(i,0)

for i in range(len(a)):
            if(i == len(a)-1):
                 ans_list[i]=a[0]
            else:
                  ans_list[i]= a[i+1]
'''

ans_list=list(map(lambda n:a[n+1] if n !=len(a)-1  else  a[0],[k for k in range(len(a))]))
             
      
print(ans_list)