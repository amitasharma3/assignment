#!/usr/bin/env python
# coding: utf-8

# In[1]:



# 1.1 Write a Python Program to implement your own myreduce() function which works exactly
#      like Python's built-in function reduce()


from functools import reduce
 
def do_sum(x1, x2): 
    return x1 + x2                  

print(reduce(do_sum, [1, 2, 3, 4]))


# In[ ]:





# In[2]:


def do_sum(x1, x2): 
    return x1 + x2

def my_reduce(func, seq):
    first = seq[0]
    for i in seq[1:]:
        first = func(first, i)
    return first

print(my_reduce(do_sum, [1, 2, 3, 4]))


# In[3]:


#1.2 Write a Python program to implement your own myfilter() function which works exactly
#  like Python's built-in function filter()






# In[6]:


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

f = filter(is_even, [1, 3, 10, 45, 6, 50])

print(f)

for i in f:
    print(i)


# In[13]:


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

print( list(filter(is_even, [1, 3, 10, 45, 6, 50])) )




# Implement List comprehensions to produce the following lists.
# Write List comprehensions to produce the following Lists
# ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
# [[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6],
# [4, 5, 6, 7], [5, 6, 7, 8]]
# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

# In[12]:




# Compress above for loop into a single list comprehension using technique [i <Upper for condition> <lower for condition>]

input_list = ['x','y','z']
result = [ item*num for item in input_list for num in range(1,5)  ]
print("['x','y','z'] => " +   str(result))


# Compress above for loop same as above

input_list = ['x','y','z']
result = [ item*num for num in range(1,5) for item in input_list  ]
print("['x','y','z'] => " +   str(result))

#

input_list = [2,3,4]
result = [ [item+num] for item in input_list for num in range(0,3)]
print("[2,3,4] =>" +  str(result))

#

input_list = [2,3,4,5]
result = [ [item+num for item in input_list] for num in range(0,4)  ]
print("[2,3,4,5] =>" +  str(result))

#

input_list=[1,2,3]
result = [ (b,a) for a in input_list for b in input_list]
print("[1,2,3] =>" +  str(result))


# In[14]:


#Reduce will produce a single result
def myreduce(anyfunc, sequence):

 # Get first item in sequence and assign to result
  result = sequence[0]
 # iterate over remaining items in sequence and apply reduction function 
  for item in sequence[1:]:
   result = anyfunc(result, item)

  return result


# Custom filter function 
def myfilter(anyfunc, sequence):

 # Initialize empty list
 result = []
 # iterate over sequence of items in sequence and apply filter function
 for item in sequence:
  if anyfunc(item):
   result.append(item)

 # return funal output
 return result


# test myreduce function
def sum(x,y): return x + y

# test myfilter function
def ispositive(x):
 if (x <= 0): 
  return False 
 else: 
  return True


# In[15]:


print ("Sum on list [1,2,3] using custom reduce function "   + str(myreduce(sum, [1,2,3])) )
print ("Filter only positive Integers on list [0,1,-2,3,4,5] using custom filter function"  + str(myfilter(ispositive, [0,1,-2,3,4,5])))


# 
# 

# In[ ]:




