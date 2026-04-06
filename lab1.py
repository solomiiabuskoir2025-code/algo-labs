import random


def find_k_largest(arr, k):
    if k <= 0 or k > len(arr):
        raise ValueError("k have to be within the array")

    arr_copy = arr[:]
    target_index = len(arr_copy) - k

    def quickselect(left, right):
        pivot_index = random.randint(left, right)
        pivot_value = arr_copy[pivot_index]


        arr_copy[pivot_index], arr_copy[right] = arr_copy[right], arr_copy[pivot_index]

        store_index = left

        for i in range(left, right):
            if arr_copy[i] < pivot_value:
                arr_copy[i], arr_copy[store_index] = arr_copy[store_index], arr_copy[i]
                store_index += 1


        arr_copy[store_index], arr_copy[right] = arr_copy[right], arr_copy[store_index]

        if store_index == target_index:
            return arr_copy[store_index]
        elif store_index < target_index:
            return quickselect(store_index + 1, right)
        else:
            return quickselect(left, store_index - 1)

    value = quickselect(0, len(arr_copy) - 1)

    index = arr.index(value)

    return value, index