# write a python program to convert a list of tuples into a dictionary

a=[('a',1),('b',2),('c',3)]
ans=[]
for i in a:
     tk=i[0]
     tv=i[1]
     ans.append({tk:tv})

print("the convert tuple to dictonary is ",ans)     
