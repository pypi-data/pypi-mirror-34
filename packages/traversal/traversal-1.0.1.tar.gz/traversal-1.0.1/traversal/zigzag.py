# ZigZag Traversal
# Expected Output: [[1, 2, 4], [7, 5, 3], [6, 8, 9]]

def zigzag(rows, columns, matrix):

    arr = []
    solution = [[] for i in range(rows + columns - 1)]

    for i in range(rows):
        for j in range(columns):
            sum = i + j
            if(sum % 2 == 0):
                solution[sum].insert(0, matrix[i][j])
            else:
                solution[sum].append(matrix[i][j])

    for i in solution:
        for j in i:
            arr.append(j)

    print (arr)
