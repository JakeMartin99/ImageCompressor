"""
Jake Martin
2020
"""

# Import libraries
from pygame import surfarray, image, display
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
screenpix = surfarray.pixels3d(image)

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

# Set the height and width of the screen
size = (resolution[0]*3, resolution[1])
screen = pygame.display.set_mode(size)

pygame.display.set_caption("The Compressor")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
paint = True
# Loop as long as done == False
while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # All drawing code happens after the for loop and but
    # inside the main while not done loop.

    # Clear the screen and set the screen background
    screen.fill(WHITE)
#===============================================================================

    for i in range(resolution[0]):
        for j in range(resolution[1]):
            pygame.draw.rect(screen, (screenpix[i][j][0], screenpix[i][j][1], screenpix[i][j][2]), (i, j, 1, 1))
            if (i*j % 2 == 1):
                pygame.draw.rect(screen, (screenpix[i][j][0], screenpix[i][j][1], screenpix[i][j][2]), (i+resolution[0], j, 1, 1))
                pygame.draw.rect(screen, (screenpix[i][j][0], screenpix[i][j][1], screenpix[i][j][2]), (i+2*resolution[0], j, 1, 1))
            else:
                pygame.draw.rect(screen, colAvg(screenpix, i, j), (i+2*resolution[0], j, 1, 1))



#===============================================================================
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    if paint:
        pygame.display.flip()
        paint = False

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# Be IDLE friendly
pygame.quit()
