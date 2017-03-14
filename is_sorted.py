def is_sorted(lst):
    if type(lst) == list and lst:
        for i in lst:
            if type(i) != int and int(i) != i:
                return None
        return sorted(lst) == lst
    return None
