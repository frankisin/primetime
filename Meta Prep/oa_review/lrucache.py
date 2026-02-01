def solution(queries):
    class Node:
        def __init__(self,key,val):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None 
    class LRUCache:
        def __init__(self,capacity):
            self.capacity = capacity
            self.cache = {} #key : node 

            self.head = Node(0,0)
            self.tail = Node(0,0)

            self.head.next = self.tail
            self.tail.prev = self.head
        
        def remove(node):
            prev_node = node.prev
            next_node = node.next

            prev_node.next = next_node
            next_node.prev = prev_node
        def insert(self,node):
            node.prev = self.head
            node.next = self.head.next

            self.head.next.prev = node
            self.head.next = node 

        def get(self,key):
            if key in self.cache:
                node = self.cache[key]
                value = node.val
                self.insert(node)
                self.remove(node)

                return value
            else:
                return ""
        def put(self,key,val):

            if self.capacity == 0: 
                return

            if key in self.cache:
                #update the value
                node = self.cache[key]
                del self.cache[key]
                mru = Node(key,val)
                self.cache[key] = mru

                self.remove(node)
                self.insert(mru)
            else:
                capacity = self.capacity
                if len(self.cache) >= capacity:
                    lru = self.tail.prev
                    del self.cache[lru.key]
                    self.remove(lru)
                #insert new key 
                node = Node(key,val)
                self.cache[key] = node
                self.insert(node)

                

