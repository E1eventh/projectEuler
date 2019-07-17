def evenFibonacci (limit):
    numbers = []
    firstN = 1
    secondN = 1
    num = 1
    while num <= limit:
        num = firstN + secondN
        firstN = secondN
        secondN = num
        if num % 2 == 0:
            numbers.append(num)
    return sum(numbers)

print(evenFibonacci(4000000))