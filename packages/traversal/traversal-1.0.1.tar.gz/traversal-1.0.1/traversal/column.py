# Column Order Traversal
# Expected Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

def column(rows, columns, matrix):
    arr = []
    for i in range(rows):
        for j in range(rows):
            arr.append(matrix[j][i])
    print (arr)
