#!/usr/local/bin/python3
import sys
sys.path.append('/home/staff/kurban/python')

import csc220
import expressiontree

csc220.showForm("This is the comment on the form area.")  

textarea = csc220.getInput('textarea')
# textbox = csc220.getInput('textbox')

# print ("<h2>This is at the bottom and can be used for any html output </h2><br>")

# print ("textbox contains <b>{}</b> <br>".format( textbox ))
# print ("textarea contains <b>{}</b> <br>".format( textarea ))


def resolve_vars(val):
    if (val[0] in "qwertyuiopasdfghjklzxcvbnm"):
        if (val not in variables):
            print(f'ERROR: {val} not defined')
            exit()
        val = variables[val]
    return str(val)

def assign(parts):
    global variables
    var_name = parts[0]
    expr = parts[2:]
    filtered_expr = [ x for x in map(resolve_vars, expr) ]
    etree = expressiontree.build_expression_tree(filtered_expr)
    val = etree.evaluate()
    variables[var_name] = val

def name(parts):
    print("Josh Loftus")

def dump(parts):
    print("Printing all variables:")
    for var in variables:
        print(f'{var} { variables[var] }')

# split input into a list of commands
input_lines = textarea.split('\n')
variables = {}
command = {
    "DUMP": dump,
    "NAME": name,
    "<-": assign
}

print('<pre>')
for line in input_lines:
    
    parts = line.split()
    count = len(parts)

    if (count == 1):
        func = command[ parts[0] ]
    else:
        func = command[ parts[1] ]

    func(parts)

print('</pre>')


# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Josh Loftus
# there is nothing below here!