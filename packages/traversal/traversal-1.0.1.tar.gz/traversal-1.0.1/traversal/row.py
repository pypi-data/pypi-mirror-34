# Row Order Traversal
# Expected Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def row(rows, columns, matrix):
    arr = []
    for i in range(rows):
        for j in range(rows):
            arr.append(matrix[i][j])
    print (arr)