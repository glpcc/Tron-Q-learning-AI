import pygame
from car import car 

pygame.init()
dimensions = {'w':1500,'h':800}
canvas = pygame.display.set_mode((dimensions['w'], dimensions['h']))

tron = car()
def main():
    tron.update()
    tron.draw(canvas)

running = True

while running:
    pygame.time.delay(20)
    canvas.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        tron.change_direction('up')
    if keys[pygame.K_DOWN]:
        tron.change_direction('down')
    if keys[pygame.K_LEFT]:
        tron.change_direction('left')
    if keys[pygame.K_RIGHT]:
        tron.change_direction('right')
    
    main()
    pygame.display.flip()

pygame.quit()