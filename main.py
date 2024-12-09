import day3.day3 as currentDay


def main():
    #file1 = open("inputTest.txt")
    file1 = open("day3/input3.txt")
    # Reading from file
    inputList = []
    line = file1.readline()
    while(line):
        inputList.append(line)
        line = file1.readline()
    file1.close()
    #currentDay.main1(inputList)
    currentDay.main2(inputList)


if __name__ == '__main__':
    main()