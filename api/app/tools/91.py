from functools import reduce


def remove_item(l):
    low = 0
    arr = []
    while low <= len(l) - 1:
        for i in range(len(l)):
            if l[low]['a'] == l[i]['a']:
                arr.append(i)
        low += 1

    # a = list(set(arr))
    # for j in a:
    #     l[j] = 0
    # for i in l:
    #     print(i)
    # x = [i for i in l if i != 0]
    return list(set(arr))


def remove_duplicate(dict_list):
    seen = set()
    new_dict_list = []
    for dict in dict_list:
        t_dict = {'res_model': dict['res_model'], 'res_id': dict['res_id']}
        t_tup = tuple(t_dict.items())
        if t_tup not in seen:
            seen.add(t_tup)
            new_dict_list.append(dict)
    return new_dict_list


def list_dict_duplicate_removal():
    data_list = [{"a": "123", "b": "321"}, {"a": "123", "b": "321"}, {"b": "321", "a": "123"}]
    run_function = lambda x, y: x if y in x else x + [y]
    return reduce(run_function, [[], ] + data_list)
if __name__ == '__main__':
    x = [1,2,3,4]
    l = [{"a": 1, "b": 2}, {"a": 1, "b": 3}, {"a": 1, "b": 5}, {"a": 1, "b": 5}, {"a": 2},{"a":1}]


