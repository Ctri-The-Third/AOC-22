from models.day_0 import problem


class Day_4(problem):
    def __init__(self,  file_in=None, file_out=None) -> None:
        super().__init__("day_4", file_in, file_out)
        
        self.pre_process()

    def pre_process(self):
        self.section_pairs = []
        for line in self.problem:
            line:str
            sections = line.split(",")

            fs = sections[0].split("-")
            first_section = {"min":int(fs[0]), "max":int(fs[1])}
            fs = sections[1].split("-")
            second_section = {"min":int(fs[0]), "max":int(fs[1])}
            self.section_pairs.append([first_section,second_section])

    def solve(self):
        total_overlap = 0 
        partial_overlap = 0 
        for pair in self.section_pairs:

            pair_1 = set(range(pair[0]["min"],pair[0]["max"]+1,1))
            pair_2 = set(range(pair[1]["min"],pair[1]["max"]+1,1))
            inter = pair_1.intersection(pair_2) if len (pair_1) >= len(pair_2) else pair_2.intersection(pair_1)


            if len(inter) == len(pair_1) or len(inter) == len(pair_2):
                total_overlap += 1
            elif len(inter)> 0:
                partial_overlap += 1
        self.solution = f"{total_overlap},{total_overlap+partial_overlap}"
        return super().solve()

#01234567890
#..234......
#......678..

if __name__ == "__main__":
    day = Day_4(r"problems/day4_input.txt")
    print(day.solve())