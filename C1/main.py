
"""
Script for the first laboratory.
Add code by following instructions of the teacher.
"""

from typing import Any, List


def add(a: int, b: int) -> int:
    """Adds parameters."""
    return a + b

def what_number(number: int|float) -> str:
    """Returns string positive/zero/negative specifying
    value of the number."""
    if number > 0:
        return "positive"
    elif number == 0:
        return "zero"
    else:
        return "negative"

def sum_of_numbers(lst: List[int|float]) -> int:
    return sum(lst)

def ship_name(fleet: dict, designated_no: Any) -> Any:
    """Return ship's name for specified designated number
    from the fleet."""
    return fleet[designated_no]
    

def how_many_5(numbers: List[int|float]) -> int:
    """Returns number of numbers greater than 5."""
    x = 0
    for number in numbers:
        if number > 5:
            x += 1
    return x
     

def gen_list_gt(lst: List[int|float], no: int|float) -> List[int|float]:
    """Returns list with numbers greater than no."""
    x = []
    for number in lst:
        if number > no:
            x.append(number)
    
    return x #list(filter(lambda x: x > no, lst))


print(add(1, 3))
#print(add([1, 2, 3], [4, 5, 6]))
# Try addition of strings or different data type and see what happens

#if statement example
n = 5
print("Number", n, "is:", what_number(n))

#for example: sum of the list example
lst = [1, 2, 3, 6, 7, 8]
print("Sum is:", sum_of_numbers(lst))

#dictionary example
fleet = {'BS62': 'Pegasus', "BS75": "Galactica", 36: 'Valkirie'}
designated_no = "BS62"
print("We've got {} in the fleet".format(ship_name(fleet, designated_no)))

#function to count how many numbers > 5 are in the list
lst = [1, 2, 5, 6, 7, 10, 12, 40, 3]
print("There are {} numbers greater than 5".format(how_many_5(lst)))

#generating list example
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
no = 5
print("List with numbers > {}: {}".format(no, gen_list_gt(lst, no)))
