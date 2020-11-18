import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

answer = 0

# game loop
while True:
    recipes = np.zeros(shape=(5, 18))
    spells = np.zeros(shape=(4, 6))
    spells_opponent = np.zeros(shape=(4, 6))
    ingredients = np.zeros(shape=(2, 5))

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

        a = 0
        b = 0
        c = 0
        if action_type == BREW:
            recipes[a, 0:6] = [action_id, delta_0, delta_1, delta_2, delta_3, price]
            a = a + 1
        if action_type == CAST:
            spells[b, :] = [action_id, delta_0, delta_1, delta_2, delta_3, castable]
            b = b + 1
        if action_type == OPPONENT_CAST:
            spells_opponent[c, :] = [action_id, delta_0, delta_1, delta_2, delta_3, castable]
            c = c + 1

    for i in range(2):
        # inv_0: tier-0 ingredients in inventory
        # score: amount of rupees
        inv_0, inv_1, inv_2, inv_3, score = [int(j) for j in input().split()]
        ingredients[i, :] = [score, inv_0, inv_1, inv_2, inv_3]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # in the first league: BREW <id> | WAIT; later: BREW <id> | CAST <id> [<times>] | LEARN <id> | REST | WAIT
    print("BREW", answer)