# write a program to find list of second smallest number in a list

a=[10,10,20,30,40,50]

minv=min(a)
maxv=max(a)+1
for i in a:
        if(i==minv):
              index=a.index(i)
              a[index]=maxv

secminvalue=min(a)

print("the second smallest  number in a list  is ",secminvalue)

