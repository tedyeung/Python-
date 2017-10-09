# In exercise 4, you recursively printed out converted temperature in the command line. For this exercise, please consider the same list of Celsius values again as input:

# temperatures=[10,-20,-289,100]

# Try to make a script that converts Celsius to Fahrenheit and creates a text file and stores the converted values inside the text file. Your text file content should look like this:

 # 50.0
 # -4.0
 # 212.0

# Please don't write any message in the text file when input is lower than -273.15.

temperatures = [10,-20,-289,100]
temp_file = open('temp_file.txt', 'w')
def temp (c):
    if c < -273.15:
        return "Dont Print"
    else:
        f = c * 9/5 + 32
        return f 
for t in temperatures:
    print ("Temp in F is", temp_file.write(temp(t)))
    temp_file.close()
