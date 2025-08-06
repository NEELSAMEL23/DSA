def left_right_intersection():
  N = int(input())
  S = input().strip()
  
  A= [0]
  
  for i in range(1,N+1):
    
    pos = A.index(i-1)

    if S[i-1]=='L':
      A.insert(pos,i)
    else:
       A.insert(pos+1,i)
      
  
  print(' '.join(map(str,A)))
  
left_right_intersection()