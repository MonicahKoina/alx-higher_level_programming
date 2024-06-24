#!/usr/bin/python3
def remove_char_at(str, n):
    strcopy = ""
    count = 0
    for i in range(len(str)):
        if count == n:
            strcopy += ''
        elif count != n:
            strcopy += str[count]
        count += 1
    return strcopy
