def find_index(numbers, number):
    summa = []
    for i, num in enumerate(numbers):
        q = number - num
        if q in numbers:
            summa.append(i)
    print(summa)
find_index([5, 6, 1, 4], 7)
