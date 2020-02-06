# Nodes and Linked Lists
## Description
Node points to the address of the next node. Linked lists are lists of nodes. Linked list can be unordered or ordered. Here, a node class and unordered linked list class are implemented in Python
## Content
* node.py: contains the Node class
    * setData(new_val) : set the value of this node
    * setNext(next_node) : set the node this node will points to
    * getData() : returns the value of this node
    * getNext() : returns the node that this node is pointing to
* unordered_linked_list.py: contains the unordered linked list class
    * add(next_val) : add a node with value set to next_val to the list
    * size() : returns the size of the list
    * search(val) : searches for the presence of the value, returns True if val present, False if not
    * remove(val) : remove val from the list
    * getList() : returns a list that has all the values in the list
    * pop() : pops out the head of the list (the one most recently added)

## Testing
* Node :
```python
node1 = Node(93) # make a new node with value 93
print(node1.getData()) # should be 93
node2= Node(22)
node1.setNext(node2)
print(node1.getNext().getData()) # should be 22
```
* UnorderedList :
```python
ul = UnorderedList() # make a new unordered list
ul.add(31) # add node with value 31 to list
ul.add(77) # add node with value 77 to list
ul.add(17) # add node with value 17 to list
ul.add(93) # add node with value 93 to list
print(ul.size()) # should be 4
print(ul.search(17)) # should return True
ul.remove(17) # 17 should be removed
print(ul.size()) # should now be 3
print(ul.getList()) # should be 93,77,31
print(ul.pop()) # pop out 93
print(ul.getList()) # should be 77,31
```