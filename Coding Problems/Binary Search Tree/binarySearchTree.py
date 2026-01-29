class Node:  
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.head = None
    def addNode(self,value):
        if self.head is None:
            self.head = Node(value=value)
        else:
            self.add(self.head,value)
    def add(self,current,value):
        if(current.value > value):
            if current.left is None:
                current.left = Node(value=value)
            else:
                self.add(current.left,value)
        else:
            if current.right is None:
                current.right = Node(value=value)
            else:
                self.add(current.right,value)
    def dfs(self,node):
        if node:
            self.dfs(node.left)
            print(node.value)
            self.dfs(node.right)
    def search(self,node,target):

        if node is None:
            return None
        if node.value == target: #weve found our target
            return node.value
        if node.value > target:
            return self.search(node.left,target=target)
        elif node.value < target:
            return self.search(node.right,target=target)
        
    def dfs_search(self,node,target):
        if node is None:
            return None 

        left_subtree = self.dfs_search(node.left,target=target)
        if left_subtree:
            return left_subtree

        if node.value == target:
            return node
    
        return self.dfs_search(node.right,target=target)
    