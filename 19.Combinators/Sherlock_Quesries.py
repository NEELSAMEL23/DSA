def count_odd_elements_after_queries(n, m, queries):
    row_increments = [0] * n
    col_increments = [0] * m
    
    for query_type, index in queries:
        if query_type == 0:
            row_increments[index] += 1
        elif query_type == 1:
            col_increments[index] += 1
    
    odd_rows = sum(1 for r in row_increments if r % 2 != 0)
    odd_columns = sum(1 for c in col_increments if c % 2 != 0)
    
    odd_count = odd_rows * m + odd_columns * n - 2 * odd_rows * odd_columns
    return odd_count


n = 2
m = 2
queries = [(0, 1), (0, 0), (0, 0), (1, 1)]
result = count_odd_elements_after_queries(n, m, queries)
print(result)  # Outputs the result based on inputs
