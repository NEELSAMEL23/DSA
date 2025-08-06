def solve(a,b,c,d):
  
  if(b - a == c- b == d - c):
    print("Arithmetic")
  elif(b/a == c/b == d/c):
    print("Geometric")
  else:
    print("Neither")
  