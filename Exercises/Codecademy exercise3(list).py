"""
Let's say there are a list,
and we want to double the index,
and replace the original indexed element with the doubled indexed number.
if index number is too big in the list, it would just return the original list.

Create a function that does this.

For example,
double_index([1,21,25,8].2)
should return [1,21,50,8]

"""

#.Create function with two parameters lst, and index
def double_index(lst,index):
  if index < len(lst):
    a = lst[index] * 2
    lst.remove(lst[index])
    lst.insert(2,a)
    return lst
  else:
    return lst
 
  
