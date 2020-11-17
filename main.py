# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np


answer = 0

def print_h():
    recipes = np.zeros(shape=(5, 11))
    spells = np.zeros(shape=(4, 6))
    ingredients = np.zeros(shape=(2, 5))

    recipes[0, 0:6] = [70, -2, -2, 0, -2, 15]
    recipes[1, 0:6] = [71, -2, 0, -3, 0, 11]
    recipes[2, 0:6] = [72, 0, -2, -3, 0, 13]
    recipes[3, 0:6] = [73, -2, 0, 0, 0, 10]
    recipes[4, 0:6] = [74, -2, 1, 0, 1, 9]

    spells[0, :] = [80, 2, 0, 0, 0, 1]
    spells[1, :] = [81, -1, 1, 0, 0, 1]
    spells[2, :] = [82, 0, -1, 1, 0, 1]
    spells[3, :] = [83, 0, 0, -1, 1, 1]

    ingredients[0, :] = [0, 3, 0, 0, 0]
    ingredients[1, :] = [0, 3, 0, 0, 0]

    n = 0
    for i in recipes[:, 1:5]:
        recipes[n, 6:10] = ingredients[0, 1:5] + i
        n = n + 1

    l: int = 0
    while l < 5:
        m = []
        for i in recipes[:, 6:10]:
            for j in i:
                if j < 0:
                    m.append(False)
                else:
                    m.append(True)
            a = all(m)
            if a == False:
                recipes[l, 10] = 0
                l = l + 1
                m.clear()
            else:
                recipes[l, 10] = 1
                l = l + 1
                m.clear()

    x = np.nonzero(recipes[:, 10])
    if np.count_nonzero(x) == 1:
        answer = np.take(recipes[:, 0], x)
    elif np.count_nonzero(x) > 1:
        ind_price = np.take(recipes[:, 5], x)
        pric = ind_price.max()
        ans = recipes[recipes[:, 5] == pric]
        answer = ans[0,0]
    else:




    print(answer)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_h()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
