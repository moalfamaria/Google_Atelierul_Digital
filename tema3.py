#exercitiul1

def my_function_ex1(*args, **kwargs):
    sum = 0
    for i in args:
        if type(i) is int or type(i) is float:
          sum += i
    return sum

print(my_function_ex1(1,5,-3))
print(my_function_ex1(1,5,-3,'Rasrs',[12,56,'dsada']))
print(my_function_ex1())
print(my_function_ex1(2,4,'ddfds',param_1=2))

print("debug")
#exercitiul2

def test_function(n):
    if not n:
        return 0, 0, 0
    else:
        if n % 2 == 0:
            total_sum, even_sum, odd_sum = n, n, 0
        else:
            total_sum, even_sum, odd_sum = n, 0, n
    return total_sum + test_function(n-1)[0], even_sum + test_function(n-1)[1], odd_sum + test_function(n-1)[2]

print("ex 2")
print(test_function(3))


''' 
def my_function(n):
    suma = 0
    sum_pare = 0
    sum_impare = 0

    if n == 0:
        return 0

    if n%2 == 0:
      sum_pare += n + my_function(n-2)
    else:
      sum_pare += my_function(n-1)

    if n % 2 == 1:
      sum_impare += my_function(n - 1)
    else:
      sum_impare += my_function(n - 1)

    suma = n+ my_function(n-1)
    return suma, sum_pare, sum_impare


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
print(my_function(6))
print(my_function(3))
print("debug 2")

'''


#exercitiul3
def my_function_tastatura():
    n = input()
    try:
        n = int(n)
        return n
    except:
        return 0

print(my_function_tastatura())
