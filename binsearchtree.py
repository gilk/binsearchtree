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
	
	def filltree(self,listob):
		for i in listob:
			self.add_node(i)
	
	def printsort(self,node):
		
		if node is not None:
			
			self.printsort(node.left)
			print node.value
			self.printsort(node.right)

#to print as list	
	def recsort(self,node,lis):
		if node is not None:
			
			self.recsort(node.left,lis)
			lis.append(node.value)
			self.recsort(node.right,lis)
		
	def sortprint(self,node):
		out =[]
		self.recsort(node,out)
		print out
			
		
    	
if __name__ == '__main__':
	t=BST()
	t.add_node('abe')
	t.add_node(3)
	t.add_node(3.2)
	t.add_node('dad')
	t.add_node(12)
	t.printsort(t.root)
	
	g=BST()
	things=['abe','dad',3,4,5.3,58]
	g.filltree(things)
	g.printsort(g.root)
	g.sortprint(g.root)