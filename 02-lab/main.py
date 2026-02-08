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

import circle
import color
import point
from random import randint

# returns a color object with a random rgb value
def rand_color():
  color = color.Color()
  color.setRed(randInt(0,255))
  color.setGreen(randInt(0,255))
  color.setBlue(randInt(0,255))
  return color

# returns a point object with random x and y coords
def rand_point():
  point = point.Point()
  point.setAcross(randInt(0,1000))
  point.setDown(randInt(0,1000))
  return point

# prints num_circles circles to the svg canvas
def print_circles( num_circles ):
  for i in range(0, num_circles):
    color = rand_color()
    point = rand_point()
    radius = randInt( 1, 50 )
    circle = circle.Circle( point, radius, color )
    print(circle.SVG())

print ('<svg height="1000" width="1000">')
print_circles( 1000 )
print ('</svg>')

# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Josh Loftus
# there is nothing below here!

