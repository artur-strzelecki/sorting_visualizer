def bubble_sort(numbers):
    length_array = len(numbers)
    swapped = True
    for i in range(length_array - 1):
        if not swapped:
            return
        swapped = False

        for j in range(length_array - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
            yield numbers

