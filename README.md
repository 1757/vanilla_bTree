# vanilla_bTree
A simple python bTree implementation and some experiment
This short piece of code is the implementation of a binary tree, containing 1 class Btree with 10 methods, including a bread-first-search traversal method

Testing the tree and search experiments is done below in the __main__ programme (tree and experiment result is in this Readme)



######################-------------------EXPERIMENT Check----------------------------------------################################
The tree structure is in the PNG file (just open the image for the intended tree structure, or else it's fairly easy to know which node is what). 

for example, 

Root = root node
R = right node of root
L = left node of root
RR = right node of R
RL = left node of R
and so on

##############------------------------ In which ----------------------------
(breadth first search code)
['RRR', 'RLR', 'RR', 'RL', 'LR', 'R', 'L', 'root node']
 Order of running has to fulfil: 
------------------- RRR before RR (checked)
------------------- RLR before RL (checked)
--------------------RL and RR before R (checked)
--------------------LR before L (checked)
------------------- R and L before Root (checked)


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
