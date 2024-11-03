# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:

# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:

# You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

from collections import deque


class MyStack(object):

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1


    def pop(self):
        """
        :rtype: int
        """
        return self.queue1.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.queue1[0]


    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue1) == 0