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

#### To access values in tuple, use the square brackets for slicing along with the index or indices to obtain value available at that index. 
#### exapmle - 

## Dictionaries 
#### Each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is enclosed in curly braces. An empty dictionary without any items is written with just two curly braces, like this: {}.

#### Keys are unique within a dictionary while values may not be. The values of a dictionary can be of any type, but the keys must be of an immutable data type such as strings, numbers, or tuples.
#### example - my_dictionaries = {"Name": "Slavo", "age": 35, "nick_name": "Pop"}
#### To access dictionary elements, you can use the familiar square brackets along with the key to obtain its value. Following is a simple example − print(my_dictionaries["name"])

#### Dictionary values have no restrictions. They can be any arbitrary Python object, either standard objects or user-defined objects. However, same is not true for the keys.

#### There are two important points to remember about dictionary keys :

#### (a) More than one entry per key is not allowed. This means no duplicate key is allowed. When duplicate keys are encountered during assignment, the last assignment wins. 

#### (b) Keys must be immutable. This means you can use strings, numbers or tuples as dictionary keys but something like ['key'] is not allowed. Following is a simple 

## Functions

####  Function blocks begin with the keyword def followed by the function name and parentheses ( ( ) ). Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses.

#### example def full_name( first_name, last_name): 
####    print(first_name + " " + last_name)

#### Calling Function
#### Defining a function only gives it a name, specifies the parameters that are to be included in the function and structures the blocks of code.

#### Once the basic structure of a function is finalized, you can execute it by calling it from another function or directly from the Python prompt. Following is the example to call printme() function −
#### full_name(input('Add your first name? '), input('Add your last name? ')):

## Errors 
### Sytax Error and excepcion

## Conditionals
### = , >, <, <= ,>=
###  if condition:
###     pass/code
###  else:
####    pass/code

## Loops
### Repeats a statement or group of statements while a given condition is TRUE. It tests the condition before executing the loop body. Executes a sequence of statements multiple times and abbreviates the code that manages the loop variable. You can use one or more loop inside any another while, for or do..while loop.

