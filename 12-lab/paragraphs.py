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

class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

nodes = []
frequencies = {}

def calculate_frequencies(string):
    global frequencies
    for char in string:
        if char not in frequencies:
            freq = string.count(char)
            frequencies[char] = freq
            nodes.append(Node(char, freq))

def build_huffman_tree():
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.freq)
        left = nodes.pop(0)
        right = nodes.pop(0)
        
        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        nodes.append(merged)

    return nodes[0]

def generate_huffman_codes(node, current_code, codes):
    if node is None:
        return

    if node.char is not None:
        codes[node.char] = current_code

    generate_huffman_codes(node.left, current_code + '0', codes)
    generate_huffman_codes(node.right, current_code + '1', codes)

def huffman_encoding(word):
    global nodes
    nodes = []
    calculate_frequencies(word)
    root = build_huffman_tree()
    codes = {}
    generate_huffman_codes(root, '', codes)
    return codes

string = textarea
codes = huffman_encoding(string)
encoded_string = ''.join(codes[char] for char in string)

# print("String:", string)
# print("Huffman code:", encoded_word)
# print("Conversion table:", codes)

print('<p> Character Frequency: </p>')
print('<style> table, th, td { border:1px solid black; } </style>')
print('<table style="width:5%">')

freq_keys = frequencies.keys()
for key in freq_keys:
    
    print('<tr>')

    print(f'<td> {key} : {frequencies[key]} </td>')

    print('</tr>')

print('</table>')

print('<p> Huffman Codes: </p>')
print('<style> table, th, td { border:1px solid black; } </style>')
print('<table style="width:5%">')

code_keys = codes.keys()
for key in code_keys:
    
    print('<tr>')

    print(f'<td> {key} : {codes[key]} </td>')

    print('</tr>')

print('</table>')

# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Josh Loftus
# there is nothing below here!