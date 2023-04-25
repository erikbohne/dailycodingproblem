"""
april 25th 2023

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

def get_combinations(string):
    if len(string) == 1:
        return [[string]]
    
    combinations = []
    for i in [1, 2]:
        prefix = string[:i]
        suffix = string[i:]
    
        if suffix:
            for combination in get_combinations(suffix):
                combinations.append([prefix] + combination)
        else:
            combinations.append([prefix])
    
    
    return combinations

def get_count(lists):
    count = 0
    for list in lists:
        status = True
        for number in list:
            if int(number) > 26:
                status = False
                break
        count += 1 if status else 0
    
    return count
        

string = "111"
print(f"{string} -> {get_count(get_combinations(string))}")

string = "1111"
print(f"{string} -> {get_count(get_combinations(string))}")

string = "7711"
print(f"{string} -> {get_count(get_combinations(string))}") # 7711 -> [7, 7, 11] and [7, 7, 1, 1]

string = "111111111111111111111"
print(f"{string} -> {get_count(get_combinations(string))}")
            