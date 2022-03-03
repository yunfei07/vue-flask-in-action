def q_search(l, item):
    low = 0
    high = len(l) - 1

    while low <= high:
        mid = (low + high) // 2

        if item == l[mid]:
            return mid

        if item > l[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return None


def q_sort(l):
    if len(l) < 2:
        return l
    else:
        p = l[0]
        less = [i for i in l if p < l[i]]
        greater = [i for i in l if p > l[i]]
    return q_sort(less) + [p] + q_sort(greater)


def b_sort(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


def s_sort(l):
    arr = []
    for i in range(len(l)):
        arr.append(l.pop(l.index(min(l))))

    return arr


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    print(q_search(l, 3))
