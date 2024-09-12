import re
from collections import Counter

def find_largest_most_frequent_number(input_strings):
    all_numbers = []
    for string in input_strings:
        numbers = re.split(r'[^0-9]+', string)
        numbers = [int(num) for num in numbers if num]
        all_numbers.extend(numbers)
    
    if not all_numbers:
        return None

    number_count = Counter(all_numbers)
    max_frequency = max(number_count.values())
    most_frequent_numbers = [num for num, count in number_count.items() if count == max_frequency]
    largest_most_frequent_number = max(most_frequent_numbers)
    
    return largest_most_frequent_number

input_strings = ["11920G912A93128A30", "2929B920B990U11099A099P920"]
result = find_largest_most_frequent_number(input_strings)
print("The largest consecutive number that appears the most frequently is:", result)
