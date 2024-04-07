# 최대 공약수를 구해야 할 때는 math 라이브러리의 gcd() 함수를 이용

import math

# 최소 공배수 (LCM) 구하는 함수


def lcm(a, b):
    return a * b // math.gcd(a, b)


a = 21
b = 14

print(math.gcd(a, b))  # 최대 공약수 (GCD)
print(lcm(a, b))  # 최소 공배수 (LCM)
