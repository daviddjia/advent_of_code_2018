#!/usr/bin/env python
import bisect

f = open('day13_input.txt','r')
lines = f.readlines()
f.close()

carts = {}
full_map = [['' for i in range(len(lines))] for j in range(len(lines[0])-1)]

cart_symbols_for_map = {
    '^': '|',
    'v': '|',
    '<': '-',
    '>': '-',
}

for j, row in enumerate(lines):
    for i, col in enumerate(list(row[:-1])):
        symbol = col
        if symbol in cart_symbols_for_map:
            carts[(i, j)] = [symbol, 0]
            symbol = cart_symbols_for_map[symbol]
        full_map[i][j] = symbol

cart_symbols_for_delta = {
    '^': (0, -1),
    'v': (0, 1),
    '<': (-1, 0),
    '>': (1, 0),
}
def move_delta(symbol):
    if symbol in cart_symbols_for_delta:
        return cart_symbols_for_delta[symbol]

cart_symbols_for_curve_redirect = {
    ('^', '/'): '>',
    ('^', '\\'): '<',
    ('v', '/'): '<',
    ('v', '\\'): '>',
    ('<', '/'): 'v',
    ('<', '\\'): '^',
    ('>', '/'): '^',
    ('>', '\\'): 'v',
}
cart_symbols_for_intersection_redirect = {
    ('^', 0): '<',
    ('^', 1): '^',
    ('^', 2): '>',
    ('v', 0): '>',
    ('v', 1): 'v',
    ('v', 2): '<',
    ('<', 0): 'v',
    ('<', 1): '<',
    ('<', 2): '^',
    ('>', 0): '^',
    ('>', 1): '>',
    ('>', 2): 'v',
}
def redirect(symbol, track, turn_count):
    if track in ['-', '|']:
        return (symbol, turn_count)
    elif track in ['/', '\\']:
        return (cart_symbols_for_curve_redirect[(symbol, track)], turn_count)
    elif track == '+':
        return (
            cart_symbols_for_intersection_redirect[(symbol, turn_count)],
            (turn_count+1)%3,
        )
    else:
        print 'ERROR!'
        exit()

while(True):
    for i, old_coord in enumerate(sorted(carts.keys())):
        x = old_coord[0]
        y = old_coord[1]
        if old_coord not in carts:
            continue
        symbol = carts[old_coord][0]
        turn_count = carts[old_coord][1]

        delta_coord = move_delta(symbol)
        coord = (x+delta_coord[0], y+delta_coord[1])
        if coord in carts:
            print '%s,%s' % (x+delta_coord[0], y+delta_coord[1])
            exit()
        (redirected_symbol, updated_turn_count) = redirect(
            symbol,
            full_map[coord[0]][coord[1]],
            turn_count,
        )
        carts.pop(old_coord, None)
        carts[coord] = (redirected_symbol, updated_turn_count)
