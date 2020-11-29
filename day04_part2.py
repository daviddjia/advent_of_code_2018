#!/usr/bin/env python
import re

f = open('day04_test_input.txt','r')
# f = open('day04_input.txt','r')
lines = f.readlines()
f.close()
list.sort(lines)

guard_number = -1
guards = {}
sleep_time = -1
guards_sleepiest = {}
for l in lines:
    regex = '\[\d\d\d\d-(\d\d-\d\d) \d\d:(\d\d)\] (.*)'
    groups = re.search(regex, l)
    date = groups.group(1)
    minute = int(groups.group(2))
    action = groups.group(3)
    if '#' in action:
        regex = '#(\d*)'
        guard_number = int(re.search(regex, action).group(1))
        if guard_number not in guards:
            guards[guard_number] = {}
            guards_sleepiest[guard_number] = (-1, -1)
    elif 'falls asleep' in action:
        sleep_time = minute
    elif 'wakes up' in action:
        import ipdb; ipdb.set_trace()
        for m in xrange(sleep_time, minute):
            if minute not in guards[guard_number]:
                guards[guard_number][minute] = set([date])
            else:
                guards[guard_number][minute].add(date)
            if (
                guards_sleepiest[guard_number][0] != minute and
                len(guards[guard_number][minute]) > guards_sleepiest[guard_number][1]
            ):
                guards_sleepiest[guard_number] = (
                    minute,
                    len(guards[guard_number][minute]),
                )
    else:
        print 'Error!'
        exit()

print guards_sleepiest
max_sleepiest = (-1, -1, -1)
for guard in guards_sleepiest:
    if guards_sleepiest[guard][1] > max_sleepiest[1]:
        max_sleepiest = (
            guard,
            guards_sleepiest[guard][0],
            guards_sleepiest[guard][1]
        )
print "GUARD: %s | MINUTE: %s | # OF TIMES: %s" % (
    str(max_sleepiest[0]),
    str(max_sleepiest[1]),
    str(max_sleepiest[2]),
)
