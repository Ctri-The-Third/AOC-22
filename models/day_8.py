from models.day_0 import problem

 
class Day_8(problem):
    def __init__(self,  file_in=None, file_out=None) -> None:
        super().__init__("day_8", file_in, file_out)
        self.grid = []    
        self.parse_input()
        

        self.width = len(self.problem[0])
        self.height = len(self.problem)
        

    def parse_input(self):
        for line in self.problem:
            tree_line = [] 
            self.grid.append(tree_line)
            
            for tree in line:
                tree_line.append(Tree(tree))
                #self.grid[0][4] will be 

    def check_direction(self, column:int = None, row:int = None, col_dir:int = 0, row_dir:int = 0 ):   
        "selects either a column or a row, and then either looks upward (col_dir -1) or downward (1) or l to r (row_dir = 1) or r to l (-1)"
        if (not column and not row) or (column and row):
            self.logger.error("Please set either column or row.")
            raise ValueError
                
        x_range = range(0,self.width) if row is not None else column
        y_range = range(0,self.width) if column is not None else row


    def check_row(self, row_index:int, direction:int):
        #visibility should NOT be the default? need brain think.  🤔
        row = self.grid[row_index]
        if direction < -1 or direction > 1:
            raise ValueError
        if direction == -1:
            start = len(row)
            stop = 0 
        elif direction == 1:
            start = 0 
            stop = len(row)

        highest_tree = 0 
        for i in range(start,stop,direction):
            tree = row[i]
            tree:Tree
            if tree.height <= highest_tree:
                tree.visible = False
            highest_tree = max(highest_tree,tree.height)
            

    #we could loop through each tree 
    


class Tree():
    "visibles are NSEW"
    def __init__(self,height:str) -> None:
        
        self.height = int(height)
        self.visible = True
        pass
