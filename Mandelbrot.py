'''
This program will graph the mandelbrot set using pygame. 

f(x) = x^2 + c

Noah Winkel
'''

from cmath import sqrt
import pygame

NUM_ITER = 50
SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1000
X_OFFSET = 7500
Y_OFFSET = -2000
ZOOM = .00005


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("The Mandelbrot Set")

def fractal(done_loading):
   for y in range(SCREEN_HEIGHT):
       if done_loading == False:
           print(round((y/SCREEN_HEIGHT) * 100, 2))
       for x in range(SCREEN_WIDTH):
        real_part_original = new_real_part = (x - SCREEN_WIDTH/2 + X_OFFSET) * ZOOM    #The real part of the complex number 
        imaginary_part_original = new_imaginary_part = (y - SCREEN_HEIGHT/2 - Y_OFFSET)  * ZOOM      #The imaginary part of the complex number

        for i in range(NUM_ITER):
            #equivelent to doing c^2
            real_part_squared = new_real_part * new_real_part - new_imaginary_part * new_imaginary_part 
            imaginary_part_squared = 2 * new_real_part * new_imaginary_part 

            if abs(real_part_squared + imaginary_part_squared) >= 4 or abs(real_part_squared + imaginary_part_squared) <= -4:
                break

            new_real_part = real_part_squared + real_part_original
            new_imaginary_part = imaginary_part_squared + imaginary_part_original 
        
            screen.set_at((x, y), (250 - 10 * i) * 0x10101)
            #pygame.display.update()    #creates a cool scroll animation

def Main():
    run = True
    done_loading = False
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill((255, 255, 255))

        fractal(done_loading)

        pygame.display.update()

        done_loading = True

    pygame.quit()


if __name__ == "__main__":
    Main()
