import random;

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
float=2.3;
# print(int(float));

#random number from a range
# print(random.randint(20,50));

#verify data type with isisntance
def verify(input):
    if isinstance(input, int):
        print('Its an integer');
    else:
        print('Its not an integer');
        
verify(age_two);