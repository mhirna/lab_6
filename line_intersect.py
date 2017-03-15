def line_intersect(line1, line2):
    "Find coordinates, in which two lines intersect."
    if type(line1) == type(line2) == list:
        if len(line1) == len(line2) == 2:
            for i in line1 + line2:
                if len(i) != 2:
                    return None
            a1 = line1[1][1] - line1[0][1]
            b1 = line1[0][0] - line1[1][0]
            c1 = a1 * line1[0][0] - b1 * line1[0][1]
            a2 = line2[1][1] - line2[0][1]
            b2 = line2[0][0] - line2[1][0]
            c2 = a2 * line2[0][0] - b2 * line2[0][1]
            if b1 * a2 - b2 * a1 != 0:
                y = (c2 * a1 - c1 * a2) / (b1 * a2 - b2 * a1)
                x = (-c1 - b1 * y) / a1
                return (x, y)
            elif a1 == a2 and b1 == b2 and c1 == c2:
                return line1
    return None
