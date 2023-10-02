import random;
from math import floor, ceil;

#karray -> list
list = [1,2,3];
# print(type(list));

age="21";

#string to integer
# print(int(age));

age_two = 21;

#integer to string
# print(str(age_two));

#float to integer
# float_number=2.3;
# print(int(float));

#random number from a range
# print(random.randint(20,50));

#verify data type with isisntance
def verify(input):
    if isinstance(input, int):
        print('Its an integer');
    else:
        print('Its not an integer');
        
# verify(age_two);

#floats
f = 1.45;
f2 = float(2.0);
f3 = float("2");
f4 = 1.45e3;
#testing them
# print(float(f4));

#round characters at the right of the coma
# print(round(f,2));

#round the number to float down the nearest number
# print(floor(f));

#round the number to float up the nearest number
# print(ceil(f));

def verify_floats(number1, number2):
    if (number1 == number2):
        print('Float numbers are equal');
    else:
        print('Float numbers are different');
        
# verify_floats(f, f4);

print(round((0.1 + 0.2), 2));