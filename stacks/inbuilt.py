# first one is list [] by default
from collections import deque
from queue import LifoQueue

s = deque() # type:ignore
s.append("Shekhawat")
s.append("Singh")
s.append("Sudhir")


print(s)

for i in s:
    print(i)


s1 = LifoQueue() # type:ignore
s1.put('Sudhir')
s1.put('Singh')
s1.put('Shekhawat')

print(s1)



# print(s.get())
# print(s.get())
# print(s.get())
print(s1.get_nowait())
print(s1.get_nowait())
print(s1.get_nowait())
# print(s.get_nowait())
