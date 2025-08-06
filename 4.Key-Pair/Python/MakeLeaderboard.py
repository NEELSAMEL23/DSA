def make_leaderboard():
    n = int(input())
    students = []

    for _ in range(n):
        name, mark = input().split()
        students.append((name, int(mark)))

    # Sort by (-marks, name)
    students.sort(key=lambda x: (-x[1], x[0]))

    rank = 1
    output = []
    prev_mark = None
    count_same = 0

    for i, (name, mark) in enumerate(students):
        if mark == prev_mark:
            # Same rank as before
            output.append((rank, name))
            count_same += 1
        else:
            # New mark, update rank considering previous duplicates
            rank = rank + count_same
            output.append((rank, name))
            count_same = 1
            prev_mark = mark

    # Print the result
    for r, name in output:
        print(r, name)

# Run the function
make_leaderboard()
