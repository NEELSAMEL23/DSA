
def verifySubsequence(s,t):
    while i < len(s) and j < len(t):
      if s[i] == s[j]:
        i+=1
      j+=1

    if(i == len(s)):
      print("true")
    else:
      print('false')
  




s = "abc"
t = "ahbgdc"
res = verifySubsequence(s,t)
print(res)