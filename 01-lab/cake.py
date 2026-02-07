#!/usr/local/bin/python3
import sys
sys.path.append('/home/staff/kurban/python')

import csc220

#csc220.showForm("This is the comment on the form area.")  

#textarea = csc220.getInput('textarea')
#textbox = csc220.getInput('textbox')

#print ("<h2>This is at the bottom and can be used for any html output </h2><br>")

#print ("textbox contains <b>{}</b> <br>".format( textbox ))
#print ("textarea contains <b>{}</b> <br>".format( textarea ))

print("<html>")
print("<body>")

print("<svg width=1000 height=1000>")
print_thick_circle()
print_rectangle()
print_thin_circle()
print_text()
print("</svg>") 
 
print("</body>")
print("</html>")

def print_thick_circle():
  print("<circle cx=200 cy=525 r=50 stroke=red stroke-width=10 fill=none />")

def print_rectangle():
  print("<rect width=300 height=100 x=350 y=475 fill=blue />")

def print_thin_circle():
  print("<circle cx=800 cy=525 r=50 stroke=green stroke-width=2 fill=none />")

def print_text():
  print("<text x=465 y=530>Josh Loftus</text>")

# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Josh Loftus 
# there is nothing below here!

