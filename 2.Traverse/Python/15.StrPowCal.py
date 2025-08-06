def str_Pow_Cal(str):
  vowels = "AEIOUaeiou"

  X= 0
  Y = 0

  for i in str:
    if i in vowels:
      X += 1
    else:
      Y += 1

  cal = 3*X + 5*Y
  return cal
      
    
N = 4
str = "aman"
res = str_Pow_Cal(str)
print(res)