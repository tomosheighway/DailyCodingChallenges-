""" This problem was asked by Apple.

Implement a queue using two stacks. 
Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods:
 enqueue, which inserts an element into the queue, and dequeue, which removes it."""

class QueueStacks:
    def __init__(self):
        self.stack_in = []   # Stack for enqueue
        self.stack_out = []  # Stack for dequeue

    def enqueue(self, item):
        self.stack_in.append(item)

    def dequeue(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:
            raise IndexError("Dequeue from  empty queue")
        return self.stack_out.pop()

# Testing 
q = QueueStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)


print("Before dequeue")
print("  stack_in:", q.stack_in)
print("  stack_out:", q.stack_out)

print(q.dequeue())  # Expected output: 1

print("After dequeue")
print("stack_in:", q.stack_in)
print("stack_out:", q.stack_out)


print(q.dequeue())  # Expected output: 2
q.enqueue(4)
print(q.dequeue())  # Expected output: 3
print(q.dequeue())  # Expected output: 4
