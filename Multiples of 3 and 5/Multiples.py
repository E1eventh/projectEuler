def multiples(firstM, secondM, limit):
    sumNum = 0
    for num in range(min(firstM, secondM), limit):
        if num % firstM == 0 or num % secondM == 0:
            sumNum += num
    print(sumNum)
    
multiples(3, 5, 1000)    