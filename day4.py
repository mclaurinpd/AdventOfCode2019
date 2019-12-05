def main():
    min = 264793
    max = 803935
    count = 0

    for x in range(min, max + 1):
        if checkIncreasing(x):
            if checkForDouble(x):
                count+=1

    print(count)
        

def checkForDouble(num):
    temp = str(num)
    isDouble = False
    x = 0
    while(x < len(temp)-1):
        if temp[x] == temp[x+1]:
            isDouble = True
            if x < len(temp) - 2 and temp[x] == temp[x+2]:
                isDouble = False
                while(x < len(temp) - 1 and temp[x] == temp[x+1]):
                    x+=1
        x+=1
        if(isDouble):
            return isDouble

    return isDouble

def checkIncreasing(num):
    temp = str(num)
    for x in range(len(temp)-1):
        if int(temp[x]) > int(temp[x+1]):
            return False

    return True

main()