import Stack


class DailyTemperature:
    def __init__(self):
        print("")

    @staticmethod
    def findWarmerDays(nums):
        stack = Stack.Stack()
        result = [0] * len(nums)

        for i in range(0, len(nums)):
            while not stack.isEmpty() and nums[stack.peek()] < nums[i]:
                index = stack.pop()
                result[index] = i - index
            stack.push(i)

        return result


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(DailyTemperature.findWarmerDays(temperatures))

    dailyTemp = DailyTemperature()