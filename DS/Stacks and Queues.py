'''Stack's'''
# #Python does not actually have stacks, this is why we use lists for the concept
stack = []
stack.append(5)  #this is pushing elements to the stack
element = stack.pop() #this is popping elements off the stack
stackTop = stack[len(stack) - 1] #to read the top element of the stack

'''Queue's'''
# #Python does not actually have queues, this is why we use lists for the concept
queue = []
#enqueue
queue.append(5)  #this is puttting elements into the queue
#dequeue
element = queue.pop(0) #this is popping elements out of the queue
queueNext = queue[0] #to read the next item in queue

'''When poping elements from the start of the list above
 the entire list elements are actually shifted back.
 This means that pop() in a queue is actually O(n) complexity.
 Below we will look at a way to avoid this'''

from collections import deque

data = deque()
data.append()
element = data.popleft()


