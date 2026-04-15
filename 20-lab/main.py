#!/usr/local/bin/python3
import sys
sys.path.append('/home/staff/kurban/python')

import csc220
import graph
import dfs

csc220.showForm("This is the comment on the form area.")  

textarea = csc220.getInput('textarea')
textbox = csc220.getInput('textbox')

# print ("<h2>This is at the bottom and can be used for any html output </h2><br>")

# print ("textbox contains <b>{}</b> <br>".format( textbox ))
# print ("textarea contains <b>{}</b> <br>".format( textarea ))

def mk_html_table(data):
    
    html_table = "<table>\n"
    for row in data:
        html_table += "  <tr>\n"
        for cell in row:
            html_table += f"    <td>{cell}</td>\n"
        html_table += "  </tr>\n"
    html_table += "</table>"
    return html_table

lines = textarea.split('\n')
g = graph.Graph(True)
vNames = []
eNames = []
foundEdges = False

# process data; split in verts and edges
for raw_line in lines:
    line = raw_line.strip()
    if line == "#end":
        foundEdges = True
        continue
    if len(line) < 1:
        continue
    if foundEdges:
        eNames.append(line)
    else:
        vNames.append(line)

# building graph
verts = {}
for vName in vNames:
    if vName in verts:
        continue
    verts[vName] = g.insert_vertex(vName)
for eName in eNames:
    parts = eName.split(', ')
    try:
        v1 = verts[parts[0]]
        v2 = verts[parts[1]]
    except KeyError as e:
        # print(f"Invalid endpoint: {e}.") 
        continue
    else:
        g.insert_edge(v1, v2)

# build table structure for output
table = [["Vertex", "Outgoing Edges"]]
for v in g.vertices():
    edges = []
    for e in g.incident_edges(v, outgoing=True):
        edges.append(e.opposite(v).element())
    table.append([v.element(), "<br/>".join(edges)])
html_table = mk_html_table(table)

# print html table output
print('<style> table, th, td { border:1px solid black; } </style>')
print(f"<div> {html_table} </div>")

in_progress = []
finished = []
cycle_found = False

for v in g.vertices():
    if v not in in_progress or v not in finished:
        # print(f"First call to DFS_cycle, in progress: {in_progress}")
        cycle_found = dfs.DFS_cycle(g, v, in_progress, finished)
    if cycle_found:
        break
if g.vertex_count() < 1:
    message = "Enter a graph description in the textarea."
elif cycle_found:
    message = "This graph is cyclic."
else:
    message = "This graph is acyclic."
print(f"<div> {message} </div>")

# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Josh Loftus
# there is nothing below here!
