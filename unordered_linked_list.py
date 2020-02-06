
from node import Node

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    # add a new node with value set to next_val to the list
    def add(self, next_val):
        if self.head != None:
            # make a new node with the desired value
            next_node=Node(next_val)
            # this new node should point to our current head
            next_node.setNext(self.head)
            # the new head is the new node
            self.head = next_node
        else:
            self.head = Node(next_val)
    
    # returns the size of the list
    def size(self):
        current = self.head
        count=0
        # This would follow the linked list and count until we reach the end
        while (current != None):
            count+=1
            current = current.getNext()
        return count

    # look for the presence of the value in the list, if present, return True.
    def search(self, val):
        current = self.head
        # got through the unordered linked list and look for the presence of value
        while (current!= None):
            if (current.getData() == val):
                return True
            else:
                current = current.getNext()
        # if cannot find it anywhere in the list, return False
        return False

    # remove that value from the list
    def remove(self, val):
        if self.search(val) == False:
            raise ValueError('value not in the linked list')
        else:
            current = self.head
            previous = None
            found = False
            # got through the unordered linked list and look for the presence of value
            while (found == False):
                if (current.getData() == val):
                    found = True
                    #set the previous to point to the one after Next, skipping over Next, this is essentially deleting Next off the list
                    previous.setNext(current.getNext())
                    current.setNext=None
                else:
                    previous = current
                    current = current.getNext()
    # get the values in the whole list and return the list
    def getList(self):
        current = self.head
        val_list = []
        while (current != None):
            val_list.append(current.getData())
            current = current.getNext()
        return val_list

    # pop out the current head (last item added)
    def pop(self):
        val = self.head.getData()
        next_node = self.head.getNext()
        self.head = next_node
        return val

