
import pygame
import emitter

pygame.init()
win=pygame.display.set_mode((800,800))
clc=pygame.time.Clock()
em=emitter.emitter(400,400,42)
em.load_image("circle.png")
em.load_image("star.png")
em.load_image("diamond.png")
em.apply_force(0,100)
while True:
    elapsed=clc.tick()/1000
    evt=pygame.event.poll()
    if evt.type==pygame.QUIT:
        break
    elif evt.type==pygame.MOUSEMOTION:
        x,y=evt.pos
        em.set_pos(x,y)
    #update
    em.update(elapsed)

    #draw
    win.fill((0,0,0))
    em.draw(win)
    pygame.display.flip()
pygame.quit()
