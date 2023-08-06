# Spiral Traversal
# Expected Output: [[1, 2, 3], [6, 9, 8], [7, 4, 5]]

def spiral(rows, columns, matrix) :
    k = 0; l = 0
    arr =[]
    while (k < rows and l < columns) :
        for i in range(l, columns) :
            arr.append(matrix[k][i])

        k += 1

        for i in range(k, rows) :
            arr.append(matrix[i][columns - 1])

        columns -= 1

        if ( k < rows) :

            for i in range(columns - 1, (l - 1), -1) :
                arr.append(matrix[rows - 1][i])

            rows -= 1

        if (l < columns) :
            for i in range(rows - 1, k - 1, -1) :
                arr.append(matrix[i][l])

            l += 1

    print (arr)
