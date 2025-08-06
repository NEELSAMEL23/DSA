def sort_students(students):
   
    students.sort(key=lambda x: (-x[1], x[0]))


N = int(input())

students = []

for _ in range(N):
    name, marks = input().split()
    students.append((name, int(marks)))


sort_students(students)


rank = 1
for i in range(N):
    if i > 0 and students[i][1] == students[i - 1][1]:
        print(f"{rank} {students[i][0]}")
    else:
        rank = i + 1
        print(f"{rank} {students[i][0]}")
