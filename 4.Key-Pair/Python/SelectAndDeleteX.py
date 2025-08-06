def solve_select_and_delete_x_hardcoded_examples():
    N_example = 6
    arr_example = [2, 2, 3, 3, 3, 5]

    print(f"Processing Array: {arr_example} (N={N_example})")

    total_sum = sum(arr_example)

    counts = {}
    for num in arr_example:
        counts[num] = counts.get(num, 0) + 1

    min_final_sum = total_sum

    for num_x in counts:
        sum_of_deleted_x = num_x * counts[num_x]

        current_final_sum = total_sum - sum_of_deleted_x

        if current_final_sum < min_final_sum:
            min_final_sum = current_final_sum

    print(f"Minimum Final Sum: {min_final_sum}")
    print("-" * 30)

if __name__ == '__main__':
    solve_select_and_delete_x_hardcoded_examples()
