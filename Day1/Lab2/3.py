def is_unique(list):
    stack = []
    for i in list:
        if i in stack:
            return False
        else:
            stack.append(i)

    return True

  
print(is_unique([1, 2, 3, 4]))
print(is_unique([1, 2, 3, 4, 4]))