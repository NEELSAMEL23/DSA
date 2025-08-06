def  shiftingCharacters(n,s,k):
  result = []
  
  for char in s:
    new_char = chr( ((ord(char) - ord('a') + k) % 26) + ord('a')) 
    
    result.append(new_char)
  
  return "".join(result)



n = int(input())
s = str(input())
k = int(input())

res = shiftingCharacters(n,s,k)
print(res)