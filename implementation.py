import copy


def return_orders_list(combos_PBC, counter):
    P_combo_map, B_combo_map = make_combo_maps(combos_PBC)
    PC_combo_table = get_table_from_combos(P_combo_map, B_combo_map)
    return PC_combo_table


def make_combo_maps(combos_PBC):
    P_value_set = set()
    B_value_set = set()
    for i in range(0, len(combos_PBC)):
        P_value_set.add(combos_PBC[i][0])
        B_value_set.add(combos_PBC[i][1])
    P_combo_map = {}
    B_combo_map = {}
    for i in P_value_set:
        P_combo_map[i] = []
    for i in B_value_set:
        B_combo_map[i] = []

    for i in range(0, len(combos_PBC)):
        P_combo_map[combos_PBC[i][0]].append([combos_PBC[i][1], combos_PBC[i][2], [i, 1]])
        B_combo_map[combos_PBC[i][1]].append([combos_PBC[i][0], combos_PBC[i][2], [i, 1]])

    for i in P_combo_map:
        for j in P_combo_map:
            if j != 0 and i != j and i > j and i % j == 0:
                mult = int(i / j)
                for value in P_combo_map[j]:
                    P_combo_map[i].append([mult * value[0], mult * value[1], [value[2][0], mult]])
    for i in B_combo_map:
        for j in B_combo_map:
            if j != 0 and i != j and i > j and i % j == 0:
                mult = int(i / j)
                for value in B_combo_map[j]:
                    B_combo_map[i].append([mult * value[0], mult * value[1], [value[2][0], mult]])

    return P_combo_map, B_combo_map


def get_table_from_combos(P_combo_map, B_combo_map):
    p_max = max(P_combo_map)
    b_max = max(B_combo_map)
    table_max = int(p_max*b_max)
    PB_table = [[[9999, (0, 0)]] * (table_max+1) for _ in range(table_max+1)]

    for p, bc_tuple in P_combo_map.items():
        for bp in bc_tuple:
            number_of_beers = bp[0]
            cost = bp[1]
            if (PB_table[p][number_of_beers][0]) > cost:
                (PB_table[p][number_of_beers]) = [cost, bp[2]]

    for b, pc_choice in B_combo_map.items():
        for pc in pc_choice:
            number_of_wings = pc[0]
            cost = pc[1]
            if PB_table[number_of_wings][b][0] > cost:
                PB_table[number_of_wings][b] = [cost, pc[2]]
    prices = []
    for i in range(0, table_max):
        for j in range(0, table_max):
            if PB_table[i][j][0] <9999:
                prices.append([[i, j], PB_table[i][j][0], PB_table[i][j][1]])

    return PB_table
