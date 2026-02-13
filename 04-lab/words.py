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

# Count words, and exit if there's less than 100
num_words = len(words)
if num_words < 100:
    print("<p> Where are all my wonderful words? </p>")
    exit()

# Calculate average length of words
word_lengths = [ len(word) for word in words ]
avg_word_len = statistics.mean(word_lengths)

# Sort words into ascending lexicographical order
words.sort()

print(f"<p> There are {num_words} words in this input. </p>")
print(f"<p> The average length of the words in this input is {avg_word_len}. </p>")
print(words)

# Print first 100 words from sorted list into a 10x10 grid
for i in range(10):
    start = i * 10
    print (f"<p> {words[start : start + 10]} </p>")



# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Josh Loftus 
# there is nothing below here!