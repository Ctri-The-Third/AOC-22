from models.day_0 import problem
import re

 
class Day_7(problem):
    def __init__(self,  file_in=None, file_out=None) -> None:
        super().__init__("day_7", file_in, file_out)
        
        self.cd_re = re.compile(r"\$ cd (.*)")
        self.ls_re = re.compile(r"\$ ls")
        self.dir_re = re.compile(r"dir ([a-zA-Z]*)")
        self.file_re = re.compile(r"([0-9]+) ([a-zA-Z\.]+)")
    
        self.directories = Folder("/",None)
        self.cwd = None     
        self.p1_matching_directories = [] 
        self.pre_process_problem()
    
    
    def pre_process_problem(self):    
        for stdinout in self.problem:
            if stdinout[0] == "$":
                self.do_command(stdinout)
            else:
                self.read_output(stdinout)
        pass 

        self.directories.measure_folder()


    def do_command(self, command):
        command_match = self.cd_re.findall(command)
        self.cwd:Folder
        if command_match:
            if command_match[0] == "/":
                self.cwd = self.directories
            elif command_match[0] == "..":
                self.cwd = self.cwd.parent
            elif command_match[0] not in self.cwd:
                #add folder to CWD
                new_folder = Folder(command_match[0], self.cwd)
                self.cwd = new_folder
        pass 


        

    def read_output(self, terminal_string):
        file_info = self.file_re.findall(terminal_string)
        #ignore directories
        if file_info:
            self.cwd[file_info[0][1]] = int(file_info[0][0])
        



    def solve(self):
        self.assess(self.directories, self.p1_matching_directories, max_size= 100000) 
        
        
        p2_matching_directories = []

        root_folder = self.directories
        root_folder:Folder
        p2_target_folder_size = 30000000 - (70000000 - root_folder.total_size)
        self.assess(self.directories, p2_matching_directories, min_size=  p2_target_folder_size   ) 

        tar_dir_size = max(p2_matching_directories)
        for item in p2_matching_directories:
            
            tar_dir_size = min(item,tar_dir_size)
        self.solution = f"{sum(self.p1_matching_directories)},{tar_dir_size}"
        return super().solve()

    def assess(self,folder,  target_list:list, max_size = None, min_size = None) -> list:
        folder: Folder
        if max_size and  folder.total_size <= max_size:
            target_list.append(folder.total_size)
        elif min_size is not None and folder.total_size >= min_size:
            target_list.append(folder.total_size)
        for key, item in folder.items():
            if isinstance(item,Folder):
                self.assess(item,  target_list, max_size=max_size, min_size=min_size)
        #

class Folder(dict):
    "parent is the parent folder class."
    def __init__(self,name:str,parent) -> None:
        super().__init__()
        self.parent = parent
        self.name = name
        self.total_size = 0 
        if parent is not None: 
            parent[self.name] = self

    def get_full_path(self) -> str:
        out_str = f"{self.name}"
        if self.parent is not None:
            self.parent:Folder
            out_str = f"{self.parent.get_full_path()}\{self.name}"

    def measure_folder(self) -> int:
        self:dict
        output = 0 
        for key, val in self.items():
            (f"reading a content item {key}:{val}")
            if isinstance(val,Folder):
                output += val.measure_folder()
            else :
                output +=(val)
        self.total_size = output
        return output
