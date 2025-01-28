def restore_matrix(upper_triangle):
    n = 0
    length = len(upper_triangle)
    
    while n * (n + 1) // 2 < length:
        n += 1
    
    matrix = [[0] * n for _ in range(n)]
    index = 0
    
    for i in range(n):
        for j in range(i, n):
            matrix[i][j] = upper_triangle[index]
            matrix[j][i] = upper_triangle[index]  
            index += 1
            
    return matrix

upper_triangle = [1, 2, 3, 4, 5, 6] 
matrix = restore_matrix(upper_triangle)

print("Восстановленная матрица:")
for row in matrix:
    print(row)

# вторая задача 
def diagonal_elements_and_trace(matrix):
    n = len(matrix)
    diagonal_elements = []
    trace = 0
    
    # формирование одномерного массива диагональных элементов
    for i in range(n):
        diagonal_elements.append(matrix[i][i])
        trace += matrix[i][i]  # суммируем
    
    transformed_matrix = [row[:] for row in matrix] 
    for i in range(n):
        if i % 2 == 0:  
            for j in range(n):
                transformed_matrix[i][j] /= trace
                
    return diagonal_elements, trace, transformed_matrix

matrix = [[1, 2, 3],
          [2, 5, 6],
          [3, 6, 4]]

diagonal_elements, trace, transformed_matrix = diagonal_elements_and_trace(matrix)

print(f"\nДиагональные элементы: {diagonal_elements}")
print(f"След матрицы: {trace}")
print("Преобразованная матрица:")
for row in transformed_matrix:
    print(row)
   