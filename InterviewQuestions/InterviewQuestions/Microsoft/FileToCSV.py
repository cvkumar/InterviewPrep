import io
import re

class FileToCsv:
    def __init__(self):
        print("")


if __name__ == '__main__':
    f = io.open("/Users/calebkumar/work/AwsDailyCostData.csv", 'r', encoding='utf-16-le')
    fileText = f.read()
    fileText = re.sub(r"([\t]+)", ',', fileText)

    newFile = open('/Users/calebkumar/work/AwsDailyCostDataTest.csv', 'w')
    newFile.write(fileText.encode('utf-8'))

    newFile.close()
    f.close()
