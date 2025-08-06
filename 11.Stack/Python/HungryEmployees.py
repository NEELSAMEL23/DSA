from collections import deque

def hungry_employees(n, employees, meals):
    employees = deque(employees)
    meals = meals[::-1]  # Reverse meals so we can use it as a stack (top at end)
    
    attempts = 0  # Track failed matches in a row
    
    while employees and meals:
        if employees[0] == meals[-1]:
            employees.popleft()
            meals.pop()
            attempts = 0  # Reset attempts after a successful match
        else:
            employees.append(employees.popleft())
            attempts += 1
        
        if attempts == len(employees):  # No match in full cycle
            break
    
    return len(employees)

# Input Parsing Example
n = int(input())
employees = list(map(int, input().split()))
meals = list(map(int, input().split()))
print(hungry_employees(n, employees, meals))
