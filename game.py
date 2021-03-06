# Import a library of functions called 'pygame'
import pygame
import graph as graphs
from graph import Graph
from graph import Node
import drawablenode
from drawablenode import *
import astar
# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PAD = (5, 5)
ROWS = 10
COLS = 10
WIDTH = 30
HEIGHT = 30
SCREEN_WIDTH = COLS * (PAD[0] + WIDTH) + PAD[1]
SCREEN_HEIGHT = ROWS * (PAD[0] + HEIGHT) + PAD[1]
# Set the height and width of the SCREEN

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
search_space = Graph([ROWS, COLS])

NODES = []
for i in range(ROWS):
    for j in range(COLS): 
        node = search_space.get_node([i, j])
        NODES.append(DrawableNode(node))

pygame.display.set_caption("Example code for the draw module")

# Loop until the user clicks the close button.
DONE = False
CLOCK = pygame.time.Clock()

pygame.font.init()
font1 = pygame.font.Font(None, 14)
font2 = pygame.font.Font(None, 28)
for n in NODES:
    for nds in graphs.get_neighbors(n, search_space):
        for nods in NODES:
            if nds.value[0] == nods.value[0] and nds.value[1] == nods.value[1]:
                n.adjacents.append(nods)  # map onto NODES
                break

NODES[3].walkable=False
NODES[13].walkable=False
NODES[23].walkable=False
NODES[33].walkable=False
NODES[32].walkable=False
NODES[31].walkable=False
test1 = astar.astar(NODES[0], NODES[44])

for n in NODES:
    n.walkable = True   
    n.parent = None
    n.g = 0
    n.f = 0
    n.h = 0

NODES[21].walkable = False
NODES[22].walkable = False
NODES[23].walkable = False
test2 = astar.astar(NODES[2], NODES[42])

for n in NODES:
    n.walkable = True
    n.parent = None
    n.g = 0
    n.f = 0
    n.h = 0


NODES[33].walkable = False
NODES[32].walkable = False
NODES[34].walkable = False
NODES[42].walkable = False
NODES[44].walkable = False
NODES[52].walkable = False
NODES[54].walkable = False
NODES[62].walkable = False
NODES[64].walkable = False
test3 = astar.astar(NODES[3], NODES[53])
node1 = NODES[0]
print node1.walkable
while not DONE:

    
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    CLOCK.tick(9)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            DONE = True  # Flag that we are DONE so we exit this loop

    # All drawing code happens after the for loop and but
    # inside the main while DONE==False loop.

    # Clear the SCREEN and set the SCREEN background
    SCREEN.fill(WHITE)
    # Draw a circle
    for i in NODES:
        i.draw(SCREEN, font1)

    # Go ahead and update the SCREEN with what we've drawn.
    # This MUST happen after all the other drawing commands.
    bg = pygame.Surface((SCREEN.get_size()[0] / 3, SCREEN.get_size()[1] / 3))
    bg.fill(BLACK)
    textrect = bg.get_rect()
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()
