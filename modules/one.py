from termcolor import colored
from pyfiglet import Figlet

# text = colored("Hello Salvo", 'red')
text = input('What is your nick? ')
color = input('Please choose one of those colors \n gray, red, green, yellow, blue, magenta, cyan, white: ')
f = Figlet(font = 'slant')


print (colored(f.renderText(text.title()), color.lower()))
# print(colored(text, 'green', 'on_red'))