# Standard List

a = [66.25, 333, 333, 1, 1234.5]

print a.count(333)
print a.count(66.25)

a.insert(2, -1)
a.append(333)

print a

print a.index(333)

a.remove(333)
print a

a.reverse()
print a

a.sort()
print a

print a.pop()
print a

# as Stack - Last In First Out
print "-" * 5 + "as Stack" + "-" * 5
stack = [3, 4, 5]
stack.append(6)
stack.append(7)

print stack

print stack.pop()
print stack.pop()

print stack

# as Queue - First In First Out
print "-" * 5 + "as Queue" + "-" * 5
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
queue.popleft()
print queue



