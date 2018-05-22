def checkIfPalindrome(str):
    i, j = 0, len(str) - 1

    while i < j:
        if str[i] != str[j]:
            return False
        else:
            i += 1
            j -= 1

    return True


if __name__ == '__main__':
    print(checkIfPalindrome("calac"))
    print(checkIfPalindrome("caac"))
    print(checkIfPalindrome("caab"))
