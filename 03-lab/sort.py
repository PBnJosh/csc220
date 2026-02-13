#!/usr/local/bin/python3
from random import randint
import csv

def insertion_sort(arr):

    visits = 0

    for i in range( 1, len(arr) ):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            visits += 1
        arr[j + 1] = key

    return visits

def make_list(size, min_val, max_val):
    return list( randint(min_val, max_val) for i in range(size) )

num_lists = 350
min_val = 0
max_val = 10000
tuples = []

for i in range(num_lists):
    size = randint(1000, 5000)
    l = make_list(size, min_val, max_val)
    visits = insertion_sort(l)
    tuples.append( (size, visits) )

with open('data.csv', 'w') as csvfile:
    ghost_writer = csv.writer(csvfile)
    ghost_writer.writerow( ["Size", "List Accesses"] )
    ghost_writer.writerows(tuples) 


# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# your name 
# there is nothing below here!