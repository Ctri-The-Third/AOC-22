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
        for pair in self.section_pairs:
            if pair[0]["min"] >= pair[1]["min"] and pair[0]["max"] <= pair[1]["max"]:
                total_overlap += 1
            elif pair[1]["min"] >= pair[0]["min"] and pair[1]["max"] <= pair[0]["max"]:
                total_overlap += 1
            #partial overlaps go here 

        self.solution = f"{total_overlap},"
        return super().solve()



if __name__ == "__main__":
    day = Day_4(r"problems/day4_input.txt")
    print(day.solve())