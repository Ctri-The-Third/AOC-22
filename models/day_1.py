from models.day_0 import problem


class Day_1(problem):
    def __init__(self, file_in=None, file_out=None) -> None:
        super().__init__("day_1", file_in, file_out)
        self.list_of_totals = []
        


    def solve(self):
        cur_cal = 0 
        for line in self.problem:
            if line == "":
                self.list_of_totals.append(cur_cal)
                cur_cal = 0 
            else:
                num = int(line)
                cur_cal += num
        self.list_of_totals.append(cur_cal)
        
        self.list_of_totals.sort(reverse=True)
        highest = self.list_of_totals[0]
        top_three = sum(self.list_of_totals[0:3])
        self.solution = f"{highest},{top_three}"
        return super().solve()



if __name__ == "__main__":
    day = Day_1()
    print(day.solve())