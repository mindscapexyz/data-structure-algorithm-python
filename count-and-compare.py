def anagram_solution3(s1, s2):
    """
    Create two list of a-z of 0 (length = 26)
    Count the number of a-z characters happen and fill in the list created
    Check if those two lists have equivalent values [1 0 0 2 ...] = [1 0 0 1 ...]
    If yes then it is anagram
    """
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        print("First list")
        print(ord(s1[i]))
        print(ord("a"))
        pos = ord(s1[i]) - ord("a")
        print("POS", pos)
        c1[pos] = c1[pos] + 1
        print(c1[pos])

    for i in range(len(s2)):
        print("Second list")
        print(ord(s2[i]))
        print(ord("a"))
        pos = ord(s2[i]) - ord("a")
        c2[pos] = c2[pos] + 1
        print(c2[pos])

    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            still_ok = False

    return still_ok


print(anagram_solution3("apple", "pleap"))
