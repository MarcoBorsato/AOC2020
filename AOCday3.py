def trees(data):
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

    totalcount = 1

    coords = [0, 0]

    input = [list(line[:-1]) for line in data]

    length = len(input[0])

    for slope in slopes:
        count = 0
        while coords[1] < len(input):
            if input[coords[1]][coords[0]] == "#":
                count += 1

            coords[0] += slope[0]
            if coords[0] >= length:
                coords[0] = coords[0] % length
            coords[1] += slope[1]
        totalcount = totalcount * count
        coords = [0, 0]

    return totalcount