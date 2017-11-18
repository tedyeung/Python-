import matplotlib

value = list(range(1,11))
power_of_4 = [x**4 for x  in value]
print ('Value ', value)
print ('Value power of 4 ', power_of_4)

plt.scatter(value, power_of_4, s=20)
plt.axis([0,15,0, 15000])
plt.show()