#!/usr/bin/env python
from collections import deque

class Position(object):
    def __init__(self, coord):
        self.coord = coord
        self.north = None
        self.south = None
        self.east = None
        self.west = None
    def __eq__(self, other):
        return self.coord==other.coord
    def __cmp__(self, other):
        return cmp(self.coord, other.coord)
    def adjacents(self):
        positions = []
        if self.north:
            positions.append((self.north, 'north'))
        if self.south:
            positions.append((self.south, 'south'))
        if self.east:
            positions.append((self.east, 'east'))
        if self.west:
            positions.append((self.west, 'west'))
        return positions

class Unit(object):
    def __init__(self, position):
        self.position = position
        self.attack = 3
        self.hp = 200
        self.is_alive = True
    def get_hit(self, attack):
        self.hp -= attack
        if self.hp <= 0:
            self.is_alive = False
        return self.is_alive
    def __eq__(self, other):
        return self.position==other.position
    def __cmp__(self, other):
        return cmp(self.position, other.position)

class Elf(Unit):
    pass

class Goblin(Unit):
    pass

class Cave(object):
    def __init__(self, raw_cave):
        self.rounds = 0
        self.positions = {}
        self.units = {}

        self.full_map = [
            ['' for i in xrange(len(raw_cave))]
            for j in xrange(len(raw_cave[0]))
        ]

        # Building map and creating all Position and Unit objects
        for j, row in enumerate(raw_cave):
            for i, col in enumerate(list(row)):
                symbol = col
                self.full_map[i][j] = symbol
                if symbol != '#':
                    pos = Position(coord=(i, j))
                    self.positions[(i, j)] = pos
                    if symbol == 'E':
                        self.units[pos] = Elf(position=pos)
                    if symbol == 'G':
                        self.units[pos] = Goblin(position=pos)

        # Connecting Position objects to form graph
        for j in xrange(len(self.full_map)):
            for i in xrange(len(self.full_map[0])):
                symbol = self.full_map[i][j]
                if symbol == '#':
                    continue
                pos = self.positions[(i, j)]
                if j > 0 and self.full_map[i][j-1] != '#':
                    pos.north = self.positions[(i, j-1)]
                if j < len(self.full_map)-1 and self.full_map[i][j+1] != '#':
                    pos.south = self.positions[(i, j+1)]
                if i > 0 and self.full_map[i-1][j] != '#':
                    pos.east = self.positions[(i-1, j)]
                if i < len(self.full_map[0])-1 and self.full_map[i+1][j] != '#':
                    pos.west = self.positions[(i+1, j)]

    def _calculate_move(self, unit, pos):
        # Identify targets
        enemies = [e for e in self.units.values() if type(e) != type(unit)]
        targets = set()
        for enemy in enemies:
            targets.update([
                adj_pos
                for (adj_pos, direction) in enemy.position.adjacents()
            ])

        # Find shortest path to all targets (BFS)
        target_distances = []
        queue = deque([pos])
        visited = set()
        paths = {pos: (None, None)}
        while len(queue) > 0:
            cur_pos = queue.popleft()
            if cur_pos in targets:
                temp_pos = cur_pos
                direction_list = []
                while paths[temp_pos][0] is not None:
                    (temp_pos, temp_dir) = paths[temp_pos]
                    direction_list.append(temp_dir)
                target_distances.append((len(direction_list), temp_dir))
            for (adj_pos, direction) in cur_pos.adjacents():
                if adj_pos not in visited and adj_pos not in queue:
                    queue.append(adj_pos)
                    paths[adj_pos] = (cur_pos, direction)
            visited.add(cur_pos)
        return sorted(target_distances)[0][0]

    def _combat_round(self):
        unit_positions = sorted(self.units.keys())
        for pos in unit_positions:
            unit = self.units[pos]
            direction = self._calculate_move(unit, pos)
            unit.move(direction)

    def _combat_cleanup(self):
        self.units.sort()
        self.rounds += 1

    def _win_condition(self):
        elf_count = 0
        goblin_count = 0
        for unit in self.units.values():
            if isinstance(unit, Elf):
                elf_count += 1
            else:
                goblin_count += 1
        return elf_count == 0 or goblin_count == 0

    def combat(self):
        while not self._win_condition():
            self._combat_round()
            self._combat_cleanup()
        return (self.rounds, sum([unit.hp for unit in self.units.values()]))

def parse_input():
    f = open('day15_input.txt','r')
    lines = f.readlines()
    f.close()
    return [l.strip() for l in lines]

def main():
    lines = parse_input()
    cave = Cave(raw_cave=lines)
    (rounds, remaining_hp) = cave.combat()
    print 'Rounds: %s | Remaining HP: %s | Product: %s' % (
        rounds,
        remaining_hp,
        rounds * remaining_hp,
    )

if __name__ == "__main__":
    main()
