class Practice:
    def __init__(self):
        print ""

    # @staticmethod
    # def test():
    #     print "static method"

    def test(self):
        print "class method"

    @staticmethod
    def numeric_compare(x, y):
        if x < y:
            return -1
        elif x == y:
            return 0
        else:
            return 1

    # Product Mapping Function
    def mapTagsToPredixServices(row):
        if row['account_category'] == 'Blobstore' and row['product_l3'] != 'Postgres 2.0':
            return 'Blobstore'
        elif 'event' in row['app_tag'] or 'kafka' in row['app_tag']:
            return 'Eventhub'


if __name__ == '__main__':
    practice = Practice()
    # practice.test()

    # print('{} {} {}     {}'.format(3, 'hello', ["caleb", 'Kumar', 5], {'caleb': 4, 'kumar': 8}))

    values = set()
    # print values.add(3)

    nums = [1, 2, 3, 4]
    # print(sorted(nums, reverse=True))

    nums2 = [5, 3, 2, 6]
    print(sorted(nums2, cmp=Practice.numeric_compare))

    # nums.sort(reverse=True)
    # print(nums)
