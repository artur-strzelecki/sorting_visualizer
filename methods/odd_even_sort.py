def odd_even_sort(numbers):
    sort = False
    while sort is False:
        sort = True
        for i in range(0, len(numbers) - 1, 2):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                sort = False
                yield numbers

        for i in range(1, len(numbers) - 1, 2):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                sort = False
                yield numbers
