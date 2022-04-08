arr = [1, 2, 3, 4, 5, 6, 7, 7, ]

print(arr)
print('----')

for val in arr:
    print(val)

print('----')
for i, val in enumerate(arr, start=1):
    print(i, val)

y = [x for x in arr if x % 2 == 0]
print(y)

print(arr[-1])

arr[1] = 11

print(arr)
arr.append(101)
print(arr)

arr.insert(0, 1111)

print(arr)

del arr[0]

print(arr)

print(arr.pop())

print(arr)
arr.remove(7)

print(arr)

arr.sort(reverse=True)
print(arr)
print(sorted(arr))
print(arr)

arr.reverse()

print(arr)
print(len(arr))

ll = ['a', 'b', ]
print(ord(ll[0]))

arr1 = [11, 2, 3, 4, 45, 5]
i = len(arr1)

for j in range(i-1, 0, -1):
    print(j)
