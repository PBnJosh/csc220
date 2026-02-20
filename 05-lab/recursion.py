#!/usr/local/bin/python3
import sys
sys.path.append('/home/staff/kurban/python')

import csc220

csc220.showForm("This is the comment on the form area.")  

textarea = csc220.getInput('textarea')
# textbox = csc220.getInput('textbox')

# print ("<h2>This is at the bottom and can be used for any html output </h2><br>")

# print ("textbox contains <b>{}</b> <br>".format( textbox ))
# print ("textarea contains <b>{}</b> <br>".format( textarea ))

def path_can_win(pos):

    if (pos == len(board) - 1):
        path.append(pos)
        return True

    if ( (pos in visited) or (pos < 0) or (pos >= len(board) ) or (board[pos] == 0) ):
        return False
    
    visited.add(pos)

    if ( path_can_win( pos + board[pos] ) or path_can_win( pos - board[pos] ) ):
        path.append(pos)
        return True

    return False

game_vals = textarea.split()
board = list( int( game_vals[i] ) for i in range( len(game_vals) ) )

path = []
visited = set()

path_can_win(0)
path.reverse()
print(f"The winning path (unwinnable if empty): {path}")



# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Josh Loftus
# there is nothing below here!