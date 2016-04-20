from display import *
from draw import *
from parser import *
from matrix import *
import sys

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
eep = new_matrix()
ident(eep)
stack = [eep]

if len(sys.argv) == 2:
    f = open(sys.argv[1])

parse_file( f, edges, stack, screen, color )
f.close()
