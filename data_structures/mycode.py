class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.next_ptr = None

class Stack:
    def __init__(self):

        self.head_ptr = None
        self.tail_ptr = None

    def enqueue(self, mydataval=None):
        mynode = Node()
        mynode.dataval = mydataval
        if self.tail_ptr is not None:
            self.tail_ptr.next_ptr = mynode

        #mynode.next_ptr = self.tail_ptr

        self.tail_ptr = mynode
        if self.head_ptr is None:
            self.head_ptr = mynode

    def dequeue(self):
        if self.head_ptr is not None:
            myval =  self.head_ptr.dataval
            self.head_ptr = self.head_ptr.next_ptr
            return myval
        else:
            return ("empty stack")

mystack = Stack()

mystack.enqueue('myval11')
mystack.enqueue('myval22')
mystack.enqueue('myval33')

print(mystack.dequeue())
print(mystack.dequeue())
print(mystack.dequeue())
