def RadixSort(a: list)->list:
    radix = []
    for _ in range(10):
        radix += [[]]
    max_val = max(a)
    exp = 1
    while max_val // exp > 0:
        while len(a) > 0:
            temp = a.pop()
            radix_idx = (temp // exp) % 10
            radix[radix_idx].append(temp)
        #
        for bucket in radix:
            while len(bucket) > 0:
                a.append(bucket.pop())
        exp *= 10
    return a

def QuickSort(a:list)->list:
    if len(a) <= 1:
        return a
    pivot = a[-1]  # last element as pivot
    left = [x for x in a[:-1] if x < pivot]
    right = [x for x in a[:-1] if x >= pivot]
    return QuickSort(left) + [pivot] + QuickSort(right)


def BubbleSort(a:list)->list:
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


if __name__ == "__main__":
    alist = [2, 170, 68, 85, 90, 47, 812, 24]
    print(f"Bubble Sort : {BubbleSort(alist)}")
    print(f"Quick Sort : {QuickSort(alist)}")
    print(f"Radix Sort : {RadixSort(alist)}")
