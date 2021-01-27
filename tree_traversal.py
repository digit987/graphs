class Node:
	
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data
	
def preOrder(root):
	if root:
		print(root.data)
		preOrder(root.left)
		preOrder(root.right)
	
def inOrder(root):
	if root:
		inOrder(root.left)
		print(root.data)
		inOrder(root.right)
	
def postOrder(root):
	if root:
		postOrder(root.left)
		postOrder(root.right)
		print(root.data)
		
def level_traversal(root):
	queue = []
	current = root
	queue = [current.data]
	while current is not None:
		print(current.data)
		print(queue)
		queue.extend([current.left.data, current.right.data])
		print(queue)
		del queue[0]
		current = Node(queue[0])
		print(queue)
	
		
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
'''
print('Pre-Order Traversal')
preOrder(root)
print('In-Order Traversal')
inOrder(root)
print('Post-Order Traversal')
postOrder(root)
'''
level_traversal(root)
