txt1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. God jul."
txt2 = "The quick brown fox jumps over the lazy dog. Godt nytt år."

memo = {}


def levenshtein(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    cost = 0 if s[-1] == t[-1] else 1

    i1 = (s[:-1], t)
    if i1 not in memo:
        memo[i1] = levenshtein(*i1)
    i2 = (s, t[:-1])
    if i2 not in memo:
        memo[i2] = levenshtein(*i2)
    i3 = (s[:-1], t[:-1])
    if i3 not in memo:
        memo[i3] = levenshtein(*i3)
    res = min([memo[i1] + 1, memo[i2] + 1, memo[i3] + cost])

    return res


print(levenshtein(txt1, txt2))
