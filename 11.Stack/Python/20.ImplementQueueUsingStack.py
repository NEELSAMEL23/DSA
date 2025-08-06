class QueueUsingStack:
    def __init__(self):
        self.S1 = []
        self.S2 = []

    def push(self, x):
        # Move all from S1 to S2
        while self.S1:
            self.S2.append(self.S1.pop())
        # Push new element to S1
        self.S1.append(x)
        # Move everything back to S1
        while self.S2:
            self.S1.append(self.S2.pop())

    def pop(self):
        if self.S1:
            self.S1.pop()

    def front(self):
        if self.S1:
            print(self.S1[-1])

# Hardcoded simulation
q = QueueUsingStack()

queries = [
    (0, 1),
    (0, 2),
    (0, 3),
    (1,),
    (2,),
    (1,)
]

for query in queries:
    if query[0] == 0:
        q.push(query[1])
    elif query[0] == 1:
        q.front()
    elif query[0] == 2:
        q.pop()
