"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):  # TODAY
        if value < self.value:  # the value belongs on the left of the tree
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:  # the value belongs on the right of the tree
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):  # TODAY
        if self.value == target:  # the current node is on target
            return True
        elif target < self.value:  # the target belongs on the left branch
            if not self.left:  # there exists no left branch
                return False
            else:
                return self.left.contains(target)
        elif target > self.value:  # the target belongs on the right branch
            if not self.right:  # there exists no right branch
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):  # TODAY
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node

    def for_each(self, fn):  # TODAY
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:  # start with left child
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        print(self.value)
        if self.left:
            self.left.pre_order_dft()
        if self.right:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        if self.left:
            self.left.post_order_dft()
        if self.right:
            self.right.post_order_dft()
        print(self.value)
