
class LockedShape:
    def __init__(self):
        self.shapes = [
        ]
        

    def addShape(self, shape,):
        self.shapes.append(shape)

    def clearLines(self):
        rows = 0
        rowCount = dict(sorted(self.placed().items()))
        for key, value in rowCount.items():
            if value == 10:
                rows += 1
                self.clearLine(key)
                self.shiftLines(key)
        return rows

            
        #my_dict = {'a': 1, 'b': 2, 'c': 3}
        #for key, value in my_dict.items():
        #    print(key, value)
        # a 1
        # b 2
        # c 3
        ## goes throuhg all rows to clear
        #clearLine(#line to clear)

    def placed(self):
        rowCount = {}
        for i in range(len(self.shapes)):
            for p in range(len(self.shapes[i].pieces)):
                row = self.shapes[i].pieces[p][1]
                if row in rowCount:   
                    rowCount[row] = rowCount[row] + 1
                else:
                    rowCount[row] = 1
        return rowCount

    def clearLine(self, rowToDelete):
        rows = 0
        # get original number of pieces in play
        for shape in self.shapes:
            shape.pieces = [piece for piece in shape.pieces if piece[1] != rowToDelete]
        self.shapes = [shape for shape in self.shapes if not len(shape.pieces) == 0]
        # find how many shapes have been removed, 10 = 1 layer, 20 = 2 layers, etc
        # grant certain number of points and reset rows

        

    def shiftLines(self, deletedRow):
        for shape in self.shapes:
            #shape.pieces = [[piece[0], piece[1] + 1] for piece in shape.pieces if piece[1] < deletedRow]
            shape.pieces = [[piece[0], piece[1] + 1] if piece[1] < deletedRow else piece for piece in shape.pieces]
        
        





        #for i in range(len(self.shapes)):
        #    for p in range(len(self.shapes[i].pieces)):
        #        targetRow = self.shapes[i].pieces[p][1]
        #        if targetRow == rowToDelete:
        #            self.shapes[i].pieces.remove(self.shapes[i].pieces[p])
        #            if len(self.shapes[i].pieces) == 0:
        #                self.shapes.remove(self.shapes[i])

    #myList = [1, 2, 3, 4, 5]
    ## [2, 3, 4, 5]
    ## [2, 4, 5]
    ## [2, 4]
    ## index out of range
    #for i in range(len(myList)):
    #    myList.(i)



                
        
                    
                
            
    

    

    # lockedShape
    # shapes
    # pices
    # rowCountList = 
    #{ 20: 10, 
    #  19: 10,
    # }
    # our alg:
    # go through pieces count the number of pieces in each row
    # iterate through the pieces in lockedShape
    # create a list *
    # for loop for the shapes
        # for loop for the pices
            # this will involve querying dictionary for the count a given
                # if key in dict 
            # if it's not in the dicitonary, then add a new entry
            # if it is in the dictionary, then increment the entry
            # look at the row of the piece, and increment it in the dictionary
    
    # go through the row count list
    
    # if a given entry in the row count list has a value of 10
    #   define value for the row we are removing
    #   delete pieces from locked shape -> *
    #       for loop through the shapes in lockedshape       
    #           for loop through the pieces in the shape
    #               remove pieces that are equal to the row we are removing
    #   move pieces down*
    #       for loop through the shapes in lockedshape
    #           for loop throught he pieces in the shape
    #               if the piece is greater than the row we removed,
    #                   then move the piece down by 1, by sub/adding w/e to the y value
    