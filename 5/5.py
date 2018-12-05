MAGIC_NUMBER = 42
arr = [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]


def recursive_find_magic_numbers(arr, index, acc, next_el=None):
    if not next_el:
        next_el = arr[index]

    if index > 0:
        index -= 1
        recursive_find_magic_numbers(arr, index, acc + next_el)
        recursive_find_magic_numbers(arr, index, acc - next_el)
        recursive_find_magic_numbers(arr, index, acc, int(str(arr[index]) + str(next_el)))
    else:
        acc += next_el
        if acc == MAGIC_NUMBER:
            global count
            count += 1


count = 0
arr_len = len(arr) - 1
recursive_find_magic_numbers(arr, arr_len, 0)
print(count)
