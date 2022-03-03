def search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if target == arr[mid]:
            return mid

        if target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return None


def b_sort(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]

    return l


def s_sort(l):
    arr = []
    for i in range(len(l) - 1):
        arr.append(l.pop(l.index(min(l))))
    return arr


def q_sort(l):
    if len(l) < 2:
        return l
    else:
        p = l[0]
        less = [i for i in l if p < l[i]]
        greater = [i for i in l if p > l[i]]

    return q_sort(less) + [p] + q_sort(greater)


def i_sort(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1

        while j >= 0 and key < l[j]:
            l[j + 1] = l[j]
            j -= 1
            l[j + 1] = key
    return l


def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret


if __name__ == '__main__':
    s = spread([1, 2, 3, [4, 5, 6], [7], 8, 9])
    # lst = [7, 4, 9, 2, 6, 3]
    # print(i_sort(lst))
    print(s)
