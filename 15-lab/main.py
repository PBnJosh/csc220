#!/usr/local/bin/python3
import sys
sys.path.append('/home/staff/kurban/python')

import csc220
import avl_tree

csc220.showForm("This is the comment on the form area.")  

textarea = csc220.getInput('textarea')
# textbox = csc220.getInput('textbox')

# print ("<h2>This is at the bottom and can be used for any html output </h2><br>")

# print ("textbox contains <b>{}</b> <br>".format( textbox ))
# print ("textarea contains <b>{}</b> <br>".format( textarea ))

tree = avl_tree.AVLTreeMap()

filename = "/home/staff/kurban/public/lists/web2.txt"
dictionaryFile = open(filename, "r")
for line in dictionaryFile:
    word = line.strip().lower()
    if  len(word) > 0:
        tree[word] = None

misspelled_words = []
lines = textarea.split('\n')
for line in lines:
    words = line.split()
    for word in words:
        if word not in tree:
            misspelled_words.append(word)

print(f'Misspelled words: {misspelled_words}')






# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Josh Loftus
# there is nothing below here!