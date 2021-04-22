
# Python code to merge dict using update() method
def merge(dict1, dict2):
    return(dict1.update(dict2))

dict1 = {'a': 1, 'b': 2}
dict2 = {'d': 3, 'c': 4}
 

merge(dict1, dict2)
 
# changes made in dict2
print(dict1)