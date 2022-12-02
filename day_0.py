import sys
import logging

class problem():
    """A problem for the advent of code. Takes a file in, and an option file name.
    See `.problem` and `.solution` for the problem and solution, and `.solve()` to do the thing."""
    def __init__(self, logger_name, file_in=None, file_out=None, ) -> None:
        self.logger = logging.getLogger(logger_name)
        self._logger = logging.getLogger("day 0")
        self._file_out = file_out
        if file_in is None:
            try:
                file_in = sys.argv[0] 
            except (IndexError, KeyError) as err:
                self._logger.warning("Couldn't get filepath from passed args. Failure likely. %s",err) 
        
        self.problem = self._load_file(file_in)
        self.solution = ""

    def solve(self):
        if self._file_out is not None:
            with open(self._file_out,"w+",encoding="utf-8") as file:
                file.write(self.solution)
        
        return self.solution 


    def _load_file(self, file_path):
        with open(file_path,"r",encoding="utf-8")  as file:
            return file.readlines()


