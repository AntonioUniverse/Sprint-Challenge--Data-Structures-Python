class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next
  def __str__(self):
    return f'{self.value}, {self.next_node}'
class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    #make current nodes previous node the next node
    current= self.head
    prev = None

    while current:
      # get current's next node
      next_N = current.get_next()
      # set current's next node to pervious node
      current.set_next(prev)
      # set previous node to current node
      prev = current
      # set current to next node
      current = next_N
      # if there is a next_node had a next node set next_node set new next to next_node.next_node
      if next_N:
        next_N = next_N.get_next()
      
    self.head = prev
   

    
  
   
    
    
    

  def __str__(self):
    return f' head node: {self.head}, next: {self.head.next_node}'


