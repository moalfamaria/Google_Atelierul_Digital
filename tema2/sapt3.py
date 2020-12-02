#def get_sum(a,b,*args):
 #   my_sum=0
  #  for number in args:
   #     my_sum += number
    #return my_sum + a + b
   # return a+b+c
    # print(args)

    #args - tuplu

#print(get_sum(6,8,2, "asdasdsa", 10))

#input - citit de la tastatura


my_var =input()
print(my_var)


def get_sum(n):
    if n == 0:
        return 0
    return n+get_sum(n-1)
print(get_sum(5))


if __name__ =='__main__':
    var2=5