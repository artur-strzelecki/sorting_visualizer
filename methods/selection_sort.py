def selection_sort(numbers):
    length_array = len(numbers)

    for i in range(length_array - 1):
        min_value = i

        # find a index with least value
        for k in range(i + 1, length_array):
            if numbers[k] < numbers[min_value]:
                min_value = k

        if min_value != i:
            numbers[min_value], numbers[i] = numbers[i], numbers[min_value]
            
        yield numbers
