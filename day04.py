#!/usr/bin/env python
import re

# f = open('day04_test_input.txt','r')
f = open('day04_input.txt','r')
lines = f.readlines()
f.close()
list.sort(lines)

guard_number = -1
guards = {}
sleep_time = -1
guards_sleepiest = {}
guards_sleep_duration = {}
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
            guards_sleep_duration[guard_number] = 0
    elif 'falls asleep' in action:
        sleep_time = minute
    elif 'wakes up' in action:
        guards_sleep_duration[guard_number] += minute - sleep_time
        for m in xrange(sleep_time, minute):
            if m not in guards[guard_number]:
                guards[guard_number][m] = set([date])
            else:
                guards[guard_number][m].add(date)
            if (
                guards_sleepiest[guard_number][0] != m and
                len(guards[guard_number][m]) > guards_sleepiest[guard_number][1]
            ):
                guards_sleepiest[guard_number] = (
                    m,
                    len(guards[guard_number][m]),
                )
    else:
        print 'Error!'
        exit()

max_sleep_duration = (-1, -1)
for guard in guards_sleep_duration:
    if guards_sleep_duration[guard] > max_sleep_duration[1]:
        max_sleep_duration = (guard, guards_sleep_duration)

sleepiest_guard = max_sleep_duration[0]
sleepiest_minute = guards_sleepiest[sleepiest_guard][0]
sleepiest_minute_repeats = guards_sleepiest[sleepiest_guard][1]
print "GUARD: %s | MINUTE: %s | # OF TIMES: %s" % (
    str(sleepiest_guard),
    str(sleepiest_minute),
    str(sleepiest_minute_repeats),
)
print sleepiest_guard * sleepiest_minute
import ipdb; ipdb.set_trace()
