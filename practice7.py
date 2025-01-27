def sum_and_product(arr):
    total_sum = 0
    total_product = 1
    has_odd_index_elements = False  # проверим наличие элементов с нечетными индексами

    for index in range(len(arr)):
        if index % 2 == 0:  # Четный индекс
            total_sum += arr[index]
        else:  # Нечетный индекс
            total_product *= arr[index]
            has_odd_index_elements = True

    if not has_odd_index_elements:  # Если нет элементов с нечетными индексами, возвращаем 0
        total_product = 0

    return total_sum, total_product

arr1 = [1, 2, 3, 4, 5]
result_sum, result_product = sum_and_product(arr1)
print(f'Сумма элементов с четными индексами: {result_sum}')
print(f'Произведение элементов с нечетными индексами: {result_product}') 


def swap_min_max(arr):
    if not arr:  # Проверка на пустой массив
        return arr

    min_index = arr.index(min(arr))
    max_index = arr.index(max(arr))

    # Меняем местами минимальный и максимальный элементы
    arr[min_index], arr[max_index] = arr[max_index], arr[min_index]
    
    return arr

arr2 = [6, 8, 4, 1, 4]
swapped_arr = swap_min_max(arr2)
print(f'Массив после замены значений min и max: {swapped_arr}') 
