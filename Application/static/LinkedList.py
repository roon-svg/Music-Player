class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)
        
    def get_head_node(self):
        return self.head_node
    
    def prepend(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    
    def append(self, new_value):
        new_node = Node(new_value)
        
        head = self.head_node # first variable
        current = head

        # loops to the end of the linked list
        while current.next_node != None: 
            current = current.next_node
    
        current.set_next_node(new_node) # the append statement!