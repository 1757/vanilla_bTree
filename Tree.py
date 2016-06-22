###############------------------------ Author: Stephen Vu Xuan Kim Cuong---------------------------------------
###############--------------------Contact me at kimcuong_vu@mymail.sutd.edu.sg---------------------------------------

from threading import Thread
import time

class bTree:
	def __init__(self, root_node_name):
		#each node is defined by {nodename: [parent_node, left_child, right_child, level]}, will be added to node_dict (faster to find node by name)
		self.node_dict = {}
		self.node_count = 1

		self.root_node_name = root_node_name
		self.node_dict[root_node_name] = [None, None, None, None]
		self.node_dict[root_node_name][3] = self.tree_level(root_node_name)
		#The last parameter is used for bread-first-search. Basically it create the order in which the task execute. 
		self.revtasklist = []

	#this method is used to print out the whole tree dictionary
	def print_tree(self):
		print "list of nodes currently in the tree"
		for key, value in self.node_dict.iteritems():
			print key, value
		print "----------------"

	def add_left_node(self, parent, node_name):
		if node_name not in self.node_dict:
			if not self.node_dict[parent][1]:
				#change the parameter "left" of the parent node to "node_name"
				self.node_dict[parent][1] = node_name
				#add the key node_name into the dictionary
				self.node_dict[node_name] = [parent, None, None, None]
				#calculate the level of the tree
				self.node_dict[node_name][3] = self.tree_level(node_name)
				self.node_count += 1
				print "left node \"%s\" added to parent \"%s\"" %(node_name, parent)
			else: 
				print "left node of parent already exists"
		else:
			print "name already exists"

	def add_right_node(self, parent, node_name):
		if node_name not in self.node_dict:
			if not self.node_dict[parent][2]:
				self.node_dict[parent][2] = node_name
				self.node_dict[node_name] = [parent, None, None, None]
				self.node_dict[node_name][3] = self.tree_level(node_name)
				self.node_count += 1
				print "right node \"%s\" added to parent \"%s\"" %(node_name, parent)
			else: 
				print "right node of parent already exists"
		else:
			print "name already exists"

	def tree_level(self, node_name):
		# a recursive way to return level of specific node
		if node_name in self.node_dict:
			if not self.node_dict[node_name][0]:
				return 0
			else:
				return bTree.tree_level(self, self.node_dict[node_name][0]) + 1
		else:
			return "node does not exist"

	def remove_node(self, node_name):
		# a recursive way to remove a node and all its branches
		if not self.node_dict[node_name][1] and not self.node_dict[node_name][2]:
			#set the parent node's respective 'children' parameter to None
			self.node_dict[self.node_dict[node_name][0]] = map(lambda x: None if (x == node_name) else x, self.node_dict[self.node_dict[node_name][0]])
			del self.node_dict[node_name]
		elif self.node_dict[node_name][1]:
			bTree.remove_node(self, self.node_dict[node_name][1])
			bTree.remove_node(self, node_name)
		else:
			bTree.remove_node(self, self.node_dict[node_name][2])
			bTree.remove_node(self, node_name)

	def get_left_name(self, node_name):
		return self.node_dict[node_name][1]

	def get_right_name(self, node_name):
		return self.node_dict[node_name][2]

	def check_exist(self, node_name):
		if node_name in self.node_dict:
			return "node exists"
		else:
			return "node does not exist"

	def get_parent(self, node_name):
		return self.node_dict[node_name][0]

	def inverse_bfs(self):
		#bfs
		q = [self.root_node_name]
		queue_list = []
		while q:
			element = q.pop(0)
			if self.node_dict[element][1]:
				q.append(self.node_dict[element][1])
			if self.node_dict[element][2]:
				q.append(self.node_dict[element][2])
			queue_list.append(element)
		queue_list.reverse()
		return queue_list


	#def no_parent_list(self):


#----code for testing the trees and its feature, running the tree, parallelize the processes------
if __name__ == "__main__":

	#Testing the tree with easy-to-see names : e.g root = root node, right of root node = R, left of right of root node = RL, etc... The task test would be the same too
	#uncomment the print method to see the tree's evolution
	an_instance = bTree("root node")
	#an_instance.print_tree()

	an_instance.add_right_node(parent ="root node", node_name = "R")
	#an_instance.print_tree()

	an_instance.add_left_node("root node", "L")
	#an_instance.print_tree()

	an_instance.add_left_node("R", "RL")
	#an_instance.print_tree()

	an_instance.add_right_node("RL", "RLR")
	#an_instance.print_tree()

	an_instance.add_right_node("R", "RR")
	#an_instance.print_tree()

	an_instance.add_right_node("RR", "RRR")
	#an_instance.print_tree()

	an_instance.add_right_node("L", "LR")
	an_instance.print_tree()
	print an_instance.node_count
	##Uncomment this code to remove 

	#print an_instance.tree_level("RR")
	#time.sleep(12)
	#An easiest way to traverse the list is using bread-first-search, then invert the order

	####----------Define task functions that corresponds to the list
	def func1():
		print "root started"
		time.sleep(3)
		print "root finished"

	def func2():
		print "R started"
		time.sleep(2)
		print "R finished"
	def func3():
		print "L started"
		time.sleep(4)
		print "L finished"

	def func4():
		print "RL started"
		time.sleep(3)
		print "RL finished"

	def func5():
		print "RLR started"
		time.sleep(2.5)
		print "RLR finished"

	def func6():
		print "RR started"
		time.sleep(2)
		print "RR finished"

	def func7():
		print "RRR started"
		time.sleep(5)
		print "RRR finished"

	def func8():
		print "LR started"
		time.sleep(2)
		print "LR finished"

	#initialize a dictionary that contains name of nodes and the function it supposed to run
	run_dict = {"root node": func1, "R": func2, "L": func3, "RL": func4, "RLR": func5, "RR": func6, "RRR": func7, "LR": func8}
	#print run_dict["root node"]()
	
	##-------Now, try to run the code according to the bread-first-search, uncomment to run, but the order is pretty obvious because it just follow the list "order" below
	print "------------------------------------------------------"
	order = an_instance.inverse_bfs()
	print "BFS outcome"
	print order
	for i in xrange(len(order)):
		run_dict[order[i]]()
	### Threading and parallelizing the tasks
	#first, initialized a status dictionary (since threading is being done)
	run_status = {}
	for i in xrange(len(order)):
		run_status[order[i]] = "NOT RUNNING"

	#A 2 functions that does the threading

	#firstly, run through the whole list and check if the tasks' have runned
	#find out the "no_children :(" tasks:
	print "----------------------------------"
	print "Threading outcome"
	for i in xrange(len(order)):
		#attempt to run
		left_child = an_instance.get_left_name(order[i])
		right_child = an_instance.get_right_name(order[i])

		if not left_child and not right_child:
			run_attempt(order[i])

	#run until everything is done
	#print run_status


######################-------------------EXPERIMENT Check----------------------------------------################################
# The tree structure is below -------------------------------------
# 											Root
# 					L 											R
# 			None 		 LR 						RL 						RR		
# 												None 	RLR 			None 	RRR	

# ##############------------------------ In which ----------------------------
# (breadth first search code)
# ['RRR', 'RLR', 'RR', 'RL', 'LR', 'R', 'L', 'root node']
#  Order of running has to fulfil: 
# ------------------- RRR before RR (checked)
# ------------------- RLR before RL (checked)
# --------------------RL and RR before R (checked)
# --------------------LR before L (checked)
# ------------------- R and L before Root (checked)


######## Checking order of the threading 
###

# 1# RRR started
# 2# RLR started
# 3# LR started
# 4# LR finished
# 5# L started
# 6# RLR finished
# 7# RL started
# 8# RRR finished
# 9# RR started
# 10# RL finished
# 11# L finished
# 12# RR finished
# 13# R started
# 14# R finished
# 15# root started
# 16# root finished

###------------------- RRR finished before RR started (checked) (line 8, and 9)
###------------------- RLR finished before RL started (checked) (line 6, and 7)
###--------------------RL finished and RR finished before R started (checked) (line 10, 12, 13)
###--------------------LR finished before L started (checked) (line 4)
### -------------------R finished and L finished before Root started (checked)
