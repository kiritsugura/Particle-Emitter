import pygame
import random
import math

class emitter():
    def __init__(self,x,y,angle_degrees):
        self.x=x
        self.y=y
        self.prts=[]
        self.cycleAmount=20
        self.cycleTime=.2
        self.speed=300
        self.image=[]
        self.angle=angle_degrees
        self.force_x=1
        self.force_y=1
    def set_speed(self,sp):
        self.speed=sp
    def set_angle(self,an):
        self.angle=an
    def reset_forces(self):
        self.force_x=0
        self.force_y=0
    def set_amount(self,an):
        self.angle=an
    def set_cycle_time(self,ct):
        self.cycleTime=ct
    def set_pos(self,x,y):
        self.x=x
        self.y=y
    def update(self,elapsedTime):
        self.cycleTime-=elapsedTime
        if self.cycleTime<0:
            self.cycleTime=.2
            for num in range(0,self.cycleAmount):
                self.create_part()
        for prt in self.prts:
            if prt.is_alive():
                prt.apply_force(self.force_x*elapsedTime,self.force_y*elapsedTime)
                prt.update(elapsedTime)
            else:
                self.prts.remove(prt)
    def draw(self,window):
        for prt in self.prts:
            prt.draw(window)
    def apply_force(self,x,y):
        self.force_x+=x
        self.force_y+=y
    def load_image(self,fname):
        im=pygame.image.load(fname).convert()
        im.set_colorkey(im.get_at((0,0)))
        self.image.append(im)
    def create_part(self):
        self.prts.append(Particle(2,random.choice(self.image),self.x,self.y,random.randrange(-self.angle,self.angle),random.randint(50,self.speed)))
class Particle():
    def __init__(self,ltime,im,x,y,angle,speed):
        self.ltime=ltime
        self.alpha=255
        self.image=im.copy()
        self.color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.x=x
        self.y=y
        for y in range(0,im.get_height()):
            for x in range(0,im.get_width()):
                if im.get_at((x,y))!=im.get_at((0,0)):
                    im.set_at((x,y),self.color)
        self.dx=speed*math.cos(math.radians(angle))
        self.dy=speed*math.sin(math.radians(angle))
    def is_alive(self):
        return self.ltime>0
    def update(self,elapsed):
        self.ltime-=elapsed
        self.x+=self.dx*elapsed
        self.y+=self.dy*elapsed
    def draw(self,window):
        self.image.set_alpha(255*self.ltime)
        window.blit(self.image,(self.x,self.y))
    def apply_force(self,dx,dy):
        self.dx+=dx
        self.dy+=dy