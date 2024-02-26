'''Build a program that converts temperatures between Celsius and Fahrenheit using a dictionary 
to store conversion factors.'''

temperature = {}
celsius = int(input("Enter the temperature in celsius "))
fahrenheit = (celsius * 9/5) + 32
temperature[celsius]=fahrenheit
print(temperature)