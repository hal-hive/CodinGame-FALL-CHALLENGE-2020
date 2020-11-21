# ### 5. розраховую питому вартість кроку з найефективнішим додатковим заклинанням
elif q == True:

# ### 5.1 повторні розрахунки, колонки 20-30 аналонічні як 6-16

# ### 5.12 вибираю максимальне значення питомої вартості, максимальне з колонки 30
max_averag = 0.1

# ### 6. порівнюю питому вартість
# ### 6.1 якщо ефективне заклинання ефективніше вибираю його на відповідь
if max_averag > max_average:
    answer_id = learns[ind_max_efficient, 0]
    answer = LEARN + str(int(answer_id))

# ### 6.2 якщо звичані заклинання ефективніші - йду звичайним шляхом
else:
    ind_max_step = recipes[recipes[:, 16] == max_average]
    ind_max_average = ind_max_step[0, 17]
    ind_max_average = int(ind_max_average)


    # n. процес виконання замовлення

    # n.2 перевірка стандартного заклинання на доступність (виконати заклинання чи відпочити)
    def check_n(n):
        if spells[n, 5] == 0:
            answer = REST
            return answer
        else:
            answer_id = int(spells[n, 0])
            answer = CAST + str(answer_id)
            return answer


    # n.1 виконання замовлення, ітерую по колонках 6-10 і вибираю стандартні заклинання
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
            elif recipes[ind_max_average, 7] > 0:
                answer = check_n(2)
                break
            elif recipes[ind_max_average, 6] > 0:
                answer = check_n(1)
                break
            else:
                answer = check_n(0)
                break






            # ### 5.3 перевіряю чи можу виконати кожеш рецепт колонка 24 = 1-можу або 0-неможу
            l: int = 0
            while l < 5:
                m = []
                for i in array[:, 0:4]:
                    for j in i:
                        if j < 0:
                            m.append(False)
                        else:
                            m.append(True)
                    a = all(m)
                    if a == False:
                        array[l, 4] = 0
                        l = l + 1
                        m.clear()
                    else:
                        array[l, 4] = 1
                        l = l + 1
                        m.clear()