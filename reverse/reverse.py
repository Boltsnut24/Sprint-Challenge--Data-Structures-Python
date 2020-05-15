class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev=None):
        #empty
        if node is None:
            return None

        #base case
        if node.next_node is None:
            return node
        
        #set head as prev pointer, new_head as rest of list
        head = node
        new_head = head.next_node

        #recursive call, passing in next node in list
        future_head = self.reverse_list(new_head)

        #flip pointer around towards previous node
        new_head.next_node = head

        #set new_head as result of recursive call
        new_head = future_head
        self.head = new_head

        return new_head




        
  
