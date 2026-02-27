#!/usr/local/bin/python3
import sys
sys.path.append('/home/staff/kurban/python')

import csc220

# csc220.showForm("This is the comment on the form area.")  

textarea = csc220.getInput('textarea')
# textbox = csc220.getInput('textbox')

# print ("<h2>This is at the bottom and can be used for any html output </h2><br>")

# print ("textbox contains <b>{}</b> <br>".format( textbox ))
# print ("textarea contains <b>{}</b> <br>".format( textarea ))
textarea = "NAME\nx<-8\nDUMP"

dictionary = {}

# takes a string of the format "x<-6" and adds or modifies the entry in the dictionary
def store_variable(line):
    global dictionary
    
    vals = line.split('<-')

    # throw "error" if the syntax is invalid and end program
    if ( (len(vals) != 2) or ( vals[1] == '') ):
        print(f'Invalid Syntax: {line}')
        exit()
        
    # try storing variable as a float
    try:
        num = float( vals[1] )
        dictionary[ vals[0] ] = num
    except:
        # not a float; try storing value of another variable
        try:
            dictionary[ vals[0] ] = dictionary[ vals[1] ]
        except:
            # other variable is not defined
            print(f'Error: variable { vals[1] } is not defined')
            exit()

# split input into a list of commands
input_lines = textarea.split('\n')

# process each line of input
for i in input_lines:
    
    # remove all spaces from the input line
    line = i.replace(' ', '')

    # process 'NAME' instruction
    if (line == "NAME"):
        print("Josh Loftus")

    # process 'DUMP' instruction
    elif (line == "DUMP"):
        print("Printing all variables:")
        for var in dictionary:
            print(f'{var} { dictionary[var] }')
    
    # process variable assignment instruction
    elif ( line.__contains__('<-') ):
        store_variable(line)
    
    else:
        print(f"Error: unrecognized syntax: {i}")
        exit()
    


# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Josh Loftus 
# there is nothing below here!