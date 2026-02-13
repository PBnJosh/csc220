#!/usr/local/bin/python3
import statistics
import sys
sys.path.append('/home/staff/kurban/python')

import csc220

csc220.showForm("This is the comment on the form area.")  

# textbox = csc220.getInput('textbox')

# print ("<h2>This is at the bottom and can be used for any html output </h2><br>")

# print ("textbox contains <b>{}</b> <br>".format( textbox ))
# print ("textarea contains <b>{}</b> <br>".format( textarea ))

textarea = csc220.getInput('textarea')
words = textarea.split()
num_words = len(words)
word_lengths = [ len(word) for word in words ]
avg_word_len = statistics.mean(word_lengths)

print(f"There are {num_words} words in this input.")
print(f"The average length of the words in this input is {avg_word_len}.")



# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Josh Loftus 
# there is nothing below here!