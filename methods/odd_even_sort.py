import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random as r


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


def odd_even_sort_visualize(size, speed):
    # speed {15, 50, 80}
    numbers = [x + 1 for x in range(size)]
    print(numbers)
    r.shuffle(numbers)

    fig, ax = plt.subplots()
    bar_list = ax.bar(range(len(numbers)), numbers, width=0.8)
    iteration = [0]

    def update(array, bars, i):
        for bar, value in zip(bars, array):
            index = array.index(value)

            # set colors
            if index % 2 == 0:
                bar.set_color('green')
            else:
                bar.set_color('red')

            bar.set_height(value)
        i[0] += 1

    anim = animation.FuncAnimation(fig, func=update, fargs=(bar_list, iteration), frames=odd_even_sort(numbers),
                                   interval=speed, repeat=True, save_count=1000)
    plt.show()
