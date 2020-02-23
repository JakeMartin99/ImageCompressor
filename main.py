"""
Jake Martin
2020
"""

# Import libraries
from pygame import surfarray, image, display
from copy import deepcopy
import pygame
import numpy

# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#Initializations
image = image.load(input("Enter image filename: "))
resolution = (image.get_width(),image.get_height())
surfarray.use_arraytype("numpy")
pix = surfarray.pixels3d(image)

#Functions
def colAvg(pixels, x: int, y: int)->(int, int, int):
    neighbors = 0
    total = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            try:
                total[0] += pixels[x-1+i][y-1+j][0]
                total[1] += pixels[x-1+i][y-1+j][1]
                total[2] += pixels[x-1+i][y-1+j][2]
                neighbors += 1
            except:
                pass

    return (total[0] / neighbors, total[1] / neighbors, total[2] / neighbors)

def disp_img(pix):
    res = [len(pix), len(pix[0])]
    for i in range(res[0]):
        for j in range(res[1]):
            pygame.draw.rect(screen, (pix[i][j][0], pix[i][j][1], pix[i][j][2]), (i, j, 1, 1))

def space_img(pix):
    pixels = deepcopy(pix)
    res = [len(pix), len(pix[0])]
    for i in range(res[0]):
        for j in range(res[1]):
            if i*j%2 == 0:
                pixels[i][j] = WHITE
    return pixels

def cmpr_img(pix):
    pixels = deepcopy(pix)
    res = [len(pix), len(pix[0])]
    for i in range(res[0]):
        for j in range(res[1]):
            if i*j%2 == 0:
                pixels[i][j] = colAvg(pix, i, j)
    return pixels

# Set the height and width of the screen
size = (resolution[0], resolution[1])
screen = pygame.display.set_mode(size)

pygame.display.set_caption("The Compressor")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
mode = 0
# Loop as long as done == False
while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            mode += 1

    # All drawing code happens after the for loop and but
    # inside the main while not done loop.

    # Clear the screen and set the screen background
    screen.fill(WHITE)
#===============================================================================


    if mode == 0:
        disp_img(pix)
    elif mode == 1:
        disp_img(space_img(pix))
    elif mode == 2:
        disp_img(cmpr_img(pix))


#===============================================================================
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(3)

    if mode > 2:
        mode = 0

# Be IDLE friendly
pygame.quit()
