import pygame
import random

class car():
    def __init__(self):
        self.trace = []
        self.position = [500,500]
        self.next_pos = [490,500]
        self.colour_list = {
            'next':(10,10,10),
            'head':(random.randint(10,255),random.randint(10,255),random.randint(10,255)),
            'trace':(random.randint(10,255),random.randint(10,255),random.randint(10,255))

        }
        self.directions = {
            'up':(0,-10),
            'left':(-10,0),
            'right':(10,0),
            'down':(0,10)
        }
        self.dir = 'left'
    def draw(self,canvas):
        pygame.draw.rect(canvas,self.colour_list['head'] , (self.position[0], self.position[1], 10, 10), 0)
        pygame.draw.rect(canvas,self.colour_list['next'] , (self.next_pos[0], self.next_pos[1], 10, 10), 0)
        for i in self.trace:
            pygame.draw.rect(canvas,self.colour_list['trace'] , (i[0], i[1], 10, 10), 0)
    def change_direction(self,direction):
        new_pos = [self.position[0] + self.directions[direction][0],self.position[1] + self.directions[direction][1]]
        if new_pos != self.position:
            self.next_pos = new_pos
        self.dir = direction
    def update(self):
        if self.alive: 
            self.trace.append(self.position)
            self.position = self.next_pos
            self.next_pos = [self.next_pos[0] + self.directions[self.dir][0],self.next_pos[1] + self.directions[self.dir][1]]

        



