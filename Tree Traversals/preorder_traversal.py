# Group Members:
# Caleb Mabuka: CIT-227-030/2021
# Joram Kariuki: CIT-227-009/2021
# JohnMark Wanjugu: CIT-227-008/2021
# Thorne Musau: CIT-227-029/2021

# Traversal:
# Root --> Left --> Right

# A class that represents an individual node
# in a Binary Tree
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


# A function to do postorder tree traversal
def printPostorder(root):

	if root:

		# First recur on left child
		printPostorder(root.left)

		# The recur on right child
		printPostorder(root.right)

		# Now print the data of node
		print(root.val, end=" "),


# Driver code
if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.right = Node(4)
	root.right.left = Node(5)
	root.right.right = Node(6)
	root.right.left.left = Node(7)
	root.right.right.left = Node(8)
	root.right.right.right = Node(9)

	# Function call
	print("Postorder traversal of binary tree is")
	printPostorder(root)
