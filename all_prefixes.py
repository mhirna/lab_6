def all_prefixes(s):
    if type(s) == str:
        return set([s[:i] for i in range(1, len(s) + 1)])
    return None
