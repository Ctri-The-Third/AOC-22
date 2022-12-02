from day_0 import problem

MAP = {"A":"X","B":"Y","C":"Z"}
OUTCOMES = {"X":0,"Y":1,"Z":2}
ROCK = "X"
PAPER = "Y"
SCISSORS = "Z"
SCORES = {ROCK:1,PAPER:2,SCISSORS:3}
class day_2(problem):
    def __init__(self, logger_name, file_in=None, file_out=None) -> None:
        super().__init__(logger_name, file_in, file_out)
        self.your_score = 0
        self.your_part2_score = 0

    def solve(self):
        for line in self.problem:
            
            self.play_round(line[2],MAP[line[0]])
            self.play_round_strategically(MAP[line[0]],OUTCOMES[line[2]])
        self.solution = f"{self.your_score},{self.your_part2_score}"
        return super().solve()


    def play_round(self,yours,theirs) -> int:
        out = outcome(yours,theirs) 
        
        self.your_score += out * 3
        self.your_score += SCORES[yours]


    def play_round_strategically(self,theirs,desired_outcome):
        yours = strategic_choice(theirs,desired_outcome)
        self.your_part2_score += outcome(yours,theirs) * 3 
        self.your_part2_score += SCORES[yours]

            
def strategic_choice(theirs,desired_outcome):
    if desired_outcome == 1:
        return theirs
    elif theirs == ROCK and desired_outcome == 2:
        return PAPER
    elif theirs == ROCK and desired_outcome == 0:
        return SCISSORS
    elif theirs == PAPER and desired_outcome == 2:
        return SCISSORS
    elif theirs == PAPER and desired_outcome == 0:
        return ROCK
    elif theirs == SCISSORS and desired_outcome == 2:
        return ROCK 
    elif theirs == SCISSORS and desired_outcome == 0:
        return PAPER

def outcome(yours,theirs):
    "does yours beat theirs? 2 if yes, 0 if lost, 1 on tie"
    if theirs == yours:
        return 1 
    elif theirs == ROCK and yours == PAPER:
        return 2 
    elif theirs == ROCK and yours == SCISSORS:
        return 0 
    elif theirs == PAPER and yours == SCISSORS:
        return 2
    elif theirs == PAPER and yours == ROCK:
        return 0 
    elif theirs == SCISSORS and yours == ROCK:
        return 2 
    elif theirs == SCISSORS and yours == PAPER:
        return 0 

if __name__ == "__main__":
    day = day_2("day_2","problems\day2_input.txt")
    
    print(day.solve())



