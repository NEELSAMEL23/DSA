def check_largest_odd_frequency(test_cases):
    for _ in range(test_cases):
        # Read the size of the matrix
        N = int(input())
        
        # Initialize arrays to store left diagonal and right diagonal elements
        left_diag = []
        right_diag = []
        
        # Read the matrix
        matrix = []
        for i in range(N):
            row = list(map(int, input().split()))
            matrix.append(row)
            # Left diagonal: elements where row == col
            left_diag.append(row[i])
            # Right diagonal: elements where row + col == N - 1
            right_diag.append(row[N - i - 1])
        
        # Combine both diagonals
        combined_diags = left_diag + right_diag
        
        # Find the maximum element in combined diagonals
        max_elem = max(combined_diags)
        
        # Count the frequency of the maximum element
        max_count = combined_diags.count(max_elem)
        
        # Check if the frequency is odd
        if max_count % 2 == 1:
            print("yes")
        else:
            print("no")

# Input number of test cases
T = int(input())
check_largest_odd_frequency(T)
