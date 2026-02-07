def solution(queries):
   out = []
   lru = None
   
   class Node:
      def __init__(self, key, value):
          self.key = key
          self.val = value
          self.next = None
          self.prev = None 
          
   class LRUCache:
      def __init__(self, capacity):
          self.capacity = capacity
          self.cache = {} #key : node

          self.head = Node(0,0)
          self.tail = Node(0,0)

          #link tail and head
          self.head.next = self.tail
          self.tail.prev = self.head

      def insert(self,node):
          node.prev = self.head
          node.next = self.head.next
          self.head.next.prev = node
          self.head.next = node  
      def remove(self,node):
          prev_node = node.prev
          next_node = node.next 
          prev_node.next = next_node
          next_node.prev = prev_node
      def get(self,key):
          if key in self.cache:
              node = self.cache[key]
              self.remove(node)
              self.insert(node)

              return node.val
          else:
              return ""
      def put(self,key,value):
          
          if self.capacity == 0:
              return 

          if key in self.cache:
              node = self.cache[key]
              node.val = value

              self.remove(node)
              self.insert(node)
          else:
              node = Node(key,value)
              if len(self.cache) < self.capacity:
                  self.cache[key] = node
                  
              else:
                  lru = self.tail.prev
                  del self.cache[lru.key]
                  self.remove(lru)
                  self.cache[key] = node

              self.insert(node)    

   for q in queries:
        op = q[0] 
        if op == "INIT":

            cap = int(q[1]) #capacity
            lru = LRUCache(cap)
            out.append("true")
        elif op == "PUT":
            key = q[1]
            val = q[2]

            lru.put(key,val)
            out.append("true")
        elif op == "GET":
            key = q[1]
            res = lru.get(key)
            out.append(res)

   return out 
            
queries = [
  ["INIT", "2"],
  ["PUT", "a", "1"],
  ["PUT", "b", "2"],
  ["GET", "a"],      # makes a MRU
  ["PUT", "c", "3"], # should evict b
  ["GET", "b"],      # should be ""
  ["GET", "a"],      # "1"
  ["GET", "c"]       # "3"
]

print(solution(queries))




            

                
            
                
            
            
            
            
                

                
                
                

            

            






