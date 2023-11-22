def merge_sort(array):
    if len(array) == 1:
        return [array[0]]

    array1, array2 = array[:(len(array) // 2)], array[(len(array) // 2):]
    result1, result2 = merge_sort(array1), merge_sort(array2)

    result = result1.copy()
    pr_i = 0

    for item in result2:
        for i in range(pr_i, len(result)):
            if result[i] > item:
                result.insert(i, item)
                pr_i = i
                break
        else:
            result.append(item)

    return result
