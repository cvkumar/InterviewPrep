class Reverse:
    def __init__(self):
        print("")

    @staticmethod
    def reverse_string(a_string):
        new_str = []
        index = len(a_string)
        while index:
            index -= 1
            # print(index)
            # print(a_string[index])
            new_str.append(a_string[index])

        return ''.join(new_str)


if __name__ == '__main__':
    my_car = Reverse()

    print(Reverse.reverse_string(""))
