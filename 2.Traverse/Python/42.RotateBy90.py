def rotate_90(matrix,N):
  arr2 = []
  for col in  range(N-1,-1,-1):
      arr1 = []
      for row in range(N):
          arr1.append(matrix[row][col])
      arr2.append(arr1)
  
  for i in arr2:
    print(" ".join(map(str,i)))

matrix = [ 
          [1,2,3,4], 
          [5,6,7,8] , 
           [1,2,3,4], 
          [5,6,7,8] , 
          ] 
N = 4
rotate_90(matrix,N)