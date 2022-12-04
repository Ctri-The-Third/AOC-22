from models.day_0 import problem


class Day_1(problem):
    def __init__(self, file_in=None, file_out=None) -> None:
        super().__init__("day_1", file_in, file_out)
        self.max_cal = 0 
        self.sec_max = 0
        self.third_max = 0
        


    def solve(self):
        self.max_cal = 0 
        self.sec_max = 0
        self.third_max = 0
        cur_cal = 0 
        for line in self.problem:
            if line == "":
                self.update_cals(cur_cal)
                cur_cal = 0 
            else:
                num = int(line)
                cur_cal += num
        self.update_cals(cur_cal)
        top_three = self.max_cal+self.sec_max+self.third_max
        self.solution = f"{self.max_cal},{top_three}"
        return super().solve()

    def update_cals(self, cal:int):
        if cal > self.max_cal:
            self.third_max = self.sec_max
            self.sec_max = self.max_cal
            self.max_cal = cal
        elif cal > self.sec_max:
            self.third_max = self.sec_max
            self.sec_max = cal
        elif cal > self.third_max:
            self.third_max = cal

if __name__ == "__main__":
    day = Day_1(r"problems\day1_input.txt")
    print(day.solve())