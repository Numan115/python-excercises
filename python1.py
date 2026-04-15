def string_ops(s):
    reversed_s = s[::-1]
    every_second = s[1::2]
    return reversed_s, every_second

print(string_ops("hello"))
