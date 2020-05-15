import time

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
 
        #Value is less than current node
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        
        #Value is greater than OR EQUAL TO current node
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #Base case
        if target == self.value:
            return True
        
        #left traversal
        elif target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)

        #right traversal
        elif target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)

        #was not found
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is not None:
            return self.right.get_max()
        
        return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left is not None:
            self.left.for_each(fn)

        if self.right is not None:
            self.right.for_each(fn)
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        #check if it has children
        if node.left is not None and node.right is not None:
            print(node.value)
            return
        
        if node.left is not None:
            self.in_order_print(node.left)

        if node.right is not None:
            self.in_order_print(node.right)
        

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
#for name_1 in names_1:
#    for name_2 in names_2:
#        if name_1 == name_2:
#            duplicates.append(name_1)
tree = BSTNode('M')
#build tree with names, as we do, check for duplicates and add to final list
for x in names_1:
    if tree.contains(x):
        duplicates.append(x)
    else:
        tree.insert(x)

for y in names_2:
    if tree.contains(y):
        duplicates.append(y)
    else:
        tree.insert(y)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
