def anagram_solution1(s1, s2):
    """Checkoff solution
    Check each character in the first string actually occur in the second
    If it is possible to 'checkoff' each character then two strings must be anagram
    """
    a_list = list(s2)

    pos1 = 0
    still_ok = True

    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(a_list) and not found:
            if s1[pos1] == a_list[pos2]:
                found = True
            else:
                print("s1 is:", s1[pos1])
                print("s2 is:", a_list[pos2])
                pos2 = pos2 + 1

        if found:
            a_list[pos2] = None
            print("List is: ", a_list)
        else:
            still_ok = False

        pos1 = pos1 + 1
    return still_ok


print(anagram_solution1("abcd", "dcba"))
