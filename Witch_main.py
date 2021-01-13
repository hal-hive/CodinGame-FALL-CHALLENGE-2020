# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import time
import sys


def print_h():

    # засікти час початку виконання коду
    tic = time.perf_counter()

    answer = 0
    BREW = 'BREW '
    REST = 'REST'
    CAST = 'CAST '
    LEARN = 'LEARN '

    # пусті масиви NumPy
    recipes = np.zeros(shape=(5, 31))
    spells = np.zeros(shape=(20, 6))
    spells_opponent = np.zeros(shape=(20, 6))
    ingredients = np.zeros(shape=(8, 5))
    learns = np.zeros(shape=(6, 14))
    coefficient = np.zeros(shape=(7, 4))

    # запис вхідних даних в масиви
    # рецепти
    recipes[0, 0:6] = [64, 0, 0, -2, -3, 19]
    recipes[1, 0:6] = [59, -2, 0, 0, -3, 14]
    recipes[2, 0:6] = [67, 0, -2, -1, -1, 12]
    recipes[3, 0:6] = [61, 0, 0, 0, -4, 16]
    recipes[4, 0:6] = [75, -1, -3, -1, -1, 16]
    recipes[:, 17] = [0, 1, 2, 3, 4]

    # доступні заклинання: стандартні + вивчені
    spells[0, :] = [78, 2, 0, 0, 0, 1]
    spells[1, :] = [79, -1, 1, 0, 0, 1]
    spells[2, :] = [80, 0, -1, 1, 0, 1]
    spells[3, :] = [81, 0, 0, -1, 1, 1]
    spells[4, :] = [94, 3, -2, 1, 0, 1]
    spells[5, :] = [97, 3, 0, 1, -1, 1]

    # наявні інгредієнти
    ingredients[0, :] = [0, 4, 3, 1, 1]
    ingredients[1, :] = [0, 3, 0, 0, 0]

    # коефіцієнти для оцінки заклинань поінгредієнтно
    coefficient[1, :] = [2, 3, 4, 5]
    coefficient[2, :] = [2, 5, 7, 9]
    coefficient[3, :] = [4, 8, 11, 14]
    coefficient[4, :] = [4, 10, 14, 18]
    coefficient[5, :] = [6, 13, 18, 23]
    coefficient[6, :] = [6, 15, 21, 27]

    # додаткові заклинання доступні для вивчення
    learns[0, 0:6] = [30, 0, 2, -2, 1, 0]
    learns[1, 0:6] = [31, -1, -1, 0, 1, 1]
    learns[2, 0:6] = [32, 3, -1, 0, 0, 2]
    learns[3, 0:6] = [33, 2, 2, 0, -1, 3]
    learns[4, 0:6] = [34, 0, 0, -2, 2, 4]
    learns[5, 0:6] = [35, 1, 2, -1, 0, 5]

    # чи можу в даний момент виконати рецепт
    # від своїх інгредієнтів віднімаю рецепти
    n = 0
    for i in recipes[:, 1:5]:
        recipes[n, 6:10] = ingredients[0, 1:5] + i
        n = n + 1

    # перевіряю чи можу виконати кожеш рецепт, колонка 10 = 1-можу або 0-неможу
    l = 0
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

    # перевіряю колонку 10 на 1/0, індекси елементів, що не 0
    x = np.nonzero(recipes[:, 10])

    # у = кількість елементів в колонці 10 зі значенням 1
    y = np.size(x)

    # розгалуження, шлях 2 - зразу можу зробити замовлення, шлях 3 - неможу зробити замовлення і рахую дальше
    # шлях 3 -неможу зробити замовлення, створюю словник для можливих варіантів
    dict_id = {}

    # шлях 3 / рахую дальше
    if y == 0:

        # виконання додаткових заклинань, якщо вони є
        # перевірка заклинання на можливість виконати (чи є достатньо інгредієнтів)
        def chek_can_do(index, ingredients):
            ingr = ingredients[0, 1:5] + index
            q = 0
            for j in ingr:
                if j < 0:
                    return False
                else:
                    q = q + 1
            return True

        # перевірка заклинання на можливість виконати (є достатньо місця для інгредієнтів True)
        def check_owerflow(index, ingredients):
            ingr_main = np.sum(ingredients[0, 1:5])
            ingr_two = np.sum(index)
            result = ingr_main + ingr_two
            if result <= 10:
                return True
            else:
                return False

        # функція повертає максимальну питому вартість для конкретного заклинання
        def best_unit_price(index, count, recipes, ingredients, coefficient):

            # створюю пустий масив для розрунків
            array = np.zeros(shape=(5, 11))

            # віднімаю від своїх нових інгредієнтів (row 2) замовлення
            n = 0
            ingredients[2, 1:5] = ingredients[0, 1:5] + index
            for i in recipes[:, 1:5]:
                array[n, 0:4] = ingredients[2, 1:5] + i
                n = n + 1

            # вираховую кількість кроків для виконання замовлень із заклинаннями, колонки 5-8
            ro = 0
            for i in array[:, 0:4]:
                co = 0
                for j in i:
                    if j == 0:
                        array[ro, co + 5] = j
                        co = co + 1
                    elif j < 0:
                        if abs(j) == 1:
                            array[ro, co + 5] = coefficient[1, co]
                            co = co + 1
                        if abs(j) == 2:
                            array[ro, co + 5] = coefficient[2, co]
                            co = co + 1
                        if abs(j) == 3:
                            array[ro, co + 5] = coefficient[3, co]
                            co = co + 1
                        if abs(j) == 4:
                            array[ro, co + 5] = coefficient[4, co]
                            co = co + 1
                        if abs(j) == 5:
                            array[ro, co + 5] = coefficient[5, co]
                            co = co + 1
                        if abs(j) == 6:
                            array[ro, co + 5] = coefficient[6, co]
                            co = co + 1
                    elif j > 0:
                        j = j - (j * 2)
                        array[ro, co + 5] = j
                        co = co + 1
                ro = ro + 1

            # рахую суму кроків для кожного замовлення по стандартних закриланнях, колонка 9
            array[:, 9] = count + np.sum(array[:, 5:9], axis=1)

            # виправити відємні або нульові значення
            r = 0
            for i in array[:, 9]:
                if i > 0:
                    array[r, 9] = i
                    r = r + 1
                else:
                    array[r, 9] = 1
                    r = r + 1

            # рахую питому вартість кроку, колонка 10
            array[:, 10] = recipes[:, 5] / array[:, 9]

            # вибираю максимальне значення питомої вартості, максимальне з колонки 10
            max_averag = np.amax(array[:, 10])

            return max_averag

        # вираховую кількість кроків для виконання замовлень стандартними заклинаннями, колонки 11-14
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

        # рахую суму кроків для кожного замовлення по стандартних закриланнях, колонка 15
        recipes[:, 15] = np.sum(recipes[:, 11:15], axis=1)

        # виправити від'ємні значення
        r = 0
        for i in recipes[:, 15]:
            if i > 0:
                recipes[r, 15] = i
                r = r + 1
            else:
                recipes[r, 15] = 1
                r = r + 1

        # рахую питому вартість кроку, колонка 16
        recipes[:, 16] = recipes[:, 5] / recipes[:, 15]

        # вибираю максимальне значення питомої вартості, максимальне з колонки 16
        max_average = np.amax(recipes[:, 16])
        ans = recipes[recipes[:, 16] == max_average]
        brew_id = ans[0, 0]
        dict_id['brew'] = max_average

        # розрахувати ефективність додаткових заклинань, кількість кроків для кожного елемента, колонки 8-11
        learns[:, 12] = [0, -2, -2, -4, -4, -6]
        row = 0
        for i in learns[:, 1:5]:
            col = 0
            for j in i:
                if j == 0:
                    learns[row, col + 8] = 0
                    col = col + 1
                elif j < 0:
                    if abs(j) == 1:
                        learns[row, col + 8] = -1 * coefficient[1, col]
                        col = col + 1
                    if abs(j) == 2:
                        learns[row, col + 8] = -1 * coefficient[2, col]
                        col = col + 1
                    if abs(j) == 3:
                        learns[row, col + 8] = -1 * coefficient[3, col]
                        col = col + 1
                    if abs(j) == 4:
                        learns[row, col + 8] = -1 * coefficient[4, col]
                        col = col + 1
                    if abs(j) == 5:
                        learns[row, col + 8] = -1 * coefficient[5, col]
                        col = col + 1
                    if abs(j) == 6:
                        learns[row, col + 8] = -1 * coefficient[6, col]
                        col = col + 1
                else:
                    if abs(j) == 1:
                        learns[row, col + 8] = coefficient[1, col]
                        col = col + 1
                    if abs(j) == 2:
                        learns[row, col + 8] = coefficient[2, col]
                        col = col + 1
                    if abs(j) == 3:
                        learns[row, col + 8] = coefficient[3, col]
                        col = col + 1
                    if abs(j) == 4:
                        learns[row, col + 8] = coefficient[4, col]
                        col = col + 1
                    if abs(j) == 5:
                        learns[row, col + 8] = coefficient[5, col]
                        col = col + 1
                    if abs(j) == 6:
                        learns[row, col + 8] = coefficient[6, col]
                        col = col + 1
            row = row + 1

        # рахую суму кроків = ефективність, колонка 13
        learns[:, 13] = np.sum(learns[:, 8:13], axis=1)

        # записую в словник результати всіх ефективних заклинань
        r = 0
        for i in learns[:, 13]:
            if i > 0:
                q = chek_can_do(learns[r, 1:5], ingredients)
                z = check_owerflow(learns[r, 1:5], ingredients)
                if q == True and z == True and ingredients[0, 1] >= learns[r, 5]:
                    dict_id[LEARN + str(int(learns[r, 0]))] = best_unit_price(learns[r, 1:5], 1, recipes, ingredients, coefficient)
            r = r + 1

        # перевірка чи заклинання стандартне (False), чи додаткове (True)
        def main_spell(i):
            a = [2, 0, 0, 0]
            b = [-1, 1, 0, 0]
            c = [0, -1, 1, 0]
            d = [0, 0, -1, 1]
            al = np.array_equal(a, i)
            bl = np.array_equal(b, i)
            cl = np.array_equal(c, i)
            dl = np.array_equal(d, i)
            if al == True:
                return False
            elif bl == True:
                return False
            elif cl == True:
                return False
            elif dl == True:
                return False
            else:
                return True

        # записую в словник результати всіх своїх додаткових заклинань
        r = 0
        for i in spells[:, 1:5]:
            idi = spells[r, 0]
            m = main_spell(i)
            if idi != 0 and m == True:
                q = chek_can_do(i, ingredients)
                z = check_owerflow(i, ingredients)
                if q == True and z == True and spells[r, 5] == 1:
                    dict_id[CAST + str(int(spells[r, 0]))] = best_unit_price(i, 0, recipes, ingredients, coefficient)
            r = r + 1

        # вибрати максимальне значення зі словника
        v = list(dict_id.values())
        k = list(dict_id.keys())
        result = k[v.index(max(v))]
        if result != 'brew':
            answer = result
        else:

        # розгалуження коли не можу зробити додаткове ефективне заклинання, роблю за старою схемою
            # індекс максимального питомого (рядок замовлення яке я буду виконувати)
            ind_max_step = recipes[recipes[:, 16] == max_average]
            ind_max_average = ind_max_step[0, 17]
            ind_max_average = int(ind_max_average)

            # процес виконання замовлення
            # перевірка стандартного заклинання на доступність (виконати заклинання чи відпочити)
            def check_n(n):
                if spells[n, 5] == 0:
                    answer = REST
                    return answer
                else:
                    answer_id = int(spells[n, 0])
                    answer = CAST + str(answer_id)
                    return answer

            # виконання замовлення, ітерую по колонках 6-10 і вибираю стандартні заклинання
            k = 0
            for i in recipes[ind_max_average, 6:10]:
                if i >= 0:
                    k = k + 1
                elif i < 0 and k == 0:
                    owerflow = check_owerflow(spells[0, 1:5], ingredients)
                    if owerflow == True:
                        answer = check_n(0)
                        break
                    else:
                        k = k + 1
                elif i < 0 and k == 1:
                    if recipes[ind_max_average, 6] > 0:
                        owerflow = check_owerflow(spells[1, 1:5], ingredients)
                        if owerflow == True:
                            answer = check_n(1)
                            break
                        else:
                            k = k + 1
                    else:
                        owerflow = check_owerflow(spells[0, 1:5], ingredients)
                        if owerflow == True:
                            answer = check_n(0)
                            break
                        else:
                            k = k + 1
                elif i < 0 and k == 2:
                    if recipes[ind_max_average, 7] > 0:
                        owerflow = check_owerflow(spells[2, 1:5], ingredients)
                        if owerflow == True:
                            answer = check_n(2)
                            break
                        else:
                            k = k + 1
                    if recipes[ind_max_average, 6] > 0:
                        owerflow = check_owerflow(spells[1, 1:5], ingredients)
                        if owerflow == True:
                            answer = check_n(1)
                            break
                        else:
                            k = k + 1
                    else:
                        owerflow = check_owerflow(spells[0, 1:5], ingredients)
                        if owerflow == True:
                            answer = check_n(0)
                            break
                        else:
                            k = k + 1
                elif i < 0 and k == 3:
                    if recipes[ind_max_average, 8] > 0:
                        owerflow = check_owerflow(spells[3, 1:5], ingredients)
                        if owerflow == True:
                            answer = check_n(3)
                            break
                        else:
                            k = k + 1
                    elif recipes[ind_max_average, 7] > 0:
                        owerflow = check_owerflow(spells[2, 1:5], ingredients)
                        if owerflow == True:
                            answer = check_n(2)
                            break
                        else:
                            k = k + 1
                    elif recipes[ind_max_average, 6] > 0:
                        owerflow = check_owerflow(spells[1, 1:5], ingredients)
                        if owerflow == True:
                            answer = check_n(1)
                            break
                        else:
                            k = k + 1
                    else:
                        owerflow = check_owerflow(spells[0, 1:5], ingredients)
                        if owerflow == True:
                            answer = check_n(0)
                            break
                        else:
                            k = k + 1

            # неможу виконати жодне з доступних заклинань через переповнення інгредієнтів
            if answer == 0:
                answer = REST

    # шлях 2 -зразу можу зробити замовлення, вибираю id
    else:
        if y == 1:
            answer_id = recipes[x, 0]
            answer = BREW + str(int(answer_id))
        else:
            ind_price = np.take(recipes[:, 5], x)
            pric = ind_price.max()
            ans = recipes[recipes[:, 5] == pric]
            l = 0
            for i in ans[:]:
                m = i[10]
                if m == 1:
                    answer_id = ans[l, 0]
                    answer = BREW + str(int(answer_id))
                else:
                    l = l + 1

    # роблю крок у грі
    print(answer)

    # вираховую час закінченя виконання коду, та виводжу в debag різницю
    toc = time.perf_counter()
    print(f"Debag {toc - tic:0.4f} seconds", file=sys.stderr, flush=True)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_h()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/