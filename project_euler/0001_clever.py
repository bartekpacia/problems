def sumDivisbleBy(n, p):
    return n*(p//n)*((p//n)+1)/2


result = sumDivisbleBy(3, 999) + sumDivisbleBy(5, 999) - sumDivisbleBy(15, 999)
print(result)
