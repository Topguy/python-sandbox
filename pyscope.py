import os
import pygame
import time
import random

class PyScope:
    screen = None
    
    def __init__(self):
        """Initializes a new pygame screen using the framebuffer"""
        # Based on "Python GUI in Linux frame buffer"
        # https://www.karoltomala.com/blog/?p=679
        disp_no = os.environ.get("DISPLAY")
        if disp_no:
            print(f"I'm running under X display = {disp_no}")
        
        # Check which frame buffer drivers are available
        # Start with fbcon since directfb hangs with composite output
        drivers = ['fbcon', 'directfb', 'svgalib','xkb','x11']
        found = False
        for driver in drivers:
            # Make sure that SDL_VIDEODRIVER is set
            if not os.environ.get('SDL_VIDEODRIVER'):
                os.putenv('SDL_VIDEODRIVER', driver)
            try:
                pygame.display.init()
            except pygame.error:
                print(f"Driver: {driver} failed.")
                continue
            found = True
            break
    
        if not found:
            raise Exception('No suitable video driver found!')
        
        size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        print(f"Framebuffer size: {size[0]} x {size[1]}")
        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        # Clear the screen to start
        self.screen.fill((0, 0, 0))        
        # Initialise font support
        pygame.font.init()
        # Render the screen
        pygame.display.update()

    def __del__(self):
        """Destructor to make sure pygame shuts down, etc."""
        pygame.quit()

    def test(self):
        # Fill the screen with red (255, 0, 0)
        red = (255, 0, 0)
        self.screen.fill(red)
        # Update the display
        pygame.display.update()
        time.sleep(3)

# Create an instance of the PyScope class
scope = PyScope()
scope.test()
