def pyramid(rows):
    for i in range(1, rows + 1):
        print(("*" * (2 * i - 1)).center(2 * rows - 1))

# Example: Print a pyramid with 5 rows
rows = int(input("Enter the number of rows: "))
pyramid(rows)
#pyramid 
