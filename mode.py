def mode(numbers):
    counts = {}
    max_count = 0
    mode_val = None

    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > max_count:
            max_count = counts[num]
            mode_val = num

    return mode_val