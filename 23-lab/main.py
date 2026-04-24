#!/usr/local/bin/python3
import sys
sys.path.append('/home/staff/kurban/python')

import csc220
import graph
import mst

# csc220.showForm("This is the comment on the form area.")  
csc220.showForm("<br/>")

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


def MST_print(tree, message):
    counter = 0
    table = [["Edge"]]
    for e in tree:
        table.append([e])
        counter = counter + e.element()
    html_table = mk_html_table(table)
    # print html table output
    print('<style> table, th, td { border:1px solid black; } </style>')
    print(f"<div> <h2>{message}</h2> {html_table} </div>")
    print(f"<div> <b>Total Weight: {counter}</b> </div>")

# get graph data
data = csc220.getInput('textarea')
lines = data.split('\n')
g = graph.Graph(False)
vNames = []
eNames = []
foundEdges = False

# process data; split into verts, edges, and weights
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
        parent = verts[parts[0]]
        child = verts[parts[1]]
        weight = float(parts[2])
    except KeyError as e:
        continue
    else:
        g.insert_edge(parent, child, weight)

# build table structure for output
table = [["Parent", "Child", "Weight"]]
for v in g.vertices():
    parent = v.element()
    for e in g.incident_edges(v, outgoing=True):
        child = e.opposite(v).element()
        weight = e.element()
        table.append([parent, child, weight])
html_table = mk_html_table(table)

# print html table output
print('<style> table, th, td { border:1px solid black; } </style>')
print(f"<div> <h2>Your Graph</h2> {html_table} </div>")

# run Kruskal and output MST & total weight
K_counter = 0
K_tree = mst.MST_Kruskal(g)
MST_print(K_tree, "Kruskal's MST")

# run Prims and output MST & total weight
P_counter = 0
P_tree = mst.MST_PrimJarnik(g)
MST_print(P_tree, "Prim's MST")

# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Josh Loftus