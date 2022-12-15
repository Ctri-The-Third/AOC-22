from models.day_0 import problem





class Day_6(problem):
    def __init__(self, file_in=None, file_out=None) -> None:
        super().__init__("day_6", file_in, file_out)

    
    
    def solve(self):
        p1 = p2 = 0
        line = self.problem.pop()
        for i in range(4,len(line),1):

            maybe_p1 = check_for_uniques(line,i,4)
            if maybe_p1 and p1 == 0 :
                p1 = maybe_p1
            
            maybe_p2 = check_for_uniques(line,i,14)
            if maybe_p2 and p2 == 0:
                p2 = maybe_p2

        self.solution = f"{p1},{p2}"
        return super().solve()

def check_for_uniques(str, index, length):
    if index-length < 0:
        return 
    letters = str[index-length:index]
    unique_letters = set(letters)
    if len(unique_letters) == length:
        return index 
    return 