# String has all unique characters
class UniqueStringChecker:
    def __init__(self):
        print("")

    @staticmethod
    def check_unique_string(string):
        unique_set = [False] * 256
        for char in string:
            if unique_set[ord(char)]:
                return False
            else:
                unique_set[ord(char)] = True

        return True


if __name__ == '__main__':
    print(UniqueStringChecker.check_unique_string("test"))
    print(UniqueStringChecker.check_unique_string("true"))
    print(UniqueStringChecker.check_unique_string("false"))
    print("False: " + str(UniqueStringChecker.check_unique_string("calec")))
