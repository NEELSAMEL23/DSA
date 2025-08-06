# Function to calculate the square of a number with type annotation
def square(num: int) -> int:
    return num * num

# Declare a number variable
num: int = 7

# Store the result from the square function
res: int = square(num)

# Print the result
print(res)  # Output: 49
