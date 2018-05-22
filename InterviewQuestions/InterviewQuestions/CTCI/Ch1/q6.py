# compress string to numbers
class StringCompression:
    def __init__(self):
        print("")

    @staticmethod
    def compressString(string):
        compressedString = []
        i = 0
        j = 0
        charCount = 0

        while i in xrange(len(string)):
            while j < len(string) and string[i] == string[j]:
                charCount += 1
                j += 1

            compressedString.append(string[i] + str(charCount))
            charCount = 0
            i = j

        compressedString = ''.join(compressedString)
        return compressedString if len(compressedString) <= len(string) else string


if __name__ == '__main__':
    print(StringCompression.compressString("aabcccc"))  # a2b1c4
    print(StringCompression.compressString("aabbc"))  # aabbc
    print(StringCompression.compressString("aabcccaaa"))  # a2b1ca3
    print(StringCompression.compressString(""))  #
    print(StringCompression.compressString("a"))  # a
    print(StringCompression.compressString("aa"))  # a2
