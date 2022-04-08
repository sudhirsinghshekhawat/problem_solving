# Write your code here
# no_of_items = input().split(" ")
# print(no_of_items)
items = "45 32 12 78 13".split(" ")
# print(items)
# operation_count = input()
# print(operation_count)
operation_no = "32 13".split()

print(f"{items}")
print(f"{operation_no}")


# [45,32,78,13,12]

def reorder_arr(items, operation_no):
    a, b = operation_no
    index_a = items.index(a)

    index_b = items.index(b)

    index_after_a = index_a + 1

    print(items[index_b])

    new_array = items[0:index_a+1] + items[index_after_a+1:index_b+1] + [items[index_after_a]] + items[index_b+1:]
    print(new_array)


reorder_arr(items, operation_no)
