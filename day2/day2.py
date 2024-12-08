def main1(inputList):
    # parse input
    l1 = []
    for ele in inputList:
        div = ele.split()
        l1.append(div)
    
    # result
    result = 0
    for item in l1:
        safe = True
        increase = (int(item[0])- int(item[1])) < 0
        if(not(increase)):
            i = 1
            while(safe and i<len(item)):
                if(0 < (int(item[i-1])- int(item[i])) < 4):
                    i+=1
                else:
                    safe = False
        else:
            i = 1
            while(safe and i<len(item)):
                if(0 > (int(item[i-1])- int(item[i])) > -4):
                    i+=1
                else:
                    safe = False
        if(safe):
            result += 1
            print(item)
    print(result)

def main2(inputList):
    # parse input
    l1 = []
    for ele in inputList:
        div = ele.split()
        l1.append(div)
    
    # result
    result = 0
    for item in l1:
        i = 1
        increase = True
        safe = True
        error = 0
        justHappen = False
        while(safe and i<len(item)):
            if(justHappen):
                calcul = int(item[i-2]) - int(item[i])
                justHappen = False
            else:
                calcul = int(item[i-1]) - int(item[i])
            if(0 < abs(calcul) < 4):
                if((i == 1 or (i==2 and error==1) ) and calcul > 0):
                    increase = True
                if((i == 1 or (i==2 and error==1)) and calcul < 0):
                    increase = False
                if(calcul > 0 and increase):
                    i+=1
                elif(calcul < 0 and not(increase)):
                    i+=1
                else:
                    if(error == 0 and i == len(item)-1):
                        i+=1
                    else:
                        error += 1
                        justHappen = True
                        if(error > 1):
                            safe = False
            else:
                if(error == 0 and i == len(item)-1):
                    i+=1
                else:
                    error += 1
                    justHappen = True
                    if(error > 1):
                        safe = False
        if(safe):
            if(result < 10):
                print(item)
            result += 1

    print(result)
