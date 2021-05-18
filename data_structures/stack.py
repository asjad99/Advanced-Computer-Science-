class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.next_ptr = None

class Stack:
    def __init__(self):

        self.top_ptr = None

    def push(self, mydataval=None):

        mynode = Node()
        mynode.dataval = mydataval
        mynode.next_ptr =  self.top_ptr

        self.top_ptr = mynode
        return

    def pop(self):
        if self.top_ptr is not None:
            myval =  self.top_ptr.dataval
            self.top_ptr = self.top_ptr.next_ptr
            return myval
        else:
            return ("empty stack")

mystack = Stack()

mystack.push('myval1')
mystack.push('myval2')
print(mystack.pop())
mystack.push('myval3')
print(mystack.pop())
print(mystack.pop())
print(mystack.pop())