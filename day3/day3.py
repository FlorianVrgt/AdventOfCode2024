import re

def main1(inputList):
    # parse input
    l1 = []
    for part in inputList:
        l1.append(re.findall(r"mul\(-?\d{1,3},-?\d{1,3}\)",part))
    result = 0
    for item in l1:
        for it in item:
            l2 = re.findall(r"-?\b\d+\b",it)
            result += (int(l2[0])*int(l2[1]))
    print(result)


def main2(inputList):
    # parse input
    l1 = []
    for part in inputList:
        l1.append(re.findall(r"mul\(-?\d{1,3},-?\d{1,3}\)|do\(\)|don't\(\)",part))
    print(l1)
    result = 0
    math = True
    for item in l1:
        for it in item:
            if(it == 'do()'):
                math = True
            elif(it == "don't()"):
                math = False
            else:
                if(math):
                    l2 = re.findall(r"-?\b\d+\b",it)
                    print(l2)
                    result += (int(l2[0])*int(l2[1]))
    print(result)