# Check if two strings are permutations of each other
class PermutationChecker:
    def __init__(self):
        print("")

    @staticmethod
    def checkIfPermutationThroughSort(str1, str2):
        listStr1 = list(str1)
        listStr2 = list(str2)

        listStr1.sort()
        listStr2.sort()

        return listStr1 == listStr2

    @staticmethod
    def checkIfPermutationThroughMap(str1, str2):
        if len(str1) != len(str2):
            return False

        charCount = {}

        for char in str1:
            if char not in charCount.keys():
                charCount[char] = 1
            else:
                charCount[char] = charCount[char] + 1

        for char in str2:
            if charCount[char] < 1:
                return False
            charCount[char] -= 1

        return True


if __name__ == '__main__':
    print(PermutationChecker.checkIfPermutationThroughSort("abc", "bac"))
    print(PermutationChecker.checkIfPermutationThroughSort("caleb", "balec"))
    print(PermutationChecker.checkIfPermutationThroughSort("caleb", "baleb"))

    print(PermutationChecker.checkIfPermutationThroughMap("abc", "bac"))
    print(PermutationChecker.checkIfPermutationThroughMap("caleb", "balec"))
    print(PermutationChecker.checkIfPermutationThroughMap("caleb", "baleb"))
