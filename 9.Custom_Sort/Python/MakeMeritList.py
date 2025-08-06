def sort_students(n, student_data):
    students = []

    for data in student_data:
        name, h, w, iq = data.split()
        students.append((int(iq), int(h), int(w), name))

    # Sort by: IQ desc, Height desc, Weight asc, Name asc
    students.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))

    # Print top 8 student names
    for i in range(min(8, n)):
        print(students[i][3])


n = int(input())
student_data = [input().strip() for _ in range(n)]
sort_students(n, student_data)
