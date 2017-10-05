# Python for Data Science & Machine Learning 
# Python 3.6. 

## Enviroment  

#### Visual Studio Code
#### Jupyter Notebooks 
#### Anaconda 
#### Spyder
#### Files & Notes are compatible with Python 2.


## Variables 
#### Variables are container where you can store varius date types. 
#### Variables can store all sorts of things, not just numbers. A typical other thing you want to have stored often is a string - a piece of text. Strings are indicated with a starting and ending " (double quote). You’ll learn about this and other types of data you can store, and what you can do with them later on.


## Strings
#### Everything inside the quotes "" are strings
#### String has methods associated. For methods you need to use dot notation.
#### Code - dir(variable) -  you can print all avaible methods

### Indexing and Split Strings
#### c = "Hi There!"
#### c[] indexing the string, python start counting from num 0
#### c[0] - output is H; c[2] output is " " 
#### c[-1] output is ! indexing from the end of the string
#### c[0:1] outis H, splitting in Python is upper bound exclusive!!!
#### c[0:2] output is "Hi" 
#### c[-3:-1] output is 're: from the end of the string

## Lists

### The list is a most versatile datatype available in Python which can be written as a list of comma-separated values (items) between square brackets. Important thing about a list is that items in a list need not be of the same type.

### Creating a list is as simple as putting different comma-separated values between square brackets. For example − my_list = ['Slavo', 36, "Python", "Swift", 3450]

### To access values in lists, use the square brackets for slicing along with the index or indices to obtain value available at that index. For example − my_list[2] output is Python

### You can update single or multiple elements of lists by giving the slice on the left-hand side of the assignment operator, and you can add to elements in a list with the append() method 

## Tuples
#### A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

#### Creating a tuple is as simple as putting different comma-separated values. Optionally you can put these comma-separated values between parentheses also. 
#### example - my_tuple = ("Slavo", 45, 4.6)