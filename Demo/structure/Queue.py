from collections import deque

queue = deque()

#入队
queue.append(1)
queue.append(2)
queue.append(3)

#出队
#front = queue.popleft()
front2 = queue.pop()
print(front2)
