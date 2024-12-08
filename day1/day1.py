def main1(inputList):
    # parse input
    l1,l2 = [],[]
    for ele in inputList:
        div = ele.split()
        l1.append(int(div[0]))
        l2.append(int(div[1]))
    l1.sort()
    l2.sort()

    # result 
    result = 0
    for i in range(0,len(l1)):
        result += abs(l1[i]-l2[i])
    print(result)


def main2(inputList):
    # parse input
    l1,l2 = [],[]
    for ele in inputList:
        div = ele.split()
        l1.append(int(div[0]))
        l2.append(int(div[1]))
    l1.sort()
    l2.sort()

    # result 
    result = 0
    for i in range(0,len(l1)):
        result += l2.count(l1[i]) * l1[i]
    print(result)