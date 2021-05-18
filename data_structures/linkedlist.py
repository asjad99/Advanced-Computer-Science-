'''
About:

A sequence is an ordered collection of data values. The sequence is a powerful, fundamental abstraction in computer science.

Linked


Applications:



'''

class Node:
    def __init__(self, dataval=None):
        self.pre_ptr = None
        self.dataval = dataval
        self.next_ptr = None


class SLinkedList:
    def __init__(self):
        self.head_ptr = None

    def listprint(self):
        my_pointer = self.headval
        while my_pointer is not None:
            print (my_pointer.dataval)
            my_pointer = my_pointer.nextval

'''
Objects are both information and processes, bundled together to represent the properties, interactions, and behaviors of complex things.
'''

mylist = SLinkedList()

e1 = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

#------------------------------
mylist.head_ptr = e1
# Link first Node to second node
e1.next_ptr = e2
e2.pre_ptr = e1
# Link second Node to third node
e2.next_ptr = e3
e3.pre_ptr = e2

mylist.listprint()

#------------------------------
