#!/usr/bin/env python

"""Here we load a .TTF font file, and display it in
a basic pygame window. It demonstrates several of the
Font object attributes. Nothing exciting in here, but
it makes a great example for basic window, event, and
font management."""


import pygame
from pygame.locals import *
from pygame.compat import unichr_, unicode_
import sys
import locale


if sys.version_info >= (3,):
    def print_unicode(s):
        e = locale.getpreferredencoding()
        print (s.encode(e, 'backslashreplace').decode())
else:
    def print_unicode(s):
        e = locale.getpreferredencoding()
        print (s.encode(e, 'backslashreplace'))

def main():
    #initialize
    pygame.init()
    resolution = 400, 200
    screen = pygame.display.set_mode(resolution)

##    pygame.mouse.set_cursor(*pygame.cursors.diamond)

    fg = 250, 240, 230
    bg = 5, 5, 5
    wincolor = 40, 40, 90

    #fill background
    screen.fill(wincolor)

    #load font, prepare values
    font = pygame.font.Font(None, 80)
    text = 'Fonty'
    size = font.size(text)

    #no AA, no transparancy, normal
    ren = font.render(text, 0, fg, bg)
    screen.blit(ren, (10, 10))

    #no AA, transparancy, underline
    font.set_underline(1)
    ren = font.render(text, 0, fg)
    screen.blit(ren, (10, 40 + size[1]))
    font.set_underline(0)


    a_sys_font = pygame.font.SysFont("Arial", 60)


    #AA, no transparancy, bold
    a_sys_font.set_bold(1)
    ren = a_sys_font.render(text, 1, fg, bg)
    screen.blit(ren, (30 + size[0], 10))
    a_sys_font.set_bold(0)

    #AA, transparancy, italic
    a_sys_font.set_italic(1)
    ren = a_sys_font.render(text, 1, fg)
    screen.blit(ren, (30 + size[0], 40 + size[1]))
    a_sys_font.set_italic(0)


    # Get some metrics.
    print ("Font metrics for 'Fonty':  %s" % a_sys_font.metrics (text))
    ch = unicode_("%c") % 0x3060
    msg = (unicode_("Font metrics for '%s':  %s") %
           (ch, a_sys_font.metrics (ch)))
    print_unicode(msg)

    ## #some_japanese_unicode = u"\u304b\u3070\u306b"
    ##some_japanese_unicode = unicode_('%c%c%c') % (0x304b, 0x3070, 0x306b)
    
    #AA, transparancy, italic
    ##ren = a_sys_font.render(some_japanese_unicode, 1, fg)
    ##screen.blit(ren, (30 + size[0], 40 + size[1]))
    




    #show the surface and await user quit
    pygame.display.flip()
    while 1:
        #use event.wait to keep from polling 100% cpu
        if pygame.event.wait().type in (QUIT, KEYDOWN, MOUSEBUTTONDOWN):
            break



if __name__ == '__main__': main()
    
