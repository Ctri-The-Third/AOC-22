import sys
import logging
from logging import StreamHandler
from sys import stdout

class problem():
    """A problem for the advent of code. Takes a file in, and an option file name.
    See `.problem` and `.solution` for the problem and solution, and `.solve()` to do the thing."""
    def __init__(self, logger_name, file_in=None, file_out=None, ) -> None:
        #set up debug messaging (overkill)
        self.logger = logging.getLogger(logger_name)
        self._logger = logging.getLogger("day 0")
        format = "%(asctime)s:%(levelname)s:%(name)s  %(message)s"
        logging.basicConfig(handlers=[StreamHandler(stdout)], level=logging.WARNING, format=format)

        self._file_out = file_out

        # if an input file isn't supplied by the invocation, it will be supplied as an argument
        if file_in is None:
            try:
                file_in = sys.argv[1] 
            except (IndexError, KeyError) as err:
                self._logger.warning("Couldn't get filepath from passed args. Failure likely. %s",err) 
        
        #actually load the file
        self.problem = self._load_file(file_in)
        self._logger.debug("file load completed, %s lines loaded", len(self.problem) if self.problem is not None else "Null")
        #all days have a solution 
        self.solution = ""

    def solve(self):
        if self._file_out is not None:
            with open(self._file_out,"w+",encoding="utf-8") as file:
                file.write(self.solution)
        
        return self.solution 


    def _load_file(self, file_path) -> list :
        #stops the method crashing if None is passed in, or something weird like an int
        self._logger.debug("Attempting to load file %s", file_path)
        if not file_path or not isinstance(file_path,str):
            self._logger.error("Can't load problem filepath %s because it's not a string", file_path)

        #catch any errors
        try:
            #open the path
            with open(file_path,"r",encoding="utf-8")  as file:
                #read().splitlines() gets rid of the annoying '\n' that .readlines() includes.
                self._logger.debug("Successfully opened file, attempting to read and return")
                return file.read().splitlines()
        except FileNotFoundError:
            self._logger.error("File [%s] not found",file_path)

        return [] 




