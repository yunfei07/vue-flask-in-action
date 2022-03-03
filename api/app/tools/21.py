def b_search(l, item):
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


def b_sort(l):
    for x in range(len(l) - 1):
        for y in range(len(l) - 1):
            if l[y] > l[y + 1]:
                l[y], l[y + 1] = l[y + 1], l[y]
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
        greater = [i for i in l if l > p]
    return q_sort(less) + p[0] + q_sort(greater)


def del_num(l):
    for x in l:
        if isinstance(x, list):
            del_num(x)
        elif x == 1:
            l.pop(l.index(1))
            del_num(l)
    return l


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7]
    b = [1, 2, 3, [1, [9, 8, 1, 7]], [2, 3, 1, 1]]
    # print(b_search(a, 3))
    print(del_num(b))
