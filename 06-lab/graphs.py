#!/usr/local/bin/python3
import sys
import random
import csv
sys.path.append('/home/staff/kurban/python')

import csc220

# csc220.showForm("This is the comment on the form area.")  

# textarea = csc220.getInput('textarea')
# textbox = csc220.getInput('textbox')

# print ("<h2>This is at the bottom and can be used for any html output </h2><br>")

# print ("textbox contains <b>{}</b> <br>".format( textbox ))
# print ("textarea contains <b>{}</b> <br>".format( textarea ))


def quicksort(arr, a, b):
    global count
    if a >= b: return
    pivot = arr[b]
    count += 1
    left = a
    right = b - 1

    while (left <= right):
        while (left <= right):
            count += 1
            if (arr[left] < pivot):
                left += 1
            else:
                break
        
        while (left <= right):
            count += 1
            if (arr[left] > pivot):
                right -= 1
            else:
                break
        
        if (left <= right):
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            count += 2

    arr[left], arr[b] = arr[b], arr[left]
    count += 2
    quicksort(arr, a, left - 1)
    quicksort(arr, left + 1, b)

# returns a list with random elements between min_val and max_val
def make_list(size, min_val, max_val):
    return list( random.randint(min_val, max_val) for i in range(size) )

num_lists = 350
minimum = -25000
maximum = 25000
tuples = []

for i in range(num_lists):
    count = 0
    size = random.randint(1000, 5000)
    l = make_list(size, minimum, maximum)
    quicksort(l, 0, len(l) - 1)
    tuples.append( (size, count) )
print(tuples)

with open('data.csv', 'w') as csvfile:
    ghost_writer = csv.writer(csvfile)
    ghost_writer.writerow( ["List Size", "List Accesses"] )
    ghost_writer.writerows(tuples)



# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Josh Loftus
# there is nothing below here!