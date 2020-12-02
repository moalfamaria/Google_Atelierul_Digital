#exercitiul1

def my_function_ex1(*args, **kwargs):
    sum = 0
    for i in args:
        if type(i) is int:
          sum += i
    return sum

print(my_function_ex1(1,5,-3))
print(my_function_ex1(1,5,-3,'Rasrs',[12,56,'dsada']))
print(my_function_ex1())
print(my_function_ex1(2,4,'ddfds',param_1=2))

print("debug")

#exercitiul2
def my_function(n):
    if n == 0:
        return 0
    return n+ my_function(n-1)

def my_function_par(n):
    if n == 0:
        return 0
    if n%2 == 0:
     return n + my_function_par(n-2)
    else:
      return my_function_par(n-1)


def my_function_impar(n):
    if n == 0:
        return 0
    if n%2 == 1:
     return n + my_function_impar(n-1)
    else:
      return my_function_impar(n-1)


print(my_function(5))
print(my_function_par(6))
print(my_function_par(3))
print(my_function_impar(6))
print(my_function_impar(3))



#exercitiul3
def my_function_tastatura(n):
    input(n)
    if n == int(n):
        return n
    else:
        return 0

my_function_tastatura(400)
my_function_tastatura(4.7)
