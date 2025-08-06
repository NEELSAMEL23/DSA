def solve_trapped_zeroes():
    try:
        n_str, m_str = input().split()
        n = int(n_str)
        m = int(m_str)
    except ValueError:
        print("Invalid input for n and m. Please provide two integers.")
        return

    matrix = []
    for _ in range(n):
        try:
            row_str = input().split()
            row = []
            if len(row_str) != m:
                print(f"Row has {len(row_str)} elements, but expected {m}. Please check input.")
                return

            for val_str in row_str:
                val = int(val_str)
                # Ensure matrix elements are binary (0 or 1)
                if val not in [0, 1]:
                    print(f"Invalid matrix value: {val}. Matrix elements must be 0 or 1.")
                    return
                row.append(val)
            matrix.append(row)
        except ValueError:
            print("Invalid input for matrix row. Please provide integers.")
            return

    trapped_zeroes_count = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                is_trapped = True

                if i > 0 and matrix[i-1][j] == 0:
                    is_trapped = False
                
                if i < n - 1 and matrix[i+1][j] == 0:
                    is_trapped = False
                
                if j > 0 and matrix[i][j-1] == 0:
                    is_trapped = False
                
                if j < m - 1 and matrix[i][j+1] == 0:
                    is_trapped = False
                
                if is_trapped:
                    trapped_zeroes_count += 1
    
    print(trapped_zeroes_count)

solve_trapped_zeroes()
