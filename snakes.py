#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 20:15:49 2018

@author: arepo
"""

import numpy as np
from matplotlib import pyplot as plt




def snakestep(world, position):
    
    '''
    get perception and act accordingly
    '''
    perception = get_percept(position)
    action = act_on(perception, position, world)
    
    
    '''
    update snake's position
    '''
    snakeposition = np.zeros((2))
    snakeposition[:] = position[:] + action[:]
    snakeposition = snakeposition.astype(int)
    
    
    '''
    fix the confines of the world (how poetic!)
    '''
    world[0,:] = -2
    world[-1,:] = -2
    world[:,0] = -2
    world[:,-1] = -2
    
    '''
    update position - later on, it will be the tail part switching places with
    the head part.
    '''
    world[position[0], position[1]] = 0
    world[snakeposition[0],snakeposition[1]] = 1
    
    return snakeposition, position, world


def act_on(perception, position, world):
    '''
    atm returns a random step
    '''
    
    stepdirection = np.random.randint(-1,2,2)  
    
    snakeposition = np.zeros((2))
    snakeposition[:] = position[:] + stepdirection[:]
    
    if snakeposition[0] < 0 or snakeposition[0] > (world.shape[0]-1) or snakeposition[1] < 0 or snakeposition[1] > (world.shape[1]-1):
        stepdirection = act_on(perception, position, world)
     
    return stepdirection

    


def get_percept(position):
    '''
    atm just a placeholder
    '''
    return 1


def generate_world(dim1, dim2, n_foodpoints):
    '''
    generates a world with defined parameters
    '''
    world = np.zeros((dim1,dim2))
    world[0,:] = -2
    world[-1,:] = -2
    world[:,0] = -2
    world[:,-1] = -2
    
    foodpoints1 = np.random.randint(1,dim1-1,n_foodpoints)
    foodpoints2 = np.random.randint(1,dim2-1,n_foodpoints)
    
    world[foodpoints1[:],foodpoints2[:]] = + 2

    return world


'''
the "main function"
'''
    
world = generate_world(10,10,20)

pos = np.random.randint(1,9,2)

#newpos, poss, world = snakestep(world, pos)
#pos = newpos
plt.imshow(world)    
for i in range(100):
    '''
    loop to check if errors occurr
    '''
    newpos, poss, world = snakestep(world, pos)
    pos = newpos
    
plt.imshow(world) 


    
    

