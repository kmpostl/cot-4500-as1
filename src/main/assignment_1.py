from os import cpu_count
import numpy as np
#import sympy as sy

def main():
    #######################Question 1###########################
    one = ieeeBinarytoDecimal("010000000111111010111001")
    print(one)
    print()
    #print(xChop(3, "010000000111111010111001"))

    #######################Question 2###########################
    two = chopSecondApproach(3, one)
    print(two)
    print()
    #######################Question 3###########################
    three = rounding(3, one)
    print(three)
    print()

    #######################Question 4###########################
    absoluteRound = absoluteError(three, one)
    relativeRound = relativeError(three, one)
    print(absoluteRound)
    print(relativeRound)
    print()

    #######################Question 5###########################
    count = randomFormulaConverage(10**-4) 
    print(count)
    print()
    #######################Question 6###########################
    def formula(x):
        return (np.power(x, 3)) + (4*np.power(x, 2)) - 10
    def derivative(x):
        return (3*np.power(x,2)) + (8*x)
    arr = bisection(-4, 7, formula, .0001)
    print(str(arr[0]))
    #print("a: " + str(arr[1]))
    #print("b: " + str(arr[2]))
    #print("f_cn: " + str(arr[3]))
    arr2 = newtonRaph(7, formula, derivative, .0001)
    print()
    print(arr2[0])
    

def ieeeBinarytoDecimal(binaryNum):
    sign = (-1)**int(binaryNum[0])
    exponent = 0
    currentTwo = 1

    for i in range(11, 0, -1):
        if (binaryNum[i] == '1'):
            exponent += currentTwo
        currentTwo = 2*currentTwo
    exponent = exponent - 1023
    constant = np.power(2, exponent)
    currentTwo = 2
    fraction = 1.0
    for i in range(12, len(binaryNum)):
        if (binaryNum[i] == '1'):
            fraction += (1/currentTwo)
        currentTwo = 2*currentTwo 

    return round((sign * (constant * fraction)), 5)

""" def xChop(x, binaryNum):
    num = ieeeBinarytoDecimal(binaryNum)
    strNum = list(str(num))
    ##print(strNum)
    for i in range(len(strNum)):
        if (i < x and strNum[i] == '.'):
            x += 1
            continue
        if(i >= x and strNum[i] != '.'):
            strNum[i] = '0'
    return float("".join(strNum)) """

def chopSecondApproach(x, num):
    tens = 1
    while (num > 1):
        num /= 10
        tens *= 10
    chop = list(str(num))
    temp = 0
    for i in range(2, x + 2):
        tens = tens / 10
        temp = temp + (int(chop[i]) * tens)
    return temp

def rounding(x, num):
    tens = 1
    while (num > 1):
        num /= 10
        tens *= 10
    temp = .5
    for i in range(x):
        temp /= 10
    
    chop = list(str(num))
    temp2 = 0
    tens2 = 10
    for i in range(2, x + 3):
        temp2 = temp2 + (float(chop[i]) * (1/tens2))
        tens2 = tens2 * 10
    #print("TEMP1::::::::::::::::::: ", temp, "\t\tTEMP2:::::::::::::::::: ", temp2)
    #print(temp + temp2)
    temp = round(temp2 + temp, x) * tens
    #print("NEWNWNWNWN TEMP:::::: " , temp)
    return temp

def absoluteError(x, y):
    return abs(x - y)

def relativeError(x, y):
    return absoluteError(x,y) / y

def randomFormulaConverage(accuracy):
    k = 1
    res2 = 1
    
    def func(k): 
        return (-1)**k * (1**k) / (k**3)
    res = abs(func(k))
    res2 = res + abs(func(k + 1))
    diff = abs(res2 - res)
    while(diff > accuracy):
        res = res2
        k += 1
        res2 += abs(func(k))
        diff = abs(res2 - res)
    return k - 1

def bisection(a, b, func, accuracy):
    count = 0
    cn = 0
    f_cn = 1
    diff = 1
    while(abs(diff) > accuracy):
        cn = (a + b) / 2
        f_cn = func(cn)
        if (f_cn == 0.0):
            break
        if (f_cn < 0):
            a = cn
        else:
            b = cn
        count += 1
        diff = a - b
    return [count, a, b, f_cn]

def newtonRaph(initial, func, funcp, accuracy):
    result = func(initial) / funcp(initial)
    x = initial
    ## since vars are setup for loop this is one iteration
    count = 1
    
    while(abs(result) >= accuracy):
        x = x - result
        count += 1
        result = func(x) / funcp(x)

    return [count, result]

if __name__ == "__main__":
    main()


