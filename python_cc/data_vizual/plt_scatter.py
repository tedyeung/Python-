import matplotlib

value = list(range(1,11))
power_of_4 = [x**4 for x in (1,10)]
print ('Value ', value)
print ('Value power of 4 ', power_of_4)
plt.scatter(value, power_of_4, s = 20)
plt.axis([0, 10, 0 , 10000])

plt.show()