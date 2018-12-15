#!/usr/bin/env python
import bisect

f = open('day13_input.txt','r')
lines = f.readlines()
f.close()

carts = []
carts_set = set()
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
            cart = [i, j, symbol, 0]
            bisect.insort(carts, cart)
            carts_set.add((i, j))
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
    for i, cart_meta in enumerate(carts):
        x = cart_meta[0]
        y = cart_meta[1]
        symbol = cart_meta[2]
        turn_count = cart_meta[3]

        delta_coord = move_delta(symbol)
        coord = (x+delta_coord[0], y+delta_coord[1])
        if coord in carts_set:
            print '%s,%s' % (x+delta_coord[0], y+delta_coord[1])
            exit()
        (redirected_symbol, updated_turn_count) = redirect(
            symbol,
            full_map[coord[0]][coord[1]],
            turn_count,
        )
        carts[i][0] = coord[0]
        carts[i][1] = coord[1]
        carts[i][2] = redirected_symbol
        carts[i][3] = updated_turn_count
        carts_set.remove((x, y))
        carts_set.add(coord)
    list.sort(carts)
