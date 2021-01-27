class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
		self.current = None
		
    def create_root(self):
	self.current = Node(self.data)
		
    def create_left_child(self):
	self.current = Node(self.data).self.left
		
    def create_right_child(self):
	self.current = Node(self.data).self.right
	
current = None	
data = int(input("Enter the data for root node: "))
new_node = Node(data)
new_node.create_root()

while True:
    ans = input("Wanna add more nodes? ")
    if ans == 'n':
        break
		
    which_child = int(input("Enter 1 Create Left Child and 2 for Right Child: "))
	
    if which_child == 1:
        left_child = int(input("Enter the data for left child: "))
        new_node = Node(left_child)
        new_node.create_left_child()
		
    if which_child == 2:
	right_child = int(input("Enter the data for right child: "))
	new_node = Node(right_child)
	new_node.create_right_child()
		
