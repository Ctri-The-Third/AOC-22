from models.day_0 import problem
import string
import math


class Day_3(problem):

    def __init__(self,  file_in=None, file_out=None) -> None:
        super().__init__("day_3", file_in, file_out)


    def solve(self):
        part_1_out = 0 
        counter = 0
        group = [] 
        part_2_out = 0 

        for line in self.problem:
            # part 2 stuff 
            group.append(line)
            counter += 1 
            if counter % 3 == 0:
                part_2_out += convert_char_to_int(find_badge(group))
                group = [] 

            #part 1 stuff 
            half_ind = int(len(line) / 2) 
            left = line[0:half_ind]
            right = line[half_ind:]
            match = find_match(left,right)
            priority = convert_char_to_int(match)
            part_1_out += priority
        
        self.solution = f"{part_1_out},{part_2_out}"

        return super().solve()

def find_badge(back_packs:list ) -> int:
    smallest_backpack = f"{back_packs[0]}{back_packs[1]}{back_packs[2]}"
    #first find the smallest backpack
    #because that will require the fewest comparisons
    for pack in back_packs:
        if len(pack) < len(smallest_backpack):
            smallest_backpack = pack
    

    #take the smallest backpack out of the pile
    back_packs.remove(smallest_backpack)


    #for each unique item in the backpack
    for char in set(smallest_backpack):
        badge = True #assume we found the badge
        for pack in back_packs:
            if char not in pack:
                #turns out it's not the badge
                badge = False
                continue
        if badge:
            break
    return char

    #second if we can, remove the duplicate entries 

def find_match(left,right):
    for char in left:
        if char in right:
            return char 

def convert_char_to_int(char:str):
    if not isinstance(char,str):
        return -1 
    try: 
        return string.ascii_lowercase.index(char) + 1
    except ValueError:
        pass 

    try:
        return string.ascii_uppercase.index(char) + 27
    except ValueError:
        pass 

    return -1 



if __name__ == "__main__":
    day = Day_3(r"problems/day3_sample.txt")
    print(day.solve())
    convert_char_to_int("b")
    convert_char_to_int("B")

