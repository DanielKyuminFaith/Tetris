import pygame, time
from board import Board
from shape import Shape, TShape, LShape, IShape, JShape, OShape, SShape, ZShape
from lockedShape import LockedShape
import random
from shapeFactory import ShapeFactory
# inclusive
# random.randint(0, 9)';';';



def getNewShapeOfSameType(shape):
    newShape = None
    if isinstance(shape, IShape):
        newShape = IShape()
    elif isinstance(shape, JShape):
        newShape = JShape()
    elif isinstance(shape, TShape):
        newShape = TShape()
    elif isinstance(shape, LShape):
        newShape = LShape()
    elif isinstance(shape, ZShape):
        newShape = ZShape()
    elif isinstance(shape, OShape):
        newShape = OShape()
    elif isinstance(shape, SShape):
        newShape = SShape()
    return newShape


def main():
    
    pygame.init()
    displayWidth = 800 #600
    displayHeight = 800 #800
    pygame.display.set_caption("Tetris")
    canvas = pygame.Surface((displayWidth, displayHeight))
    window = pygame.display.set_mode((displayWidth, displayHeight))
    Running = True
    dt = 0 
    clock = pygame.time.Clock()
    prev_time = time.time()
    elapsedTime = 0
    targetFPS = 12
    lastFall = 0
    fallSpeed = 1
    aKeyHeldTime = 0
    dKeyHeldTime = 0
    sKeyHeldTime = 0
    repeatDelay = 0.8
    holdUsed = False
    heldShape = None
    temp = None
    level = 1
    score = 0
    font = pygame.font.SysFont("Comic Sans", 30)
    shapeFactory = ShapeFactory()
    

    # initialize game pieces
    # board = Board(x = 100, y = 25, width = 380, height = 750, gridWidth = 10, gridHeight = 20)
    board = Board(x = 200, y = 25, width = 380, height = 750, gridWidth = 10, gridHeight = 20)
    shape = shapeFactory.randomizer()
    q = [shapeFactory.randomizer(), shapeFactory.randomizer(), shapeFactory.randomizer()]
    
    

    # q.qsize()
    # q.put(1) # puts new item on the queue
    # q.put(2)
    # 
    # q.get() # returns and removes item from queue
    # q.get()
    lockedShape = LockedShape()

    A_KeyPressed = False
    D_KeyPressed = False
    S_KeyPressed = False
    
    heldLongEnough = False

    finalScoreVariable = None
    finalScore = 0

    while Running == True:
        clock.tick(targetFPS)
        now = time.time()
        dt = now - prev_time
        elapsedTime = elapsedTime + dt
        prev_time = now
        
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Running = False
                if event.key == pygame.K_SPACE:
                    if holdUsed == False:
                        holdUsed = True
                        if heldShape == None:
                            heldShape = getNewShapeOfSameType(shape)
                            shape = shapeFactory.randomizer()
                        else:
                            temp = getNewShapeOfSameType(heldShape)
                            heldShape = getNewShapeOfSameType(shape)
                            shape = temp
                if event.key == pygame.K_w:
                    score += shape.hardDrop(lockedShape)*2
                
                if event.key == pygame.K_a: 
                    A_KeyPressed = True
                    if D_KeyPressed == False:
                        shape.left(lockedShape)
                        aKeyHeldTime = elapsedTime
                if event.key == pygame.K_d:
                    D_KeyPressed = True
                    if A_KeyPressed == False:
                        shape.right(lockedShape) 
                        dKeyHeldTime = elapsedTime
                if event.key == pygame.K_s:
                        S_KeyPressed = True
                        shape.fall(lockedShape)
                        sKeyHeldTime = elapsedTime
                
                        
                if event.key == pygame.K_k:
                    shape.rotateLeft(lockedShape)
                    
                if event.key == pygame.K_l:
                    shape.rotateRight(lockedShape)
                    # if variabe is less than or 3, then do +=1 one, if it is 3, set to 0 ';A                    
                    
                    
                    # if event.key == pygame.K_k:
                        # shape.rotateLeft(lockedShape)
                    

                        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a: 
                    # shape.left()
                    A_KeyPressed = False     
                    heldLongEnough = False
                if event.key == pygame.K_d:
                    D_KeyPressed = False
                    heldLongEnough = False
                if event.key == pygame.K_s:
                    S_KeyPressed = False
                    heldLongEnough = False
        if aKeyHeldTime + repeatDelay <= elapsedTime:
            if D_KeyPressed == False:
                heldLongEnough = True
        if dKeyHeldTime + repeatDelay <= elapsedTime:
            if A_KeyPressed == False:
                heldLongEnough = True
        if sKeyHeldTime + repeatDelay <= elapsedTime:
            if A_KeyPressed == False:
                if D_KeyPressed == False:
                    heldLongEnough = True

        if A_KeyPressed == True and heldLongEnough:
            if D_KeyPressed == False:
                if aKeyHeldTime + repeatDelay/8  <= elapsedTime:
                    aKeyHeldTime = elapsedTime
                    shape.left(lockedShape)    
        if D_KeyPressed == True and heldLongEnough:
            if A_KeyPressed == False:
                if dKeyHeldTime + repeatDelay/8  <= elapsedTime:
                    dKeyHeldTime = elapsedTime  
                    shape.right(lockedShape)    
        if S_KeyPressed == True and heldLongEnough:
            if A_KeyPressed == False:
                if D_KeyPressed == False:
                    if sKeyHeldTime + repeatDelay/12  <= elapsedTime:
                        sKeyHeldTime = elapsedTime  
                        lastFall = elapsedTime
                        shape.fall(lockedShape)   
                        score += 1
        
        canvas.fill((0, 0, 0))
        board.drawShape(canvas,  shape.color, shape.pieces)
        
        if heldShape != None:
            board.drawHeldShape(canvas,  heldShape.color, heldShape.pieces)
            
        # board.drawPhantom(canvas, shape)

        if shape.tooFar == True:
            for piece in shape.pieces:
                if piece[1] < 1:
                    # Code for "Game Over" Screen
                    finalScoreVariable = score
                    finalScore = font.render("Final Score: " + str(finalScoreVariable), True, (255, 255, 255))
                    gameOver = font.render("GAME OVER", True, (255, 0, 0))

                    # Running = False


            lockedShape.shapes.append(shape)
            rowsCleared = lockedShape.clearLines()
            if not rowsCleared == 0:
                if rowsCleared == 1:
                    score += 100 * level
                elif rowsCleared == 2:
                    score += 300 * level
                elif rowsCleared == 3:
                    score += 500 * level
                elif rowsCleared == 4:
                    score += 800 * level
                

            if finalScoreVariable == None:
                
                shape = q.pop(0)
                q.append(shapeFactory.randomizer())
                holdUsed = False
            
        board.drawQueue(canvas, q)

        board.drawLockedShape(canvas, lockedShape)
        board.draw(canvas)
        if lastFall + fallSpeed <= elapsedTime:

            shape.fall(lockedShape)
        
            lastFall = elapsedTime
        
        scoreText = font.render("Score: " + str(score), False, (255, 255, 255))
        if finalScoreVariable == None:
            canvas.blit(scoreText, (0, 300))
        
        
        
        if finalScoreVariable != None:
            shape.tooFar = False
            canvas.blit(finalScore, (2, 300))
            canvas.blit(gameOver, (2, 330))
            
        window.blit(canvas, (0,0))
        pygame.display.update()
        

if __name__ == '__main__':
    main()
