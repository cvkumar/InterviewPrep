'''
Write a class that has two functions
1) toString

2) addRanges (adds range to existing structure)
- ranges where there is overlap must combine into one range

Example: [(1, 3), (4, 5), (7, 12), (100, 1000)], (5, 13) => [(1, 3), (4, 13), (100, 1000)]

Solution:
We maintain a sorted list of ranges by startTime and with no overlap.

With Overlap case:
To add:
-We iterate left to right

-When we find an element to merge, we:
    -loop from it to the last range we can be merged with.
    -We delete all those ranges that we can merge with.
    -We create a new range from with the min start index and the max end index
    -We insert it at the position we first found the start at


No Overlap case:
We move left to right
When we find a start time greater than ours, we insert at that index
(could also easily apply binary search to this)

'''


class Ranges:

    def __init__(self):
        self.ranges = []

    def addRange(self, start, end):

        if not self.ranges:
            self.ranges.append((start, end))
            return

        for i in xrange((len(self.ranges))):

            # Overlap case
            if not (start > self.ranges[i][1] or end < self.ranges[i][0]):
                # print 'There was overlap for {} and {}'.format(start, end)

                start = min(start, self.ranges[i][0])
                # print 'start is: ' + str(start)

                j = i + 1
                # Find first element that does not overlap
                while not (start > self.ranges[i][1] or end < self.ranges[i][0]) and j < len(self.ranges):
                    j += 1

                # print 'no overlap for: ' + str(j)

                # Remove all elements with overlap
                k = i
                last = None
                while k < j:
                    last = self.ranges.pop(i)
                    k += 1

                self.ranges.insert(i, (start, max(end, last[1])))
                break

            # No overlap case
            if start < self.ranges[i][0]:
                self.ranges.insert(i, (start, end))
                break

            if i == len(self.ranges) - 1:
                self.ranges.insert(i + 1, (start, end))

    def __str__(self):
        return str(self.ranges)


if __name__ == '__main__':
    # No overlap testing
    test1 = Ranges()
    test1.addRange(0, 5)
    test1.addRange(6, 10)
    test1.addRange(11, 15)
    test1.addRange(-5, -1)
    # print test1

    # Overlap testing
    test2 = Ranges()
    test2.addRange(3, 5)
    test2.addRange(4, 7)
    test2.addRange(8, 25)
    test2.addRange(26, 100)
    test2.addRange(-1, 2)

    # Merge 3 elements
    test2.addRange(3, 88)
    # print test2

    # Merge All elements
    test2.addRange(101, 500)
    test2.addRange(-5, 200)
    # print test2
