def yielder(list_nums):
    for num in list_nums:
        yield num

my_list_nums = [1, 2, 3]

# print(yielder(my_list_nums))

for x in yielder(my_list_nums):
    print x
