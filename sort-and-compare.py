def anagram_solution2(s1, s2):
    """Sort and compare
    Anagram consist of exactly similar characters
    Sort from a-z, we will end up same string if two strings are anagram
    sort method is built in
    Unlike checking off, this method won't work if there's extra similar char in second string
    This method is O(n^2) or O(n log n) depending on sorting algorithm
    """

    a_list1 = list(s1)
    a_list2 = list(s2)

    a_list1.sort()
    a_list2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if a_list1[pos] == a_list2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches


print(anagram_solution2("abcde", "ecdba"))
