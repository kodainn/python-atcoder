def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)

print(lcm(12, 18))	# => 36

print(lcm(3, 4))	# => 12