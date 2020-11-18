# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np

answer = 0



def print_h():
    answer_id = 0
    BREW = 'BREW '
    REST = 'REST'
    CAST = 'CAST '

    recipes = np.zeros(shape=(5, 18))
    spells = np.zeros(shape=(4, 6))
    spells_other = np.zeros(shape=(4, 6))
    ingredients = np.zeros(shape=(2, 5))

    recipes[0, 0:6] = [70, -2, -2, 0, -2, 15]
    recipes[1, 0:6] = [71, -2, 0, -3, 0, 11]
    recipes[2, 0:6] = [72, 0, -2, -3, 0, 13]
    recipes[3, 0:6] = [73, -2, 0, 0, -2, 10]
    recipes[4, 0:6] = [74, -2, -1, 0, -1, 9]

    spells[0, :] = [80, 2, 0, 0, 0, 1]
    spells[1, :] = [81, -1, 1, 0, 0, 1]
    spells[2, :] = [82, 0, -1, 1, 0, 1]
    spells[3, :] = [83, 0, 0, -1, 1, 1]

    ingredients[0, :] = [0, 3, 1, 0, 0]
    ingredients[1, :] = [0, 3, 0, 0, 0]

    coefficient = np.zeros(shape=(7, 4))
    coefficient[1, :] = [2, 3, 4, 5]
    coefficient[2, :] = [2, 5, 7, 9]
    coefficient[3, :] = [4, 8, 11, 14]
    coefficient[4, :] = [4, 10, 14, 18]
    coefficient[5, :] = [6, 13, 18, 23]
    coefficient[6, :] = [6, 15, 21, 27]
    recipes[:, 17] = [0, 1, 2, 3, 4]

    def check_n(n):
        if spells[n, 5] == 0:
            answer = REST
            return answer
        else:
            answer_id = int(spells[n, 0])
            answer = CAST + str(answer_id)
            return answer

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
        answer_id = np.take(recipes[:, 0], x)
        answer = BREW + str(int(answer_id))
    elif np.count_nonzero(x) > 1:
        ind_price = np.take(recipes[:, 5], x)
        pric = ind_price.max()
        ans = recipes[recipes[:, 5] == pric]
        answer_id = ans[0, 0]
        answer = BREW + str(int(answer_id))
    else:
        ro = 0
        for i in recipes[:, 6:10]:
            co = 0
            for j in i:
                if j < 0:
                    if abs(j) == 1:
                        recipes[ro, co+11] = coefficient[1, co]
                        co = co + 1
                    if abs(j) == 2:
                        recipes[ro, co+11] = coefficient[2, co]
                        co = co + 1
                    if abs(j) == 3:
                        recipes[ro, co+11] = coefficient[3, co]
                        co = co + 1
                    if abs(j) == 4:
                        recipes[ro, co+11] = coefficient[4, co]
                        co = co + 1
                    if abs(j) == 5:
                        recipes[ro, co+11] = coefficient[5, co]
                        co = co + 1
                    if abs(j) == 6:
                        recipes[ro, co+11] = coefficient[6, co]
                        co = co + 1
                if j >= 0:
                    j = j - (j * 2)
                    recipes[ro, co+11] = j
                    co = co + 1
            ro = ro + 1

        recipes[:, 15] = np.sum(recipes[:, 11:15], axis=1)
        recipes[:, 16] = recipes[:, 5] / recipes[:, 15]
        max_average = np.amax(recipes[:, 16])
        ind_max_step = recipes[recipes[:, 16] == max_average]
        id_brew = ind_max_step[0, 0]
        ind_max_average = ind_max_step[0, 17]
        ind_max_average = int(ind_max_average)

        k = 0
        for i in recipes[ind_max_average, 6:10]:
            if i >= 0:
                k = k + 1
            if i < 0 and k == 0:
                answer = check_n(0)
                break
            if i < 0 and k == 1:
                if recipes[ind_max_average, 6] > 0:
                    answer = check_n(1)
                    break
                else:
                    answer = check_n(0)
                    break
            if i < 0 and k == 2:
                if recipes[ind_max_average, 7] > 0:
                    answer = check_n(2)
                    break
                if recipes[ind_max_average, 6] > 0:
                    answer = check_n(1)
                    break
                else:
                    answer = check_n(0)
                    break
            if i < 0 and k == 3:
                if recipes[ind_max_average, 8] > 0:
                    answer = check_n(3)
                    break
                if recipes[ind_max_average, 7] > 0:
                    answer = check_n(2)
                    break
                if recipes[ind_max_average, 6] > 0:
                    answer = check_n(1)
                    break
                else:
                    answer = check_n(0)
                    break

    print(answer)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_h()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
