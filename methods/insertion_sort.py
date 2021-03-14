def insertion_sort(numbers):
    for index, value in enumerate(numbers[1:]):
        swapped = False
        while index >= 0 and value < numbers[index]:
            numbers[index + 1] = numbers[index]
            index -= 1
            swapped = True

        if swapped:
            numbers[index + 1] = value

        yield numbers
