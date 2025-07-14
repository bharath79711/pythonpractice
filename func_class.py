"""
for i in range(x):
    print(i*y)



x = int(input("enter the value x:"))
y = int(input("enter the value y:"))

data = func_name(x,y)
print(data)
print("==========")
x = int(input("enter the value x:"))
y = int(input("enter the value y:"))
data2= func_name(x,y)
print(data2)

"""
"""
1. positional arguments or functions
    def func(arg1,arg2):
        ...
    func(value1,value2)

2. keyword argument
    def func(arg1,arg2):
        ...
    func(arg2=value1,arg1=value2)

3. variable length arguments or function
    def func_vari(*arg):
         ....
    func_vari(1,2,3,4,5)


4. empty functions or arguments
    def func():
       ...
    func()

5. default functions or arguments
    def func(arg1=value,arg2):
       ...
    func(arg2 = value)


*args == variable arguments
**kwargs ==multiple keyword arguments 
"""


# positional argument
def func_sum(x, y):
    value = x + y
    return value  # 30


# data_sum = func_sum(y=20, x=10)  # x,y
# print(data_sum)
# print(data_sum * 20)


def func_square(list_seq):
    """
    :param list_seq: list data
    :return: square of the list
    """
    em_list = []
    for i in list_seq:
        val = i * i
        em_list.append(val)
    return em_list


def func_cube(list_seq):
    em_list = []
    for i in list_seq:
        val = i ** 3
        em_list.append(val)
    return em_list


def check_even_odd(sequence):
    even_square = []
    odd_cube = []
    for i in sequence:
        if i % 2 == 0:
            even_square.append(i * i)
        else:
            odd_cube.append(i ** 3)
    return even_square, odd_cube


#
# data_square = func_square((1, 2, 3, 4, 5, 6))
# print("square function:", data_square)
# data_cube = func_cube(data_square)
# print("cube function:", data_cube)
# data_even_square, data_odd_cube = check_even_odd(data_square)
# print("even square:", data_even_square)
# print("odd cube:", data_odd_cube)


# empty function
def func_empty():
    x = 20
    y = 30
    return x + y


# data_empty = func_empty()
# print(data_empty)

# default function
def func_default(x, y=30):
    return x + y


# data3 = func_default(x=30,y=40)
# print(data3)

# variable function
def func_variable_len(*args):
    data_sq = (i * i for i in args)
    return list(data_sq)


# data = func_variable_len(1, 2, 3, 4, 5, 6)
# print(data)

# variable keyword function
def func_variable_len_keyw(**kwargs):
    dictt = {}
    for key, value in kwargs.items():
        dictt[key] = value * value
    return dictt


# data = func_variable_len_keyw(x=1, y=2, z=3, k=4, yu=5, m=6)
# print(data)

def func_dict(dict_val):
    return dict_val.keys()


data = func_dict({"name": "raju", "age": 20})
print(data)
print("hey hi")
