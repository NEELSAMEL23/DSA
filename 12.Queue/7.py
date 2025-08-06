class StackUsingQueue:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
     
        self.queue1.append(x)

    def pop(self):
     
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        
     
        popped_value = self.queue1.pop(0)
        
     
        self.queue1, self.queue2 = self.queue2, self.queue1
        
        return popped_value

    def top(self):
      
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        
        # Peek the last element
        top_value = self.queue1[0]
        
      
        self.queue2.append(self.queue1.pop(0))
        
   
        self.queue1, self.queue2 = self.queue2, self.queue1
        
        return top_value


q = int(input())
stack = StackUsingQueue()
    
for _ in range(q):
    query = list(map(int, input().split()))
    
    if query[0] == 0:
        stack.push(query[1])
    elif query[0] == 1:
        print(stack.top())
    elif query[0] == 2:
        print(stack.pop())


