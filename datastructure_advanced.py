from collections import deque

queue = deque(['Jhon', 'Peter', 'Gerry', 'Lenna','Nick'])
queue.append('Graham')
queue.append('Billy')
queue.popleft()

print(queue)
