from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    stack = arr.copy()
    myList = []

    while len(stack) > 0:
        value = stack.pop()
        myList.append(value)
    return myList



# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
