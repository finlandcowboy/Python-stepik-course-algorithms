def different_addends_iterative(n):
    k = 1
    addends = []

    while n >= 2 * k + 1:
        addends.append(k)
        n -= k
        k += 1

    addends.append(n)
    return k, addends

n = int(input())

k,addends = different_addends_iterative(n)

print(k)
print(*addends)
