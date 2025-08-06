def solve(n,m,prerequisites):
  
  adj_list = {i :[] for i in range(n)}
  in_degree = {i :0 for i in range(n)}
  
  for a ,b in prerequisites:
    adj_list[b].append(a)
    in_degree[a] += 1
    
  
  queue = []
  
  for node in in_degree:
    
    if in_degree[node] == 0:
      queue.append(node)
  
  visited_count = 0
  
  while queue:
    cource = queue.pop(0)
    
    visited_count += 1
    
    for neighbor in adj_list[cource]:
      in_degree[neighbor] -= 1
      if in_degree[neighbor] == 0:
        queue.append(neighbor)
  
  print("Yes" if visited_count == n else "No")
      