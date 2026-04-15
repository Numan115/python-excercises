def string_ops(s):
    reversed_s = s[::-1]
    every_second = s[1::2]
    return reversed_s, every_second

print(string_ops("hello"))




def odd_indices(lst):
    return [i for i, val in enumerate(lst) if val % 2 != 0]

print(odd_indices([10,11,12,13,14]))


def rotate_list(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

print(rotate_list([1,2,3,4,5], 2))


def list_to_dict(keys, values):
    return dict(zip(keys, values))

print(list_to_dict(["a","b","c"], [1,2,3]))


def manual_iteration(lst):
    it = iter(lst)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

manual_iteration([1,2,3,4])
