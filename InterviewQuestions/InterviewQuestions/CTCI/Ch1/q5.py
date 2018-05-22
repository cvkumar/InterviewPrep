# Given two strings if I add, remove, or replace char can the strings be equivalent
class OneAway:
    def __init__(self):
        print("")

    def checkIfOneAway(self, string1, string2):
        string1Pointer = 0
        string2Pointer = 0
        oneDifference = False
        while string1Pointer < len(string1) and string2Pointer < len(string2):
            if string1[string1Pointer] != string2[string2Pointer]:
                if oneDifference:
                    return False
                else:
                    if len(string1) > len(string2):
                        string1Pointer += 1

                    else:
                        string2Pointer += 1

                    oneDifference = True
            else:
                string1Pointer += 1
                string2Pointer += 1

        return True


if __name__ == '__main__':
    oneAway = OneAway()
    print oneAway.checkIfOneAway("pale", "ple")  # true
    print oneAway.checkIfOneAway("pale", "pala")  # true
    print oneAway.checkIfOneAway("pale", "bele")  # false
    print oneAway.checkIfOneAway("", "")  # true
    print oneAway.checkIfOneAway("", "a")  # true
    print oneAway.checkIfOneAway("b", "a")  # true

    # print oneAway.checkIfOneAway("ple", "pale")  # true
    # print oneAway.checkIfOneAway("pale", "pala")  # true
    # print oneAway.checkIfOneAway("bele", "pale")  # false
