def excel_column_number(column_title):
    column_number = 0
    for char in column_title:
        # Calculate the value of each character and add it to the column_number
        column_number = column_number * 26 + (ord(char) - ord('A') + 1)
    return column_number


column_title = "AB"
column_title = "ZY"
res = excel_column_number(column_title)
print(res)