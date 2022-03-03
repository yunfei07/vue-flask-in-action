def b_search(l, item):
    low = 0
    high = len(low) - 1

    while low < high:
        mid = (low + high) // 2
        if item == l[mid]:
            return mid

        if item > l[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return None


def b_sort(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - 1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l


def s_sort(l):
    arr = []
    for i in range(len(l)):
        arr.append(l.pop(l.index(min(l))))
    return arr


def q_sort(l):

    if len(l) < 2:
        return l
    else:
        p = l[0]
        less = [i for i in l if i < p]
        greater = [i for i in l if i > p]

    return q_sort(less) + [p] + q_sort(greater)


def i_sort(l):
    pass


if __name__ == '__main__':
    li = [2, 3, 1, 0, 5, 4, 8]
    lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(q_sort(li))
