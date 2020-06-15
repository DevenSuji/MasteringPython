# # This script spits out the minimum value

number1 = int(input('Enter first integer: '))
number2 = int(input('Enter second integer: '))
number3 = int(input('Enter third integer: '))

minimum = number1

if number2 < minimum:
    minimum = number2

if number3 < minimum:
    minimum = number3

print('Minimum value is', minimum)

# # There is an inbuilt function called min to perform the same operation.

print(min(3, 1, 2))
