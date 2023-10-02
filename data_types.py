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

# print(round((0.1 + 0.2), 2));

#TUPLES
numbers_tuple = (1,2,3);
numbers_tuple_two = 1,2,3;
mixed_type_tuple = ("Santi es el: ", 1 , True);
a_list = ["this is a list", "of two"];
other_list = [1,2,3];

def verify_tuple(input):
    if isinstance(input, tuple):
        print('The variable is a tuple');
    else:
        print('The variable is not a tuple');

# verify_tuple(mixed_type_tuple);
# print(type(mixed_type_tuple));
#make a tuple, from a list
# print(tuple(a_list));

one_item_tuple = (1,);

# print(one_item_tuple);

tuple_from_lists = (*a_list, *other_list);
print(tuple_from_lists);