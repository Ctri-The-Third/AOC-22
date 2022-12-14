import sys 
import pytest
import logging
#weird thing to support vscode's built in handling of pytest
sys.path.append("")

from models.day_0 import problem



def test_load_file():
    logging.basicConfig(level=logging.DEBUG)

    prb = problem("test_problem","problems/day1_sample.txt")
    assert len(prb.problem) > 0


def test_day_1():
    from models.day_1 import Day_1
    d1 = Day_1(r"problems/day1_sample.txt")
    d1:problem 
    assert d1.solve() == "24000,45000"


def test_day_2():
    from models.day_2 import Day_2
    day = Day_2(r"problems/day2_sample.txt")
    day:problem 
    assert day.solve() == "15,12"

def test_day_3():
    from models.day_3 import Day_3
    day = Day_3(r"problems/day3_sample.txt")
    day:problem 
    assert day.solve() == "157,70"


def test_day_3_functions():
    import models.day_3 as d3
    assert d3.convert_char_to_int("b") == 2
    assert d3.convert_char_to_int("B") == 28
    assert d3.convert_char_to_int(0) == -1 
    assert d3.convert_char_to_int([]) == -1 

    assert d3.find_match("abc","cde") == "c"
    assert d3.find_badge(["aaaaaaabcABC","ccccccdeCD","eeffcEE"]) == "c"
    

def test_day_4():
    from models.day_4 import Day_4
    day = Day_4(r"problems/day4_sample.txt")
    day:problem
    assert day.solve() == "2,4"
    


def test_day_5():
    from models.day_5 import Day_5
    day = Day_5(r"problems/day5_sample.txt")
    day:problem
    assert day.solve() == "CMZ,MCD"


def test_day_6():
    from models.day_6 import Day_6
    day = Day_6(r"problems/day6_sample.txt")
    day:problem
    
    assert day.solve() == "11,26"
    assert day.solve() == "10,29"
    assert day.solve() == "6,23"
    assert day.solve() == "5,23"
    assert day.solve() == "7,19"


def test_day_7():
    from models.day_7 import Day_7
    day = Day_7(r"problems/day7_sample.txt")
    day:problem

    assert day.solve() == "95437,24933642"
