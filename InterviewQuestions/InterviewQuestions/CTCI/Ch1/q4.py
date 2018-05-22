#
class PalindromePermutation:
    def __init__(self):
        print("")

    @staticmethod
    def checkPalindromePermutation(string):
        string = string.replace(" ", "")
        string = string.lower()
        charToCharCount = {}
        for character in string:
            if character not in charToCharCount.keys():
                charToCharCount[character] = 1
            else:
                charToCharCount[character] += 1

        stringLength = len(string)
        hasMiddleCharacter = False
        for key, value in charToCharCount.iteritems():
            if value % 2 == 1:
                if stringLength % 2 == 1:
                    if hasMiddleCharacter:
                        return False
                    else:
                        hasMiddleCharacter = True;
                else:
                    return False
        return True

    @staticmethod
    def checkIsPalindrome(string):
        string = string.replace(" ", "")
        for i in xrange(len(string)):
            if string[i] != string[len(string) - 1 - i]:
                return False

        return True


if __name__ == '__main__':
    # Palindrome tester checking
    # print(PalindromePermutation.checkIsPalindrome("taco cat"))  # true
    # print(PalindromePermutation.checkIsPalindrome("belec"))  # false

    print(PalindromePermutation.checkPalindromePermutation("lebcel"))  # Should be false
    print(PalindromePermutation.checkPalindromePermutation("lebel"))  # Should be true
    # Test with spaces
    print(PalindromePermutation.checkPalindromePermutation("tact coa"))  # true bcuz "taco cat"
    # Test with upper case
    print(PalindromePermutation.checkPalindromePermutation("Tact Coa"))  # true bcuz "taco cat"
