my_list = [7,8,9,2,3,1,4,10,5,6]
sorted_list_asc = my_list.copy()
sorted_list_desc = my_list.copy()
print(my_list)


#lista ordonata crescator
sorted_list_asc.sort()
print(sorted_list_asc)

#lista ordonata descrescator
sorted_list_desc.sort(reverse=True)
print(sorted_list_desc)


my_list.sort()
print(my_list)
#nr impare
print(my_list[1:][::2])
#nr pare
print(my_list[::2])
#multiplii de 3
print(sorted_list_asc[2::3])
