
# coding: utf-8

# In[1]:


# Use for, split(), and if to create a Statement that will print out words that start with 's':


# In[3]:


st = 'Print only the words that start with s in this sentence'


# In[7]:


split_st = st.split()


# In[11]:


for word in split_st:
    if word[0] == 's':
        print (word)


# In[12]:


# Use range() to print all the even numbers from 0 to 10.


# In[14]:


for num in range(0, 11):
    if num % 2 == 0:
        print (num)


# In[15]:


# Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.


# In[21]:


list_comprehension = [num % 3 == 0 for num in range(1, 51) ]


# In[22]:


print (list_comprehension)


# In[24]:


num_3 = [num for num in range(1, 51) if num % 3 == 0 ]
print (num_3)


# In[25]:


# Go through the string below and if the length of a word is even print "even!


# In[28]:


st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word) % 2 == 0:
        print (word)


# In[29]:


# Write a program that prints the integers from 1 to 100. But for multiples of 
# three print "Fizz" instead of the number, and for the multiples of five print 
# "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".


# In[39]:


for num in range (1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print ("FizzBuzz")
    elif num % 3 == 0:
        print ("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else: 
        print (num)
    
    


# In[40]:


# Use List Comprehension to create a list of the first letters of every word in the string below:


# In[44]:


st = 'Create a list of the first letters of every word in this string'
list_1 = [word[0] for word in st.split()]
print (list_1)

