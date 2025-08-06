# Combined upper and lower part
n = 5  # Number of rows for the upper half

for i in range(2 * n + 1):
    res = ""
    
    # Determine the current row index (mirroring for lower part)
    if i <= n:
        current = i  # Upper part
    else:
        current = 2 * n - i  # Lower part
    
    # Adding spaces
    for j in range(n - current):    
        res += "  "
    
    # Increasing numbers
    for j in range(current + 1):
        res += str(j) + " "
    
    # Decreasing numbers            
    for j in range(current - 1, -1, -1):
        res += str(j) + " "
    
    print(res)
