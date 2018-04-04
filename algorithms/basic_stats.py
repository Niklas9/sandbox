# basic stats such as mean, median, mode and range
# python 3 plz

def mean(numbers):
    if len(numbers) <= 1:
        #raise Exception('need at least 2 numbers to calculate the mean')
        return None
    s = 0
    for number in numbers:
        s += number
    return s / len(numbers)

assert mean([]) == None
assert mean([1]) == None
assert mean([1,2]) == 1.5
assert mean([-2,6,-6,3]) == 0.25
assert mean([13, 13, 13, 13, 14, 14, 16, 18, 21]) == 15


def median(numbers):
    if len(numbers) == 0:  return None
    numbers = sorted(numbers)  # using sorted since we don't want to invoke
                               # input argument
    if len(numbers) % 2 == 0:  # even
        # find the center two most numbers
        center_numbers = [numbers[int(len(numbers)/2)],
                          numbers[int(len(numbers)/2-1)]]
        return mean(center_numbers)
    else:
        # find middle integer
        return numbers[int(((len(numbers)/2)+0.5)-1)]


assert median([]) == None
assert median([9]) == 9
assert median([1,2]) == 1.5
assert median([1,2,3]) == 2
assert median([1,2,3,4]) == 2.5
assert median([13, 13, 13, 13, 14, 14, 16, 18, 21]) == 14


def mode(numbers):
    if len(numbers) == 0:  return None
    # make histogram in hash table
    histogram = {}
    for number in numbers:
        if number in histogram:
            histogram[number] += 1
        else:
            histogram[number] = 1
    # find the number with the most occurances
    max_occurances = 0
    number_w_max_occurances = None
    for k, v in histogram.items():
        if v > max_occurances:
            max_occurances = v
            number_w_max_occurances = k
    return number_w_max_occurances

assert mode([13, 13, 13, 13, 14, 14, 16, 18, 21]) == 13


def stat_range(numbers):  # not naming it 'range' due to conflict with built-in
    if len(numbers) <= 2:  return None
    smallest_number = None
    highest_number = None
    for number in numbers:
        if smallest_number is None and highest_number is None:
            smallest_number = number
            highest_number = number
        elif number < smallest_number:
            smallest_number = number
        elif number > highest_number:
            highest_number = number
    return highest_number - smallest_number

assert stat_range([13, 13, 13, 13, 14, 14, 16, 18, 21]) == 8
