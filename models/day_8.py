from models.day_0 import problem

 
class Day_8(problem):
    def __init__(self,  file_in=None, file_out=None) -> None:
        super().__init__("day_8", file_in, file_out)
        self.grid = []    
        self.parse_input()
        

        self.width = len(self.problem[0])
        self.height = len(self.problem)
        self.check_trees()

    def parse_input(self):
        y = 0 
        for line in self.problem:
            tree_line = [] 
            x = 0 
            self.grid.append(tree_line)
            
            for tree in line:
                tree_line.append(Tree(tree,x,y))
                x += 1 
            y += 1  

    def check_trees(self):
#        print("")
        for i in range(0,self.width):
            self.check_row(i,1)
            self.check_row(i,-1)
            self.check_column(i,1)
            self.check_column(i,-1)

        for line in self.grid:
            for tree in line:
                tree:Tree
                self.find_visible_trees(tree)

    def print_out(self):
        print("")
        mid_strs = []
        right_strs = [] 

        
        for line in self.grid:
            mid_str = right_str = ""
            for tree in line:
                mid_str += "X" if tree.visible else "-"
                right_str += f"{tree.visible_trees}"
            mid_strs.append(mid_str)
            right_strs.append(right_str)
        
        for i in range(self.height):
            print(f"{self.problem[i]}    {mid_strs[i]}    {right_strs[i]}")
        print ("------------------------")

    def check_row(self, row_index:int, direction:int):
        row = self.grid[row_index]
        self.check_line(direction, row)

    def check_column(self, column_index:int, direction):
        col = [] 
        for line in self.grid:
            col.append(line[column_index])
        self.check_line(direction, col)
        pass 

    def check_line(self,  direction:int, row):
        #visibility should NOT be the default? need brain think.  🤔
        if direction < -1 or direction > 1:
            raise ValueError
        if direction == -1:
            start = len(row) -1 
            stop = -1
        elif direction == 1:
            start = 0 
            stop = len(row)

        highest_tree = -1 
        for i in range(start,stop,direction):
            tree = row[i]
            tree:Tree
            if tree.height > highest_tree:
                tree.visible = True
            highest_tree = max(highest_tree,tree.height)

    def solve(self):
        p1 = 0 
        p2 = 0 
        for trees in self.grid:
            for tree in trees:
                tree:Tree
                if tree.visible:
                    p1 += 1 
                    p2 = max(p2,tree.visible_trees)
        self.solution = f"{p1},{p2}"
        return super().solve()
        
    def find_visible_trees(self,tree):
        tree:Tree

    
        left_start = tree.x -1 
        right_start = tree.x + 1 
        top_start = tree.y -1 
        bottom_start = tree.y + 1

        #look_left
        visible_trees = 0 


        if left_start >= 0:  #gotta be at least 1,2,3,4 - actually it can be 0
            max_height = -1

            for x in range(left_start,-1,-1):
                compare_tree = self.grid[x][tree.y]
                compare_tree:Tree
                if compare_tree.height > max_height:
                    visible_trees += 1 
                    max_height = compare_tree.height

        if right_start <= self.width -1:  # 0,1,2,3,4
            max_height = -1
            for x in range(right_start,self.width,1):
                compare_tree = self.grid[x][tree.y]
                compare_tree:Tree
                if compare_tree.height > max_height:
                    visible_trees += 1 
                    max_height = compare_tree.height

        if top_start >= 0:
            max_height = -1
            for y in range(top_start,-1,-1):
                compare_tree = self.grid[tree.x][y]
                compare_tree:Tree
                if compare_tree.height > max_height:
                    visible_trees += 1 
                    max_height = compare_tree.height

        if bottom_start <= self.height - 1:
            max_height = -1
            for y in range(bottom_start,self.height,1):
                compare_tree = self.grid[tree.x][y]
                compare_tree:Tree
                if compare_tree.height > max_height:
                    visible_trees += 1 
                    max_height = compare_tree.height 
        tree.visible_trees = visible_trees

    #we could loop through each tree 
    


class Tree():
    "visibles are NSEW"
    def __init__(self,height:str,x,y) -> None:
        
        self.height = int(height)
        self.x = x
        self.y = y 
        self.visible = False
        self.visible_trees = 0
        pass
