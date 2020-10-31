#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # Write a Python Program(with class concepts) to find the area of the triangle using the below
# formula.
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

# In[4]:


class polygon:
    def __init__(self,a,b,c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
a= int(input("a="))
b= int(input("b="))
c= int(input("c="))

class triangle(polygon):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)

    def get_area(self):
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5        

t = triangle(a,b,c)
print("area : {}".format(t.get_area()))


# # 1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns
# the list of words that are longer than n.

# In[ ]:


def listing(guess, number):

    new_list = []

    for i in range(len(guess)):
        if len(guess[i]) > number:
            new_list.append(guess[i])

    print (new_list)

list1 = input("take input: ")

list = list1.split(",")

def main():
    global list, integer1
    integer = input()
    integer1 = int(integer)
    listing(list, integer1)

main()


# # Write a Python program using function concept that maps list of words into a list of integers
# representing the lengths of the corresponding words.

# In[1]:


listOfWords = ['wordOne','wordTwo','wordThree','wordFour','wordFive']
 
listOfInts = []
 
for i in range(len(listOfWords)):
    listOfInts.append(len(listOfWords[i]))
 
print ("List of words:"+str(listOfWords))    
print ("List of wordlength:"+str(listOfInts))


# In[12]:


print(listOfWords)


# # Write a Python program using function concept that maps list of words into a list of integers
# representing the lengths of the corresponding words.

# In[11]:


s = "python is pretty fun to use"

list(map(len, s.split())) 


# In[ ]:





# # Write a Python function which takes a character (i.e. a string of length 1) and returns True if
# it is a vowel, False otherwise.

# In[14]:


def check(string): 
    string = string.replace(' ','') 
    string = string.lower() 
    vowel = [string.count('a'), string.count('e'), string.count('i'), string.count('o'), string.count('u')] 
  
    # If 0 is present int vowel count array 
    if vowel.count(0) > 0: 
        return('not accepted') 
    else: 
        return('accepted') 
  
  
  
# Driver code 
if __name__ == "__main__" : 
      
    string = "SEEquoiaL"
  
    print(check(string)) 


# In[ ]:




