
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
    def preprocess_instructions(self):
        "parse the file appropriately, sets up a variable number of stacks"
        stack_instruction_re = re.compile(r" *\[[A-Z]\] *")
        instructions_re = re.compile(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)")
        stack_definition_line_re = re.compile(r"( ([0-9])  ?)")
        loading_stacks = True
        self.stacks = []
        self.stack_instructions = [] 
        self.instructions = [] 
                
        for line in self.problem:

            if loading_stacks and stack_instruction_re.match(line):
                self.stack_instructions.append(line)
            elif not loading_stacks and instructions_re.match(line):
                self.instructions.append(line)
            elif stack_definition_line_re.match(line):
                found = stack_definition_line_re.findall(line)
                #define the number of stacks based on the count of matches
                for _ in found:
                    self.stacks.append(list())
                loading_stacks = False
         
        boxes_split_re = re.compile(r".{3,4}")
        get_label_re = re.compile(r"\[([A-Z]+)\]")
        
        self.stack_instructions.reverse()
        for stack_instruction in self.stack_instructions:
            labels = boxes_split_re.findall(stack_instruction)
             
            for pos in enumerate(labels):
                label_text = pos[1]
                stack_index = pos[0]
                label_matches = get_label_re.findall(label_text)
                if label_matches:
                    stack = self.stacks[stack_index]
                    stack:list
                    box = label_matches[0]
                    stack.append(box)

    
    def solve(self):
        p1 = self.real_solve()
        self.preprocess_instructions()
        
        p2 = self.real_solve(False)
        self.solution = f"{p1},{p2}"
        return super().solve()

    def real_solve(self, one_at_a_time = True):
        instr_splitter = re.compile("move ([0-9]+) from ([0-9]+) to ([0-9]+)")
        self._print_out("initial state")
        for instruction in self.instructions:
            pieces = instr_splitter.findall(instruction)
            qty = int(pieces[0][0])
            src = int(pieces[0][1])-1
            dst = int(pieces[0][2])-1

            crane_contents = [] 
            for _ in range(qty):
                moved_box = self.stacks[src].pop()
                crane_contents.append(moved_box)
            
            if not one_at_a_time:
                crane_contents.reverse()
            for box in crane_contents:
                self.stacks[dst].append(box)
            self._print_out(instruction)

        out = ""        
        for stack in self.stacks:
            out += stack.pop()
        
        return out



    def _print_out(self, instruction):
            "debug method, outputs the crates in the format described in the problem"
            return 
            print(instruction)
            
            max_len = 0 
            for stack in self.stacks:
                max_len = max(len(stack), max_len)
            for _ in range(max_len,-1,-1):
                out_str = ""
                for stack in self.stacks:
                    try: 
                        out_str += stack[_]
                    except IndexError:
                        out_str += " "
                print(out_str)    
            print("123456789")   
    