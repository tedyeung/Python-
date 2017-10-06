# Please create a function that converts Celsius degrees to Fahrenheit. The formula to convert   Celsius to Fahrenheit is F = C × 9/5 + 32.

def temperatura (celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

print("Celsius: 36,6 Fahremheit: ", temperatura(36.6))

# The lowest possible temperature that physical matter can reach is -273.15 °C. With that in mind, please improve the function by making it print out a message in case a number lower than -273.15 is passed as input when calling the function.

def temp (c):    
    if c < -273.15:        
        return "That temperature doesn't make sense!"    
    else:        
        f = c * 9/5 + 32        
        return f
print(temp(-273.4))

# Consider the following list:
# temperatures=[10,-20,-289,100]
# Then, iterate over the temperature converter function that you created in execise 3 and print out the following output.