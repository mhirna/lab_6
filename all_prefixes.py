def all_prefixes(s):
    if type(s) == str:
        set_str = set()
        s_index = [i for i in range(len(s)) if s[i] == s[0]]
        for ind in s_index:
            set_str = set_str | set([s[ind:i] for i in range(ind + 1, len(s) + 1)])
        return set_str
    return None

