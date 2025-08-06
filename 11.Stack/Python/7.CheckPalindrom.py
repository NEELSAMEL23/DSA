def is_palindrome(s):
  stack = []

    # Push all characters of the string onto the stack
  for char in s:
      stack.append(char)
  
  # Pop characters from the stack and form the reversed string
  reversed_s = ""
  while stack:
      reversed_s += stack.pop()
  
  # Compare the original string with the reversed string
  if s == reversed_s:
      return "YES"
  else:
      return "NO"
        



string = "vtmtmv"
N = 3
res = is_palindrome(s)

print(res)