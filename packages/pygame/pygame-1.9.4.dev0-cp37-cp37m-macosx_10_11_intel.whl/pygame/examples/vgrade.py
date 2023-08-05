#!/usr/bin/env python

"""This example demonstrates creating an image with numpy
python, and displaying that through SDL. You can look at the
method of importing numpy and pygame.surfarray. This method
will fail 'gracefully' if it is not available.
I've tried mixing in a lot of comments where the code might
not be self explanatory, nonetheless it may still seem a bit
strange. Learning to use numpy for images like this takes a
bit of learning, but the payoff is extremely fast image
manipulation in python.

For Pygame 1.9.2 and up, this example also showcases a new feature
of surfarray.blit_surface: array broadcasting. If a source array
has either a width or height of 1, the array is repeatedly blitted
to the surface along that dimension to fill the surface. In fact,
a (1, 1) or (1, 1, 3) array results in a simple surface color fill.

Just so you know how this breaks down. For each sampling of
time, 30% goes to each creating the gradient and blitting the
array. The final 40% goes to flipping/updating the display surface

If using an SDL version at least 1.1.8 the window will have
no border decorations.

The code also demonstrates use of the timer events."""


import os, pygame
from pygame.locals import *

try:
    from numpy import *
    from numpy.random import *
except ImportError:
    raise SystemExit('This example requires numpy and the pygame surfarray module')

pygame.surfarray.use_arraytype('numpy')

timer = 0
def stopwatch(message = None):
    "simple routine to time python code"
    global timer
    if not message:
        timer = pygame.time.get_ticks()
        return
    now = pygame.time.get_ticks()
    runtime = (now - timer)/1000.0 + .001
    print ("%s %s %s" %
           (message, runtime, ('seconds\t(%.2ffps)'%(1.0/runtime))))
    timer = now



def VertGradientColumn(surf, topcolor, bottomcolor):
    "creates a new 3d vertical gradient array"
    topcolor = array(topcolor, copy=0)
    bottomcolor = array(bottomcolor, copy=0)
    diff = bottomcolor - topcolor
    width, height = surf.get_size()
    # create array from 0.0 to 1.0 triplets
    column = arange(height, dtype='float')/height
    column = repeat(column[:, newaxis], [3], 1)
    # create a single column of gradient
    column = topcolor + (diff * column).astype('int')
    # make the column a 3d image column by adding X
    column = column.astype('uint8')[newaxis,:,:]
    #3d array into 2d array
    return pygame.surfarray.map_array(surf, column)



def DisplayGradient(surf):
    "choose random colors and show them"
    stopwatch()
    colors = randint(0, 255, (2, 3))
    column = VertGradientColumn(surf, colors[0], colors[1])
    pygame.surfarray.blit_array(surf, column)
    pygame.display.flip()
    stopwatch('Gradient:')



def main():
    pygame.init()
    pygame.mixer.quit() # remove ALSA underflow messages for Debian squeeze
    size = 600, 400
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode(size, NOFRAME, 0)

    pygame.event.set_blocked(MOUSEMOTION) #keep our queue cleaner
    pygame.time.set_timer(USEREVENT, 500)

    while 1:
        event = pygame.event.wait()
        if event.type in (QUIT, KEYDOWN, MOUSEBUTTONDOWN):
            break
        elif event.type == USEREVENT:
            DisplayGradient(screen)



if __name__ == '__main__': main()
