def sda4a(n):
    a = []
    a.append((n // 25))
    a.append(((n % 25) // 10))
    a.append((((n % 25) % 10) // 5))
    a.append(((((n % 25) % 10) % 5) // 1))
    return a

n = int(input())
print(sda4a(n))
