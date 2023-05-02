def combine_strings(a, b):
    a_length = len(a)
    b_length = len(b)
    a_front = a[:(a_length + 1) // 2]
    a_back = a[(a_length + 1) // 2:]
    b_front = b[:(b_length + 1) // 2]
    b_back = b[(b_length + 1) // 2:]
    return a_front + b_front + a_back + b_back


a = "abcdef"
b = "ghijklm"
result = combine_strings(a, b)
print(result)
