import math
import random


def getRichterValue(amplituda):
    if amplituda > 0:
        return round(math.log10(10000*amplituda), 2)
    else:
        return -9999

def genarateList(my_list):
    for x in range(0, 20):
        my_list.append(random.randrange(1, 100))
        my_list.sort()
    print(my_list)


def uniqueList(my_list):
    my_list = list(dict.fromkeys(my_list))
    print(my_list)

def getValueRichterList(my_list, my_list_Richter):
    dim = len(my_list)
    for x in range(0,dim):
        my_list_Richter.append(getRichterValue(my_list[x]))

def showRichterList(my_list_Richter):
    if len(my_list_Richter)>0:
        print(my_list_Richter)
    else: print('empty list')

if __name__ == '__main__':
    print(getRichterValue(121))
    my_list = list()
    my_list_Richter = list()
    genarateList(my_list)
    uniqueList(my_list)
    getValueRichterList(my_list, my_list_Richter)
    showRichterList(my_list_Richter)