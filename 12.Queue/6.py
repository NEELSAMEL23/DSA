class QueueUsingStacks:
    def __init__(self):
        self.S1 = []
        self.S2 = []

    def push(self, x):
        while self.S1:
            self.S2.append(self.S1.pop())
        self.S1.append(x)
        while self.S2:
            self.S1.append(self.S2.pop())

    def pop(self):
        if self.S1:
            return self.S1.pop()
        return None

    def front(self):
        if self.S1:
            return self.S1[-1]
        return None



def implement_queue(queries):
    q = QueueUsingStacks()
    result = []
    for query in queries:
        if query[0] == 0:
            q.push(query[1])
        elif query[0] == 1:
            result.append(q.front())
        elif query[0] == 2:
            q.pop()
    return result


n = int(input())
queries = []
for _ in range(n):
  queries.append(list(map(int, input().split())))


output = implement_queue(queries)

for value in output:
    print(value)
