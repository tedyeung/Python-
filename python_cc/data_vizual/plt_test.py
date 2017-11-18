'''
A number raised to the third power in cube.Plot the first five cubic numbers. 
and then plot the first 5000 cubic numbers
'''

import matplotlib.pyplot as plt

values =[x for x in range(1,6)]
cubes = [x**3 for x in range(1,6)]

print('Values: ', values)
print('Cubes: ', cubes)
plt.plot(values, cubes, linewidth=2)
plt.title = ("Simple Graph of cube numbers")
plt.xlabel = ('Values')
plt.ylable = ('Cubes')
plt.tick_params(axis='both', labelsize=14)
plt.show()