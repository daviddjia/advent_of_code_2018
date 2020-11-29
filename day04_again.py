#!/usr/bin/env python
import re

# f = open('day04_test_input.txt','r')
f = open('day04_input.txt','r')
lines = f.readlines()
f.close()
list.sort(lines)

guard_number = -1
guards = {}
sleep_start_time = -1
guards_sleep_duration = {}
for l in lines:
    regex = '\[\d\d\d\d-(\d\d-\d\d) \d\d:(\d\d)\] (.*)'
    groups = re.search(regex, l)
    date = groups.group(1)
    minute = int(groups.group(2))
    action = groups.group(3)
    print l.strip()
    if '#' in action:
        regex = '#(\d*)'
        guard_number = int(re.search(regex, action).group(1))
        if guard_number not in guards:
            guards[guard_number] = []
            guards_sleep_duration[guard_number] = 0
    elif 'falls asleep' in action:
        sleep_start_time = minute
    elif 'wakes up' in action:
        sleep_end_time = minute
        guards_sleep_duration[guard_number] += sleep_end_time - sleep_start_time
        for m in xrange(sleep_start_time, sleep_end_time):
            guards[guard_number].append(m)
    else:
        print 'Error!'
        exit()

max_sleep_duration = (-1, -1)
for guard in guards_sleep_duration:
    if guards_sleep_duration[guard] > max_sleep_duration[1]:
        max_sleep_duration = (guard, guards_sleep_duration)
guard_number = max_sleep_duration[0]

max_minute = max(set(guards[guard_number]), key=guards[guard_number].count)
# list.sort(guards[guard_number])
# max_minute_count = -1
# max_minute = -1
# minute_count = 0
# last_minute = -1
# for minute in guards:
    # if last_minute == minute:
        # minute_count += 1
    # else:
        # if minute_count > max_minute_count:
            # max_minute_count = minute_count
            # max_minute = last_minute
            # minute_count = 0
        # minute_count 
    # last_minute = minute
print "GUARD: %s | MINUTE: %s | %s" % (
    guard_number,
    max_minute,
    guard_number*max_minute,
)
import ipdb; ipdb.set_trace()
