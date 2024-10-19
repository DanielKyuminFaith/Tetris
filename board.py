import pygame
import numpy as np
from shape import Shape
from lockedShape import LockedShape

class Board:
    def __init__(self, x, y, width, height, gridWidth, gridHeight):
        self.width = width
        self.height = height
        self.borderThickness = 6
        self.color = (255, 255, 255)
        self.x = x
        self.y = y
        self.gridWidth = gridWidth
        self.gridHeight = gridHeight
        self.gridSquareWidth = width/gridWidth
        self.gridSquareHeight = height/gridHeight

    def draw(self, canvas):
        self.drawBorder(canvas)
        self.drawGrid(canvas)

    def drawPhantom(self,canvas, shape):
        # logic for getting color
        self.drawShape(canvas, shape.phantomShape, shape.color + (128))

    def drawBorder(self, canvas,):
        box_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(canvas, self.color, box_rect, width=self.borderThickness)
        
    def drawGrid(self, canvas):
        for i in range(1, self.gridWidth):
            # VerticalLine = pygame.line()
            pygame.draw.line(canvas, self.color, start_pos = (self.x + self.borderThickness/2 + ((self.width-self.borderThickness)/self.gridWidth)*i, self.y), end_pos = (self.x  + self.borderThickness/2 + ((self.width-self.borderThickness)/self.gridWidth)*i, self.y + self.height - self.borderThickness))
        for i in range (1, self.gridHeight):
            pygame.draw.line(canvas, self.color, start_pos = (self.x, self.y + self.borderThickness/2 + ((self.height-self.borderThickness)/self.gridHeight)*i), end_pos = (self.x + self.width - self.borderThickness, self.y + self.borderThickness/2 + ((self.height-self.borderThickness)/self.gridHeight)*i))

   


    def drawHeldShape(self, canvas, color, pieces):
        xChange = -3 - pieces[2][0]
        for i in range(len(pieces)):
            piece_coord = pieces[i]
            xSquareNum = piece_coord[0] + xChange
            # xSquareNum = -7
            ySquareNum = piece_coord[1]
            xCoord = self.x + self.borderThickness/2 + ((self.width-self.borderThickness)/self.gridWidth)*xSquareNum
            xCoordNext = self.x + self.borderThickness/2 + ((self.width-self.borderThickness)/self.gridWidth)*(xSquareNum+1)
            yCoord = self.y + self.borderThickness/2 + ((self.height-   self.borderThickness)/self.gridHeight)*ySquareNum
            yCoordNext = self.y + self.borderThickness/2 + ((self.height-   self.borderThickness)/self.gridHeight)*(ySquareNum+1)
            width = xCoordNext - xCoord
            height = yCoordNext - yCoord
            
            box_rect = pygame.Rect(xCoord + 1, 
                                   yCoord + 1 + 30, 
                                   width, 
                                   height)
            border_rect = pygame.Rect(xCoord + 1, 
                                   yCoord + 1 + 30, 
                                   width + 1, 
                                   height + 1
                                   )
            pygame.draw.rect(canvas, color, box_rect)   
            pygame.draw.rect(canvas, self.color, border_rect, width=1)   
             


    def drawShape(self, canvas, color, pieces):
        for i in range(len(pieces)):
            piece_coord = pieces[i]
            xSquareNum = piece_coord[0]
            # xSquareNum = -7
            ySquareNum = piece_coord[1]
            xCoord = self.x + self.borderThickness/2 + ((self.width-self.borderThickness)/self.gridWidth)*xSquareNum
            xCoordNext = self.x + self.borderThickness/2 + ((self.width-self.borderThickness)/self.gridWidth)*(xSquareNum+1)
            yCoord = self.y + self.borderThickness/2 + ((self.height-   self.borderThickness)/self.gridHeight)*ySquareNum
            yCoordNext = self.y + self.borderThickness/2 + ((self.height-   self.borderThickness)/self.gridHeight)*(ySquareNum+1)
            width = xCoordNext - xCoord
            height = yCoordNext - yCoord
            box_rect = pygame.Rect(xCoord + 1, 
                                   yCoord + 1, 
                                   width, 
                                   height)
            pygame.draw.rect(canvas, color, box_rect)    
            

    # use drawShape function to draw all the shapes stored inside the lockedShape object. 
    def drawLockedShape(self, canvas, lockedShape : LockedShape):
        shapes = lockedShape.shapes
        for i in range(len(shapes)):
            self.drawShape(canvas, shapes[i].color, shapes[i].pieces)
        return
    
    # queue is a list
    def drawQueue(self, canvas, queue):
        for j in range (len(queue)):
            shape = queue[j]
            color = shape.color
            pieces = shape.pieces
            
            for i in range(len(pieces)):
                piece_coord = pieces[i]
                xSquareNum = piece_coord[0]
                # xSquareNum = -7
                ySquareNum = piece_coord[1]
                xCoord = self.x + self.borderThickness/2 + ((self.width-self.borderThickness)/self.gridWidth)*xSquareNum
                xCoordNext = self.x + self.borderThickness/2 + ((self.width-self.borderThickness)/self.gridWidth)*(xSquareNum+1)
                yCoord = self.y + self.borderThickness/2 + ((self.height-   self.borderThickness)/self.gridHeight)*ySquareNum
                yCoordNext = self.y + self.borderThickness/2 + ((self.height-   self.borderThickness)/self.gridHeight)*(ySquareNum+1)
                width = xCoordNext - xCoord
                height = yCoordNext - yCoord
                if color != (39, 196, 73) and color != (204, 43, 35) and color != (220, 247, 40):
                    box_rect = pygame.Rect(xCoord + 320, 
                                           yCoord + 1 + 60 + j*120, 
                                           width, 
                                           height)
                    border_rect = pygame.Rect(xCoord + 320, 
                                           yCoord + 1 + 60 + j*120, 
                                           width + 1, 
                                           height + 1
                                           )
                elif color == (220, 247, 40):
                    box_rect = pygame.Rect(xCoord + 320, 
                                           yCoord + 1 + 95 + j*120, 
                                           width, 
                                           height)
                    border_rect = pygame.Rect(xCoord + 320, 
                                           yCoord + 1 + 95 + j*120, 
                                           width + 1, 
                                           height + 1)
                else:
                    box_rect = pygame.Rect(xCoord + 320, 
                                           yCoord + 1 + 96 + j*120, 
                                           width, 
                                           height)
                    border_rect = pygame.Rect(xCoord + 320, 
                                           yCoord + 1 + 96 + j*120, 
                                           width + 1, 
                                           height + 1
                                           )
                pygame.draw.rect(canvas, color, box_rect)   
                pygame.draw.rect(canvas, self.color, border_rect, width=1)   
            
        

    
    # shape.pieces 
    # gridsquarewidth
    # gridsquareheight
    # xgridsquare
    # ygridsquare

    #def drawLines(self, canvas):
    #    for verticalLines in range(15):
    #        line = pygame.Rect(self.x+36+(verticalLines*30), self.y, self.width-36-(verticalLines*30), self.height)
    #        pygame.draw.rect(canvas, self.Color, line, width = 1)
    #    for horizontalLines in range(20):
    #        line = pygame.Rect(self.x, self.y+36+(horizontalLines*30), self.width, self.height-36-(horizontalLines*30))
    #        pygame.draw.rect(canvas, self.Color, line, width = 1)    


#virtualGameState = 
#                   [[(x0, y0), (x1, y1), 0, 0, X, X, X, 0, 0, 0],
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




# myArray = np.zeros((3, 4))

        # 0, 0, 0, 0
        # 0, 0, 0, 0
        # 0, 0, 0, 0
        # Algorithm
        # makes a mutli-demensional array of appropriate size for holding the virtual board
        # fills each item in the arraay with coordinates for the top left corner of each grid square



        # virtualBoard.append([])
        # virtualBoard[0].append((coordinate1, cooridinate2))
        
        # Algorithm finishes:

        #
        # Piece = Piece("T")
        # Piece has a location 
        # Piece location is expressed as a coordinate on the virtual board
        # (2, 0)

        # self.virtualBoard  = 
        # [
        # [(0, 0),  (30,  0), (60, 0), (90, 0)]
        # [(0, 30), (30, 30)]
        # []
        # []
        # []
        # []
        # []
        # []
        # []
        # []
        # []
        # []
        # []
        # []
        # []
        # []
        # []
        # []
        # []
        # []
        # ]
        #
        #
        


   # JJJIIIIIIIIII####
   # JJJI########I####
   # ###I########I####
   # ###I########I####
   # ###I########I####
   # ###I########I####
   # ###I########I####
   # ###IIIIIIIIII####