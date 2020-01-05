import time

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

start_time = time.time()



f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
name_tree = BinarySearchTree(names_2[0])
# this loop add each name to my binary search tree. 
for name in names_1:
    print(name)
    name_tree.insert(name)
# this loops checks to see if the name is contained in binary tree and if it is it adds the name to the duplicate list
for name in names_2:
    if name_tree.contains(name):
        duplicates.append(name)

end_time = time.time()

print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
# runtime went from 12 seconds to runtime: 0.8125858306884766 seconds

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
