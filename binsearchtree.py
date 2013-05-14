class Node:
	
	def __init__(self,value):
		
		self.left = None
		self.right = None
		self.value = value

class BST:
	
	def __init__(self):

		self.root = None
	
	def add_node(self,val):
		
		if self.root == None: self.root = Node(val)
		else:
			
			current = self.root
			
			while True:
				
				if val < current.value:
					
					if current.left: current = current.left
					else:
						current.left = Node(val)
						break
				elif val > current.right:
					
					if current.right: current = current.right
					else: 
						current.right = Node(val)
						break
						
				else: break #ignore duplicate entries
	

	
	def inorder(self,node):
		
		if node is not None:
			
			self.inorder(node.left)
			print node.value
			self.inorder(node.right)
    	
if __name__ == '__main__':
	t=BST()
	t.add_node(5)
	t.add_node(3)
	t.add_node(2)
	t.add_node(12)
	t.inorder(t.root)