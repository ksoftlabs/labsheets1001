from collections import deque
queue=deque([])
print(queue)
queue=deque(["a","b","c","d","e"])
print(queue)
queue.append("f")
print(queue)
queue.popleft()
print(queue)
