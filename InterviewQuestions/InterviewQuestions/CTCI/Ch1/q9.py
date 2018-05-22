# Check if string is rotation of another
class StringRotation:
    def __init__(self):
        print ""

    @staticmethod
    def isRotationBook(string1, string2):
        if len(string1) != len(string2):
            return False

        string1List = list(string1)
        for character in string1:
            string1List.append(character)

        return string2 in ''.join(string1List)

    @staticmethod
    def isRotation(string1, string2):
        if len(string1) != len(string2):
            return False

        for i in xrange(string2):
            if string2[i] == string1[0]:
                print "Found my char in string1"


if __name__ == '__main__':
    #  Books way
    print StringRotation.isRotationBook('caleb', 'alebc')  # true
    print StringRotation.isRotationBook('calebkumar', 'kumarcaleb')  # true
    print StringRotation.isRotationBook('cale', 'ale')  # false
    print StringRotation.isRotationBook('cale', 'cake')  # false

    #  My way
    # StringRotation.isRotation('caleb', 'alebc')  # true
    # StringRotation.isRotationBook('calebkumar', 'kumarcaleb')  # true
    # StringRotation.isRotationBook('cale', 'cae')  # false
    # StringRotation.isRotationBook('cale', 'cake')  # false
