import math
def factors(num):
    factor = [i for i in range(1,int(math.ceil(math.sqrt(num)))) if num%i == 0]
    factor.extend([i for i in range(int(math.ceil(math.sqrt(num))),num+1) if num%i == 0])
    return factor
print(factors(100))



