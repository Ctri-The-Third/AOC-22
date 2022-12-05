import models.day_0
import models.day_1
import models.day_2
import models.day_3
import models.day_1
if __name__ == "__main__":
    d1 = models.day_1.Day_1("problems/day1_input.txt")
    print(f"Day 1: {d1.solve()}" )
    d2 = models.day_2.Day_2("problems/day2_input.txt")
    print(f"Day 2: {d2.solve()}" )


    d3 = models.day_3.Day_3("problems/day3_input.txt")
    print(f"Day 3: {d3.solve()}" )