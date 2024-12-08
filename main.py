import day2.day2 as day2


def main():
    #file1 = open("inputTest.txt")
    file1 = open("day2/input.txt")
    # Reading from file
    inputList = []
    line = file1.readline()
    while(line):
        inputList.append(line)
        line = file1.readline()
    file1.close()
    #day2.main1(inputList)
    day2.main2(inputList)


if __name__ == '__main__':
    main()