from termcolor import colored
from pyfiglet import Figlet
# text = colored("Hello Salvo", 'red')
# text = input('What is your name? ')
name = 'Salvo'
f = Figlet(font = 'slant')


print (f.renderText(name));
# print(colored(text, 'green', 'on_red'));