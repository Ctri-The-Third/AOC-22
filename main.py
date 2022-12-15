import models.day_0
import models.day_1, models.day_2, models.day_3, models.day_4
import models.day_5, models.day_6, models.day_7
if __name__ == "__main__":
    d1 = models.day_1.Day_1("problems/day1_input.txt")
    print(f"Day 1: {d1.solve()}" )
    d2 = models.day_2.Day_2("problems/day2_input.txt")
    print(f"Day 2: {d2.solve()}" )
    d3 = models.day_3.Day_3("problems/day3_input.txt")
    print(f"Day 3: {d3.solve()}" )
    d4 = models.day_4.Day_4("problems/day4_input.txt")
    print(f"Day 4: {d4.solve()}" )


    d5 = models.day_5.Day_5("problems/day5_input.txt")
    print(f"Day 5: {d5.solve()}" )
    d6 = models.day_6.Day_6("problems/day6_input.txt")
    print(f"Day 6: {d6.solve()}")

    d7 = models.day_7.Day_7("problems/day7_input.txt")
    print(f"Day 7: {d7.solve()}")
