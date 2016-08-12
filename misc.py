# Author = CCortello
# Date = 1/14/2016

"""Random musings and messings-around."""


def median(input_list):
    sorted_list = sorted(input_list)
    if len(input_list) % 2 == 1:
        return sorted_list[(len(sorted_list) - 1) / 2]
    else:
        first_pos = len(sorted_list) // 2 - 1
        return (sorted_list[first_pos] +
                sorted_list[first_pos + 1]) / 2

# print(median([4, 5, 5, 4]))

print(not not {})