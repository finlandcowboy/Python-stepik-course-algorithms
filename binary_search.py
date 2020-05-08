import sys

def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    n, *a = next(reader)
    k, *b = next(reader)
    indexes = []
    for i in b:
        indexes.append(binary_search(a,i))
    for k in indexes:
        print(k, end=' ')

def binary_search(a,elem):
    left = 0
    right = len(a)

    while left < right:
        middle = (left + right) // 2

        if elem == a[middle]:
            return middle + 1
        elif elem > a[middle]:
            left = middle + 1
        else:
            right = middle
    return -1
            


if __name__ == "__main__":
    main()
