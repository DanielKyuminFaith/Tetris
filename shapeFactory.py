import pygame
from lockedShape import LockedShape
import numpy as np
import math
import copy
import random
from shape import Shape, TShape, LShape, IShape, JShape, OShape, SShape, ZShape
class ShapeFactory():
    def __init__ (self):
        self.previousNum = 0
    
    def randomizer(self):
        shape = random.randint(1, 7)
        if shape == self.previousNum:
            shape = random.randint(1, 7)
            self.previousNum = shape
            if shape == 1:
                shape = IShape()
            if shape == 2:
                shape = JShape()
            if shape == 3:
                shape = LShape()
            if shape == 4:
                shape = OShape()
            if shape == 5:
                shape = SShape()
            if shape == 6:
                shape = TShape()
            if shape == 7:
                shape = ZShape()
            return shape
        else:
            self.previousNum = shape
            if shape == 1:
                shape = IShape()
            if shape == 2:
                shape = JShape()
            if shape == 3:
                shape = LShape()
            if shape == 4:
                shape = OShape()
            if shape == 5:
                shape = SShape()
            if shape == 6:
                shape = TShape()
            if shape == 7:
                shape = ZShape()
            return shape
        
    
