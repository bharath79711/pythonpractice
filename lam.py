
##   lambda ##
"""
add=lambda x,y: x+y

print("sum of x,y:",add(10,20))

print("sum of x,y:",add(30,20))
"""
"""
square =(lambda x:[i*i for i in x ])

print(square((1,2,3,4,5)))

"""
"""
even_odd=(lambda x : [i**2 if i%2==0 else i for i in x])

print(even_odd([1,2,3,4,5]))


"""
"""
num=(lambda x,y:x*y)(5,5)
print(num)


Big_num =lambda a,b:a if a>b else b
print(Big_num(16,12))

"""


"""
last_char = lambda s:s[-1]
print(last_char("Bharath"))

rev_str = lambda s:s[::-1]
print(rev_str("Bharath"))


rev_sentence =lambda s:" ".join(s.split()[::-1])
print(rev_sentence("i love my village chintakunta"))

"""
"""
sum_args=lambda *args:sum(args)
print("sum:",sum_args(10,20,30,40))

"""
"""
def func(*args):
    for i in args:
        if i%2==0:
           yield i**2

x=func(1,2,3,4,5,6,7,8)
print(list(x))

"""




