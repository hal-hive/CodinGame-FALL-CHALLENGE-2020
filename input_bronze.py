import sys
import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

answer = 0

# game loop
while True:
    recipes = np.zeros(shape=(5, 31))
    spells = np.zeros(shape=(20, 6))
    spells_opponent = np.zeros(shape=(20, 6))
    ingredients = np.zeros(shape=(8, 5))
    learns = np.zeros(shape=(6, 14))

    a = 0
    b = 0
    c = 0
    d = 0
    action_count = int(input())  # the number of spells and recipes in play
    for i in range(action_count):
        # action_id: the unique ID of this spell or recipe
        # action_type: in the first league: BREW; later: CAST, OPPONENT_CAST, LEARN, BREW
        # delta_0: tier-0 ingredient change
        # delta_1: tier-1 ingredient change
        # delta_2: tier-2 ingredient change
        # delta_3: tier-3 ingredient change
        # price: the price in rupees if this is a potion
        # tome_index: in the first two leagues: always 0; later: the index in the tome if this is a tome spell, equal to the read-ahead tax; For brews, this is the value of the current urgency bonus
        # tax_count: in the first two leagues: always 0; later: the amount of taxed tier-0 ingredients you gain from learning this spell; For brews, this is how many times you can still gain an urgency bonus
        # castable: in the first league: always 0; later: 1 if this is a castable player spell
        # repeatable: for the first two leagues: always 0; later: 1 if this is a repeatable player spell
        action_id, action_type, delta_0, delta_1, delta_2, delta_3, price, tome_index, tax_count, castable, repeatable = input().split()
        action_id = int(action_id)
        delta_0 = int(delta_0)
        delta_1 = int(delta_1)
        delta_2 = int(delta_2)
        delta_3 = int(delta_3)
        price = int(price)
        tome_index = int(tome_index)
        tax_count = int(tax_count)
        castable = castable != "0"
        repeatable = repeatable != "0"
        if action_type == 'BREW':
            recipes[a, 0:6] = [action_id, delta_0, delta_1, delta_2, delta_3, price]
            recipes[a, 18:20] = [tome_index, tax_count]
            a = a + 1
        if action_type == 'CAST':
            spells[b, :] = [action_id, delta_0, delta_1, delta_2, delta_3, castable]
            b = b + 1
        if action_type == 'OPPONENT_CAST':
            spells_opponent[c, :] = [action_id, delta_0, delta_1, delta_2, delta_3, castable]
            c = c + 1
        if action_type == 'LEARN':
            learns[d, 0:8] = [action_id, delta_0, delta_1, delta_2, delta_3, tome_index, tax_count, repeatable]
            d = d + 1

    for i in range(2):
        # inv_0: tier-0 ingredients in inventory
        # score: amount of rupees
        inv_0, inv_1, inv_2, inv_3, score = [int(j) for j in input().split()]
        ingredients[i, :] = [score, inv_0, inv_1, inv_2, inv_3]

    BREW = 'BREW '
    REST = 'REST'
    CAST = 'CAST '
    LEARN = 'LEARN '

    coefficient = np.zeros(shape=(7, 4))
    coefficient[1, :] = [2, 3, 4, 5]
    coefficient[2, :] = [2, 5, 7, 9]
    coefficient[3, :] = [4, 8, 11, 14]
    coefficient[4, :] = [4, 10, 14, 18]
    coefficient[5, :] = [6, 13, 18, 23]
    coefficient[6, :] = [6, 15, 21, 27]
    recipes[:, 17] = [0, 1, 2, 3, 4]
    # print(np.array_str(spells))

    n = 0
    for i in recipes[:, 1:5]:
        recipes[n, 6:10] = ingredients[0, 1:5] + i
        n = n + 1

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

    x = np.nonzero(recipes[:, 10])
    y = np.size(x)
    if y == 0:
        ro = 0
        for i in recipes[:, 6:10]:
            co = 0
            for j in i:
                if j < 0:
                    if abs(j) == 1:
                        recipes[ro, co + 11] = coefficient[1, co]
                        co = co + 1
                    if abs(j) == 2:
                        recipes[ro, co + 11] = coefficient[2, co]
                        co = co + 1
                    if abs(j) == 3:
                        recipes[ro, co + 11] = coefficient[3, co]
                        co = co + 1
                    if abs(j) == 4:
                        recipes[ro, co + 11] = coefficient[4, co]
                        co = co + 1
                    if abs(j) == 5:
                        recipes[ro, co + 11] = coefficient[5, co]
                        co = co + 1
                    if abs(j) == 6:
                        recipes[ro, co + 11] = coefficient[6, co]
                        co = co + 1
                if j >= 0:
                    j = j - (j * 2)
                    recipes[ro, co + 11] = j
                    co = co + 1
            ro = ro + 1

        recipes[:, 15] = np.sum(recipes[:, 11:15], axis=1)
        recipes[:, 16] = recipes[:, 5] / recipes[:, 15]
        max_average = np.amax(recipes[:, 16])
        ind_max_step = recipes[recipes[:, 16] == max_average]
        id_brew = ind_max_step[0, 0]
        ind_max_average = ind_max_step[0, 17]
        ind_max_average = int(ind_max_average)


        def check_n(n):
            if spells[n, 5] == 0:
                answer = REST
                return answer
            else:
                answer_id = int(spells[n, 0])
                answer = CAST + str(answer_id)
                return answer


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
                elif recipes[ind_max_average, 6] > 0:
                    answer = check_n(1)
                    break
                else:
                    answer = check_n(0)
                    break
            if i < 0 and k == 3:
                if recipes[ind_max_average, 8] > 0:
                    answer = check_n(3)
                    break
                elif recipes[ind_max_average, 7] > 0:
                    answer = check_n(2)
                    break
                elif recipes[ind_max_average, 6] > 0:
                    answer = check_n(1)
                    break
                else:
                    answer = check_n(0)
                    break
    else:
        ind_price = np.take(recipes[:, 5], x)
        pric = ind_price.max()
        ans = recipes[recipes[:, 5] == pric]
        answer_id = ans[0, 0]
        answer = BREW + str(int(answer_id))
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    # in the first league: BREW <id> | WAIT; later: BREW <id> | CAST <id> [<times>] | LEARN <id> | REST | WAIT
    print(answer)