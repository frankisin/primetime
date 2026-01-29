class Customer:
    ID = 0 
    def __init__(self,ID:int)->None:
        self.ID = ID
        
class CustomerService:
    
    def __init__(self):
        self.requests = [] 
    
    
    def enqueue(self,customer:Customer):
        self.requests.append(customer) # add element to end of queue
    def dequeue(self):
        self.requests.pop(0) # remove first element of queue
    def peek(self):
        first = self.requests[0]
        return first.ID
    def is_empty(self):
        size = len(self.requests)
        if size < 1:
            return True
        else:
            return False

customerService = CustomerService()
customer = Customer(1)

customerService.enqueue(customer)
print(customerService.peek())
print(customerService.is_empty())



