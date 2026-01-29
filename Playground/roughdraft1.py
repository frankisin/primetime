class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None 

class BinarySearchTree:
    def __init__(self):
        self.head = None 
    def addNode(self,value):
        if self.head is None:
            self.head = Node(value)
        else:
            self.add(self.head,value)
    def add(self,current,value): 
        if current.value > value:       #current node's value is greater than node we are trying to add...
            if current.left is None:    #if current.left is empty we add the node to empty branch
                current.left = Node(value)
            else:
                self.add(current.left,value)
        else:                           #current node's value is less than node we are trying to add..
            if current.right is None:   #if current.right is empty we add the node to empty branch 
                current.right = Node(value)
            else:
                self.add(current.right,value)
    def dfs(self,node):
        if node:
            self.dfs(node.left)
            print(node.value)
            self.dfs(node.right)
    def height(self,node):
        if node is None:
            return -1

        leftHeight = self.height(node.left)
        rightHeight = self.height(node.right)

        return 1 + max(leftHeight,rightHeight)
    def leaves(self,node):
        leaves = [] #empty array to store leaves

        def dfs_leaf(node,leaves):
            if node is None:
                return None
            
            if node.left is None and node.right is None:
                leaves.append(node.value)
                print('Leaf found, appending: ',node.value)
            
            dfs_leaf(node.left,leaves)
            dfs_leaf(node.right,leaves)
        
        dfs_leaf(node,leaves)
        return leaves 
    
bst = BinarySearchTree()
bst.addNode(1)
bst.addNode(2)
bst.addNode(3)
bst.addNode(10)
bst.addNode(5)
bst.addNode(15)
bst.addNode(2)
bst.addNode(7)
bst.addNode(12)
bst.addNode(17)

#bst.dfs(bst.head)


#height = max(leftHeight,rightHeight)
print(bst.height(bst.head))


            



