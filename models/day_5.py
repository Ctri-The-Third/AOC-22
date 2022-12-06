
import re 
from models.day_0 import problem

class Day_5(problem):
    def __init__(self, file_in=None, file_out=None) -> None:
        super().__init__("day_5", file_in, file_out)
        self.stack_instructions = [] # e.g. "[Z] [M] [P]" or "[D]        "
        self.stack_definition_line = "" #e.g.`  1   2   3 ` 
        self.stacks = [] #list of X stacks
        self.instructions = [] # e.g. move 1 from 2 to 1

        self.preprocess_instructions()
        self.solve()
    def preprocess_instructions(self):
        stack_instruction_re = re.compile(r" *\[[A-Z]\] *")
        instructions_re = re.compile(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)")
        stack_definition_line_re = re.compile(r"( ([0-9])  ?)")
        loading_stacks = True
        for line in self.problem:

            if loading_stacks and stack_instruction_re.match(line):
                self.stack_instructions.append(line)
            elif not loading_stacks and instructions_re.match(line):
                self.instructions.append(line)
            elif stack_definition_line_re.match(line):
                found = stack_definition_line_re.findall(line)
                #define the number of stacks based on the count of matches
                for _ in found:
                    self.stacks.append(Stack())
                loading_stacks = False
         
        boxes_split_re = re.compile(r".{3,4}")
        get_label_re = re.compile(r"\[([A-Z]+)\]")
        
        for stack_instruction in self.stack_instructions:
            labels = boxes_split_re.findall(stack_instruction)
             
            for pos in enumerate(labels):
                label_text = pos[1]
                stack_index = pos[0]
                label_matches = get_label_re.findall(label_text)
                if label_matches:
                    stack = self.stacks[stack_index]
                    stack:Stack
                    box = Box(label_matches[0])
                    stack.add_box(box)


    
    def solve(self):
        for stack in self.stacks:
            stack:Stack
            print("stack --")
            for box in stack.boxes:
                print(f"|_[{box.label}]")

        return super().solve()






class Box():
    def __init__(self,letter:str) -> None:
        self.label = letter
    def __str__(self) -> str:
        return f"{self.label}"
    

class Stack():
    def __init__(self) -> None:
        self.boxes = []

    def add_box(self, box:Box):
        self.boxes.append(box)
        return None 

    def lift_one_box(self, count=1) -> Box:
        box = self.boxes[0]
        self.boxes.pop(0)
        return box

    
