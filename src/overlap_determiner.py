# Function that returns maximum
# overlap among ranges in a list


def max_overlap(pairs):
    max_overlap_cnt = 0
    count = 0
    vec = []
    if not pairs:
        return 0

    for item in pairs:
        # label the start values
        vec.append([item['startTime'], 's'])
        # label the end values
        vec.append([item['endTime'], 'e'])

    vec = sorted(vec, key=lambda a: a[0])

    # Traverse the data vector to count number of overlaps
    for item in vec:
        if item[1] == 's':
            count += 1
        if item[1] == 'e':
            count -= 1
        max_overlap_cnt = max(max_overlap_cnt, count)

    return max_overlap_cnt
