import sys 
import pytest

#weird thing to support vscode's built in handling of pytest
sys.path.append("")

from models.day_0 import problem


def test_day_1():
    from models.day_1 import Day_1
    d1 = Day_1(r".\problems\day1_sample.txt")
    d1:problem 
    assert d1.solve() == "24000,45000"


def test_day_2():
    from models.day_2 import Day_2
    day = Day_2(r".\problems\day2_sample.txt")
    day:problem 
    assert day.solve() == "15,12"

@pytest.mark.skip
def test_day_3():
    pass 

@pytest.mark.skip
def test_day_4():
    pass 
    

