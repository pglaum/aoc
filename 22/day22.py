#!/usr/bin/env python3

import os
import re

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    lines = f.readlines()

boss_hp = int(re.findall(r'\d+', lines[0])[0])
boss_dmg = int(re.findall(r'\d+', lines[1])[0])

def is_contained(effects, e):
    for ef in effects:
        if ef[0] == e:
            return True

    return False

all_lowest = 100000
def simulate(player, mana, boss, effects=[], cost=0, turn=True, moves=[], hard=False):
    global all_lowest

    lowest = 100000
    if cost > all_lowest:
        return lowest

    if boss <= 0:
        all_lowest = cost
        #print('player won', cost)
        #[print(m) for m in moves]
        #print()
        return cost

    if hard and turn:
        player -= 1

    if player <= 0:
        #print('player dead', cost)
        #[print(m) for m in moves]
        #print()
        return lowest

    armor = 0
    new_effects = []
    for i in range(len(effects)):
        if effects[i][0] == 'shield':
            armor = 7
        elif effects[i][0] == 'poison':
            boss -= 3
        elif effects[i][0] == 'recharge':
            mana += 101
        if effects[i][1] > 1:
            new_effects.append([effects[i][0], effects[i][1] - 1])
    effects = new_effects.copy()

    if boss <= 0:
        all_lowest = cost
        #print('player won', cost)
        #[print(m) for m in moves]
        #print()
        return cost

    if turn:
        # missile
        if mana >= 53:
            lowest = min(simulate(player, mana-53, boss - 4, effects, cost + 53, False,
                                  moves + [f'missile'], hard), lowest)

        # drain
        if mana >= 73:
            lowest = min(simulate(player + 2, mana-73, boss - 2, effects, cost + 73, False,
                                  moves + ['drain'], hard), lowest)

        # shield
        if mana >= 113 and not is_contained(effects, 'shield'):
            lowest = min(simulate(player, mana-113, boss, effects + [['shield', 6]], cost + 113, False,
                                  moves + ['shield'], hard), lowest)

        # poison
        if mana >= 173 and not is_contained(effects, 'poison'):
            lowest = min(simulate(player, mana-173, boss, effects + [['poison', 6]], cost + 173, False,
                                  moves + ['posion'], hard), lowest)

        # recharge
        if mana >= 229 and not is_contained(effects, 'recharge'):
            lowest = min(simulate(player, mana-229, boss, effects + [['recharge', 5]], cost + 229, False,
                                  moves + ['recharge'], hard), lowest)
    else:
        dmg = max(boss_dmg - armor, 1)
        lowest = min(simulate(player-dmg, mana, boss, effects, cost, True,
                              moves + [f'boss attacks ({boss} vs {player} - {dmg}) | ({effects})'], hard), lowest)

    return lowest

print('Part 1:', simulate(50, 500, boss_hp, [], 0, True))

all_lowest = 100000
print('Part 2:', simulate(50, 500, boss_hp, [], 0, True, [], True))
