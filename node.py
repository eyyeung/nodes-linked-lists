class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    # get the value stored in Node
    def getData(self):
        return self.value

    # get the next node
    def getNext(self):
        return self.next_node

    #val should be a value
    def setData(self,new_val):
        self.value = new_val

    #next should be a Node
    def setNext(self,next_node):
        self.next_node = next_node

#Testing the Node class

# node1 = Node(93)
# print(node1.getData()) # should be 93
# node2= Node(22)
# node1.setNext(node2)
# print(node1.getNext().getData()) # should be 22