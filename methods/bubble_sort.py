import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random as r


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


def bubble_sort_visualize(size, speed):
    numbers = [x + 1 for x in range(size)]
    r.shuffle(numbers)

    fig, ax = plt.subplots()
    bar_list = ax.bar(range(len(numbers)), numbers, width=0.8)
    iteration = [0]

    def update(array, bars, i):
        for bar, value in zip(bars, array):
            index = array.index(value)
            # set colors
            try:
                if value > array[index + 1]:
                    bar.set_color('red')
                else:
                    bar.set_color('green')
            except IndexError:
                bar.set_color('green')

            # set value
            bar.set_height(value)

        i[0] += 1

    anim = animation.FuncAnimation(fig, func=update, fargs=(bar_list, iteration), frames=bubble_sort(numbers),
                                   interval=speed, repeat=True, save_count=1000)
    plt.show()


