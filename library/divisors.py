def divisors(n: int) -> list[int]:
    return_list = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            return_list.append(i)
            if(i * i != n):
                return_list.append(n // i)
    
    return sorted(return_list)


print(divisors(36))