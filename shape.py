import pygame
from lockedShape import LockedShape
import numpy as np
import math
import copy

class Shape:
    def __init__ (self):
        self.tooFar = False
        self.color = (0, 0, 0)
        self.pieces = []
        self.rotation = 0
        self.anchor = [0, 0]
        #  make a check to see if basic rotation is ok?
        #  modify by -1 0, fails -1, 1, faails 0,-2 etc etc
        # the wall kick test will not modify the location of the piece until a given wall kick test passes

        #  test(self.pieces, (-1, 0))

        #   take a piece, and test to see if lockedshape has pices at pice location + -1, 0

        self.basicWallKick = {
                            (0,1):[(-1, 0), (-1, 1), (0, -2), (-1, -2)], #0 >> 1
                            (1,2):[(1, 0), (1, -1), (0, 2), (1, 2)],     #1 >> 2
                            (2,3):[(1, 0), (1, 1), (0, -2), (1, -2)],    #2 >> 3
                            (3,0):[(-1, 0), (-1, -1), (0, 2), (-1, 2)],  #3 >> 0
                            (1,0):[(1, 0), (1, -1), (0, 2), (1, 2)],     #1 >> 0
                            (2,1):[(-1, 0), (-1, 1), (0, -2), (-1, -2)], #2 >> 1
                            (3,2):[(-1, 0), (-1, -1), (0, 2), (-1, 2)],  #3 >> 2
                            (0,3):[(1, 0), (1, 1), (0, -2), (1, -2)]}    #0 >> 3
        
#         0 = spawn state
#         1 = state resulting from a clockwise rotation ("right") from spawn
#         2 = state resulting from 2 successive rotations in either direction from spawn.
#         3 = state resulting from a counter-clockwise ("left") rotation from spawn
        
# -4, -3, -2  0, 1, 2, 3, 4, 5, 6
#          # 0   #  #  #
#         # 1       #
#         # 2
#         # 3
    

    
    def fall(self, lockedShape: LockedShape):
        fallCheck = True
        # for each piece in the falling shape, you must check against each piece in each shape in the lockedShape
        # list of shapes from lockedShape
            # each shape has a list of pieces 
            # you need to make a check against each piece within each shape.

        for i in range(len(self.pieces)):
            if self.pieces[i][1] == 19:
                fallCheck = False
        
        for i in range(len(lockedShape.shapes)):
            # set a variable equal to the current shape
            # loop through the peices of the shape variable that was set
            for k in range (len(lockedShape.shapes[i].pieces)):

                # i goes through the shapes from lockedShape
                # k goes through the pieces from shapes in lockedShape
                
                # we need another something that goes through the pieces in self.pieces and compares them to the pieces from shapes in lockedShape
                # lockedShape.shapes = [Shape()]
                # shape = lockedShape[0]
                # shape.pieces = [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
                for q in range (len(self.pieces)):
                    if self.pieces[q][0] == lockedShape.shapes[i].pieces[k][0] and self.pieces[q][1]+1 == lockedShape.shapes[i].pieces[k][1]:
                        fallCheck = False


        # if moved down as a result of pressing down, add 1 point
        
            
        if fallCheck == True:
            for i in range(len(self.pieces)):
                self.pieces[i][1] += 1
        else:
            self.tooFar = True
        return fallCheck
    def right(self, lockedShape: LockedShape):
        if not self.tooFar:
            rightCheck = True
            for j in range(len(self.pieces)):
                if self.pieces[j][0] == 9:
                    rightCheck = False
                for i in range(len(lockedShape.shapes)):
                    for k in range (len(lockedShape.shapes[i].pieces)):
                        for q in range (len(self.pieces)):
                            if self.pieces[q][0]+1 == lockedShape.shapes[i].pieces[k][0] and self.pieces[q][1] == lockedShape.shapes[i].pieces[k][1]:
                                rightCheck = False
            if rightCheck == True:
                for i in range(len(self.pieces)):
                    self.pieces[i][0] += 1
            return rightCheck
        return False
    def left(self, lockedShape: LockedShape):
        if not self.tooFar:
            leftCheck = True
            for j in range(len(self.pieces)):
                if self.pieces[j][0] == 0:
                    leftCheck = False
                for i in range(len(lockedShape.shapes)):
                    for k in range (len(lockedShape.shapes[i].pieces)):
                        for q in range (len(self.pieces)):
                            if self.pieces[q][0]-1 == lockedShape.shapes[i].pieces[k][0] and self.pieces[q][1] == lockedShape.shapes[i].pieces[k][1]:
                                leftCheck = False
        
            if leftCheck == True:
                for i in range(len(self.pieces)):
                    self.pieces[i][0] -= 1
            return leftCheck
        return False

    def hardDrop(self, lockedShape: LockedShape):
        rows = 0
        fallCheck = True
        while fallCheck == True:
            
            for j in range(len(self.pieces)):
                if self.pieces[j][1] == 19:
                   fallCheck = False
                

            for i in range(len(lockedShape.shapes)):
                for k in range (len(lockedShape.shapes[i].pieces)):
                    for q in range (len(self.pieces)):
                        if self.pieces[q][0] == lockedShape.shapes[i].pieces[k][0] and self.pieces[q][1]+1 == lockedShape.shapes[i].pieces[k][1]:
                            fallCheck = False
            if fallCheck == True:
                for i in range(len(self.pieces)):
                    self.pieces[i][1] += 1
                rows += 1
        # find how many incriments piece moved down, mmultiply with point multiplier

        self.tooFar = True
        return rows

    # def clearCheck(self, lockedShape: LockedShape):
        # successfulChecks = 0
        # involvedPieces = []
        # 
# 
# 
        # for q in range (len(self.pieces)):
            # for i in range(len(lockedShape.shapes)):
                # for k in range (len(lockedShape.shapes[i].pieces)):            
                    # if self.pieces[q][1] == lockedShape.shapes[i].pieces[k][1]:
                        # for p in range(len(involvedPieces)):
                            # if [lockedShape.shapes[i].pieces[k][0], lockedShape.shapes[i].pieces[k][1]] != [involvedPieces[p][0], involvedPieces[p][1]]:
                                # involvedPieces.append([lockedShape.shapes[i].pieces[k][0], lockedShape.shapes[i].pieces[k][1]])
        # print(involvedPieces)


    def rotateLeft(self, lockedShape: LockedShape):
        print(self.rotation)
        # define anchor point?
        
        # rotate shape
        rotated = []
        newRotation = self.rotation - 1
        if newRotation == -1:
            newRotation = 3
            
        anchorX = self.pieces[2][0]
        anchorY = self.pieces[2][1]
        matrixLeftModifier = np.array(([0, -1],
                                        [1, 0])) 
        # TODO: Consider better rotation method
        
        for i in range(len(self.pieces)):
            self.pieces[i][0] -= anchorX
            self.pieces[i][1] -= anchorY
            rotated = np.matmul(np.array([self.pieces[i][0], self.pieces[i][1]]), matrixLeftModifier)
            self.pieces[i] = rotated
            self.pieces[i][0] += anchorX
            self.pieces[i][1] += anchorY
        
        needToWallKick = (self.doesCollideWithWallOrFloor(self.pieces) or self.doesCollideWithLockedShape(self.pieces, lockedShape))
        # define a boolean indiciating if we did wallkick in order to satisfy rotation
        didWallKick = False
        if needToWallKick:
            kickSet = self.basicWallKick[(self.rotation, newRotation)]
            for kickCheck in range(4):
                print(kickSet[kickCheck])
                kickShift = kickSet[kickCheck] # it is a list of two numbers.
                # make an array that has all the pieces, but with kickShift applied.
                shiftedPieces = copy.deepcopy(self.pieces)
                for piece in range(len(self.pieces)):
                    shiftedPieces[piece][0] += kickShift[0]
                    shiftedPieces[piece][1] -= kickShift[1]
                # now make a check to see if shiftedPieces collides with board or lockedShape
                if not self.doesCollideWithWallOrFloor(shiftedPieces) and not self.doesCollideWithLockedShape(shiftedPieces, lockedShape):
                    self.pieces = shiftedPieces
                    # flip the boolean to true to indicate we did wall kick succusfully
                    didWallKick = True
                    break
        # check if needToWallKick is true, and if didWallKick is false. If the conditions are satisfied, then rotate back. We were unable to wallkick and do a good rotation.        
        if needToWallKick == True and didWallKick == False:
            matrixRightModifier = np.array(([0, 1],
                                           [-1, 0])) 
            # TODO: Consider better rotation method
            for i in range(len(self.pieces)):

                self.pieces[i][0] -= anchorX
                self.pieces[i][1] -= anchorY
                rotated = np.matmul(np.array([self.pieces[i][0], self.pieces[i][1]]), matrixRightModifier)
                self.pieces[i] = rotated
                self.pieces[i][0] += anchorX
                self.pieces[i][1] += anchorY
        else:
            self.rotation = newRotation
        # define anchor point?
        # if not self.tooFar:
            # rotated = []
            # anchorX = self.pieces[2][0]
            # anchorY = self.pieces[2][1]
            # matrixLeftModifier = np.array(([0, -1],
                                        #    [1, 0])) 
            # TO DO: Consider better rotation method
            # for i in range(len(self.pieces)):
# 
                # self.pieces[i][0] -= anchorX
                # self.pieces[i][1] -= anchorY
                # rotated = np.matmul(np.array([self.pieces[i][0], self.pieces[i][1]]), matrixLeftModifier)
                # self.pieces[i] = rotated
                # self.pieces[i][0] += anchorX
                # self.pieces[i][1] += anchorY

    def rotateRight(self, lockedShape: LockedShape):
        
        print(self.rotation)
        # define anchor point?
        
        # rotate shape
        rotated = []
        newRotation = self.rotation + 1
        if newRotation == 4:
            newRotation = 0
        
        if self.rotation == 1 and newRotation == 2:
                print("break!")
            
        anchorX = self.pieces[2][0]
        anchorY = self.pieces[2][1]
        matrixRightModifier = np.array(([0, 1],
                                        [-1, 0])) 
        # TODO: Consider better rotation method
        
        for i in range(len(self.pieces)):
            self.pieces[i][0] -= anchorX
            self.pieces[i][1] -= anchorY
            rotated = np.matmul(np.array([self.pieces[i][0], self.pieces[i][1]]), matrixRightModifier)
            self.pieces[i] = rotated
            self.pieces[i][0] += anchorX
            self.pieces[i][1] += anchorY
            
        needToWallKick = (self.doesCollideWithWallOrFloor(self.pieces) or self.doesCollideWithLockedShape(self.pieces, lockedShape))
        # define a boolean indiciating if we did wallkick in order to satisfy rotation
        didWallKick = False
        if needToWallKick:
            kickSet = self.basicWallKick[(self.rotation, newRotation)]
            for kickCheck in range(len(kickSet)):
                print(kickSet[kickCheck])
                kickShift = kickSet[kickCheck] # it is a list of two numbers.
                # make an array that has all the pieces, but with kickShift applied.
                shiftedPieces = copy.deepcopy(self.pieces)
                for piece in range(len(self.pieces)):
                    shiftedPieces[piece][0] += kickShift[0]
                    shiftedPieces[piece][1] -= kickShift[1]
                # now make a check to see if shiftedPieces collides with board or lockedShape
                if not self.doesCollideWithWallOrFloor(shiftedPieces) and not self.doesCollideWithLockedShape(shiftedPieces, lockedShape):
                    self.pieces = shiftedPieces
                    # flip the boolean to true to indicate we did wall kick succusfully
                    didWallKick = True
                    break
        # check if needToWallKick is true, and if didWallKick is false. If the conditions are satisfied, then rotate back. We were unable to wallkick and do a good rotation.  
        if needToWallKick == True and didWallKick == False: 
            

            matrixLeftModifier = np.array(([0, -1],
                                           [1, 0])) 
            # break point that only stops the program if the rotation is 1 >> 2
            # if piece is of type T, 

            # TODO: Consider better rotation method
            for i in range(len(self.pieces)):

                self.pieces[i][0] -= anchorX
                self.pieces[i][1] -= anchorY
                rotated = np.matmul(np.array([self.pieces[i][0], self.pieces[i][1]]), matrixLeftModifier)
                self.pieces[i] = rotated
                self.pieces[i][0] += anchorX
                self.pieces[i][1] += anchorY
        else:
            self.rotation = newRotation
            

            
    # returns if the piece collides with the walls of the board
    def doesCollideWithWallOrFloor(self, pieces):
        for i in range(len(pieces)):
            # board height is 19
            if pieces[i][0] < 0 or pieces[i][0] > 9 or pieces[i][1] > 19:
                return True            
        return False
    
    def doesCollideWithLockedShape(self, pieces, lockedShape: LockedShape):
        for r in range(len(lockedShape.shapes)):
            for k in range (len(lockedShape.shapes[r].pieces)):
                for q in range (len(pieces)):
                    if pieces[q][0] == lockedShape.shapes[r].pieces[k][0] and pieces[q][1] == lockedShape.shapes[r].pieces[k][1]:
                        return True
        

class LShape(Shape):
    def __init__ (self):
        super().__init__()
        self.color = (242, 174, 48)
        self.pieces = [              [5,0],
                       [3,1], [4,1], [5,1]]
        self.tooFar = False
class TShape(Shape):
    def __init__ (self):
        super().__init__()
        self.color = (180, 56, 224)
        self.pieces = [       [4,0],
                       [3,1], [4,1], [5,1]]
        self.tooFar = False
class IShape(Shape):
    def __init__ (self):
        super().__init__()
        self.color = (82, 222, 247)
        self.pieces = [[3, 0], [4, 0], [5, 0], [6, 0]]
        self.tooFar = False
        self.anchor = [4.5, 0.5]
        self.basicWallKick = {
                            (0,1):[(-2, 0),	( 1, 0),	(-2,-1),	( 1, 2)], #0 >> 1
                            (1,2):[(-1, 0),	( 2, 0),	(-1, 2),	( 2,-1)],     #1 >> 2
                            (2,3):[( 2, 0),	(-1, 0),	( 2, 1),	(-1,-2)],    #2 >> 3
                            (3,0):[( 1, 0),	(-2, 0),	( 1,-2),	(-2, 1)],  #3 >> 0
                            (1,0):[( 2, 0),	(-1, 0),	( 2, 1),	(-1,-2)],     #1 >> 0
                            (2,1):[( 1, 0),	(-2, 0),	( 1,-2),	(-2, 1)], #2 >> 1
                            (3,2):[(-2, 0),	( 1, 0),	(-2,-1),	( 1, 2)],  #3 >> 2
                            (0,3):[(-1, 0),	( 2, 0),	(-1, 2),	( 2,-1)]} 
        
    def right(self, lockedShape: LockedShape):
        check = super().right(lockedShape)
        if check == True:
            self.anchor[0] += 1
    def left(self, lockedShape: LockedShape):
        check = super().left(lockedShape)
        if check == True:
            self.anchor[0] -= 1
    def fall(self, lockedShape: LockedShape):
        check = super().fall(lockedShape)
        if check == True:
            self.anchor[1] += 1

    def rotateRight(self, lockedShape: LockedShape):    
        if not self.tooFar:
            rotated = []
            anchorX = self.anchor[0]
            anchorY = self.anchor[1]
            rotated = []
            newRotation = self.rotation + 1
            if newRotation == 4:
                newRotation = 0

            if self.rotation == 1 and newRotation == 2:
                    print("break!")
            matrixRightModifier = np.array(([0, 1],
                                           [-1, 0])) 
            # TODO: Consider better rotation method
            
            for i in range(len(self.pieces)):

                self.pieces[i][0] -= anchorX
                self.pieces[i][1] -= anchorY
                rotated = np.matmul(np.array([self.pieces[i][0], self.pieces[i][1]]), matrixRightModifier)
                self.pieces[i] = rotated
                self.pieces[i][0] += anchorX
                self.pieces[i][1] += anchorY

            needToWallKick = (self.doesCollideWithWallOrFloor(self.pieces) or self.doesCollideWithLockedShape(self.pieces, lockedShape))
            # define a boolean indiciating if we did wallkick in order to satisfy rotation
            didWallKick = False
            if needToWallKick:
                kickSet = self.basicWallKick[(self.rotation, newRotation)]
                for kickCheck in range(len(kickSet)):
                    print(kickSet[kickCheck])
                    kickShift = kickSet[kickCheck] # it is a list of two numbers.
                    # make an array that has all the pieces, but with kickShift applied.
                    shiftedPieces = copy.deepcopy(self.pieces)
                    for piece in range(len(self.pieces)):
                        shiftedPieces[piece][0] += kickShift[0]
                        shiftedPieces[piece][1] -= kickShift[1]
                    # now make a check to see if shiftedPieces collides with board or lockedShape
                    if not self.doesCollideWithWallOrFloor(shiftedPieces) and not self.doesCollideWithLockedShape(shiftedPieces, lockedShape):
                        self.pieces = shiftedPieces
                        self.anchor[0] += kickShift[0]
                        self.anchor[1] -= kickShift[1]
                        # flip the boolean to true to indicate we did wall kick succusfully
                        didWallKick = True
                        break
            # check if needToWallKick is true, and if didWallKick is false. If the conditions are satisfied, then rotate back. We were unable to wallkick and do a good rotation.  
            if needToWallKick == True and didWallKick == False: 


                matrixLeftModifier = np.array(([0, -1],
                                               [1, 0])) 
                # break point that only stops the program if the rotation is 1 >> 2
                # if piece is of type T, 

                # TODO: Consider better rotation method
                for i in range(len(self.pieces)):

                    self.pieces[i][0] -= anchorX
                    self.pieces[i][1] -= anchorY
                    rotated = np.matmul(np.array([self.pieces[i][0], self.pieces[i][1]]), matrixLeftModifier)
                    self.pieces[i] = rotated
                    self.pieces[i][0] += anchorX
                    self.pieces[i][1] += anchorY
            else:
                self.rotation = newRotation
            
        
            
    def rotateLeft(self, lockedShape: LockedShape):    
        if not self.tooFar:
            rotated = []
            newRotation = self.rotation - 1
            if newRotation == -1:
                newRotation = 3
            anchorX = self.anchor[0]
            anchorY = self.anchor[1]    
            matrixLeftModifier = np.array(([0, -1],
                                           [1, 0])) 
            # TODO: Consider better rotation method
            for i in range(len(self.pieces)):
                self.pieces[i][0] -= anchorX
                self.pieces[i][1] -= anchorY
                rotated = np.matmul(np.array([self.pieces[i][0], self.pieces[i][1]]), matrixLeftModifier)
                self.pieces[i] = rotated
                self.pieces[i][0] += anchorX
                self.pieces[i][1] += anchorY
            needToWallKick = (self.doesCollideWithWallOrFloor(self.pieces) or self.doesCollideWithLockedShape(self.pieces, lockedShape))
            # define a boolean indiciating if we did wallkick in order to satisfy rotation
            didWallKick = False
            if needToWallKick:
                kickSet = self.basicWallKick[(self.rotation, newRotation)]
                for kickCheck in range(4):
                    print(kickSet[kickCheck])
                    kickShift = kickSet[kickCheck] # it is a list of two numbers.
                    # make an array that has all the pieces, but with kickShift applied.
                    shiftedPieces = copy.deepcopy(self.pieces)
                    for piece in range(len(self.pieces)):
                        shiftedPieces[piece][0] += kickShift[0]
                        shiftedPieces[piece][1] -= kickShift[1]
                    # now make a check to see if shiftedPieces collides with board or lockedShape
                    if not self.doesCollideWithWallOrFloor(shiftedPieces) and not self.doesCollideWithLockedShape(shiftedPieces, lockedShape):
                        self.pieces = shiftedPieces
                        self.anchor[0] += kickShift[0]
                        self.anchor[1] -= kickShift[1]
                        # flip the boolean to true to indicate we did wall kick succusfully
                        didWallKick = True
                        break
            # check if needToWallKick is true, and if didWallKick is false. If the conditions are satisfied, then rotate back. We were unable to wallkick and do a good rotation.        
            if needToWallKick == True and didWallKick == False:
                matrixRightModifier = np.array(([0, 1],
                                               [-1, 0])) 
                # TODO: Consider better rotation method
                for i in range(len(self.pieces)):

                    self.pieces[i][0] -= anchorX
                    self.pieces[i][1] -= anchorY
                    rotated = np.matmul(np.array([self.pieces[i][0], self.pieces[i][1]]), matrixRightModifier)
                    self.pieces[i] = rotated
                    self.pieces[i][0] += anchorX
                    self.pieces[i][1] += anchorY
            else:
                self.rotation = newRotation
    
class JShape(Shape):
    def __init__ (self):
        super().__init__()
        self.color = (29, 44, 219)
        self.pieces = [[3,0],
                       [3,1], [4,1], [5,1]]
        self.tooFar = False
class OShape(Shape):
    def __init__ (self):
        super().__init__()
        self.color = (220, 247, 40)
        self.pieces = [[4,-1], [5, -1],
                       [4, 0], [5, 0],]
        self.tooFar = False
    def rotateRight(self, lockedShape: LockedShape):
        return
    def rotateLeft(self, lockedShape: LockedShape):
        return
    
class SShape(Shape):    
    def __init__ (self):
        super().__init__()
        self.color = (39, 196, 73)
        self.pieces = [[4,-1], [3, 0],
               [4, 0],[5, -1] ,]
        self.tooFar = False
class ZShape(Shape):    
    def __init__ (self):
        super().__init__()
        self.color = (204, 43, 35)
        self.pieces = [[3,-1], [4, 0],
                               [4, -1], [5, 0],]
        self.tooFar = False


# self.pieces = [
#               [4,-1]
#               [4,0] 
#          [3,1][4,1][5,1]
#  
#                [4,0]
#     [2,1][3,1] [4,1]
#                [4,2]
#   [4,1] -> [4,1] <--- anchor point

#   [5,1] -> [4,0] 5 - 1, 1 - 1

#   [4,0] -> [3,1] 4 - 1, 1 + 1

#   [4,-1] -> [2,1] 4 - 2, 1 + 2
#
#   [3,1] -> [4,2] 3 + 1, 1 + 1
#   
#   south -> east x + 1, y - 1
#   direction = [N,E,S,W]
#   if k pressed direction-1

# Translate the anchor point and it's surrounding pieces to the (0, 0) 
# This is done by subtracting the anchor coordinates from all other points

# Apply the rotation transformation
# |cos(t) -sin(t)|
# |sin(t)  cos(t)|

# Translate the anchor point back to its original position
# This is done by addding the anchor coordinates to all other points

#               [4,-1]
#               [4,0] 
#          [3,1][4,1][5,1]

# 1. Translate the anchor point and it's surrounding pieces to the (0, 0) 
# This is done by subtracting the anchor coordinates from all other points

# [4,-1]-[4,1]=[0,-2]
# [4,0]-[4,1]=[0,-1]
# [3,1]-[4,1]=[-1,0]
# [4,1]-[4,1]=[0,0]
# [5,1]-[4,1]=[1,0]

# 2. We apply the rotation transformation to rotate the points around the origin, we can use 90 transformation 
# |cos(t) -sin(t)|
# |sin(t)  cos(t)|
# theta = 90 or (pi/2)

#[-2]

#[0,-2]*# |cos(t) -sin(t)| = [-2, 0]
        # |sin(t)  cos(t)|

# [-2,0]+[4,1]

#import pygame
# Center 5 from left
#class Piece:
#    def __init__ (self, fallSp eed, rotation, color, location):
#        self.fallSpeed = 1
#        self.rotation = 0
#        # self.color = (235, 219, 52)
#        self.location = (5, 0)
##000
##000
##000
#    
#
#
## |_______________________|______\__________________|
#
#virtualGameState = [[0, 0, 0, 0, X, X, X, 0, 0, 0],
#                    [0, 0, 0, 0, 0, X, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                    ]


#if testWallkick == True:
        #    print("Rotating from " + str(self.rotation) + " to " + str(self.rotation + 1))
        #    doesCollide = False
        #    for checks in range(4):
        #        # wallKickTestSet selection is wrong
        #        wallKickTest = self.basicWallKick[self.rotation][checks]
        #        print("Wall kick test set: " + str(self.basicWallKick[self.rotation]))
        #        print("Wall Kick test: " + str(wallKickTest))
        #        
        #        for r in range(len(lockedShape.shapes)):
        #            for k in range (len(lockedShape.shapes[r].pieces)):
        #                for q in range (len(self.pieces)):
        #                    if self.pieces[q][0] + self.basicWallKick[self.rotation][checks][0] == lockedShape.shapes[r].pieces[k][0] and self.pieces[q][1] - self.basicWallKick[self.rotation][checks][1] == lockedShape.shapes[r].pieces[k][1]:
        #                        doesCollide = True
        #        if not doesCollide:
        #            change = [self.basicWallKick[self.rotation][checks][0], self.basicWallKick[self.rotation][checks][1]]
        #            break
        #        else:
        #            doesCollide = False
        #                        
        #    print("decided change: " + str(change))
        #    if not doesCollide:
        #        for shift in range(len(self.pieces)):
        #            self.pieces[shift][0] += change[0]   
        #            self.pieces[shift][1] -= change[1]
            # else:
                # undo rotation
                    
                                  
                    
                                    

                                        
                # for w in range(4):
                    
                    

            # check if valid
            
            # wall kick tests
            # if not valid, translate to new test location defined by one of the the lists in basicwallkick list

            # if none of the translate tests from basicwallkick works, rotateleft, to effectively ignore the user input
            
        
        # we have rotated the pieces
        # check collision
        # if collide!
        # perform procedure to find acceptable place for the rotated piece 
        # translate the piece up?
        # 