def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def can_place_cows(stalls, cows, dist):
    count = 1
    last_pos = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - last_pos >= dist:
            count += 1
            last_pos = stalls[i]
            if count == cows:
                return True
    return False

def aggressive_cows(stalls, cows):
    stalls = quick_sort(stalls)
    left = 1
    right = stalls[-1] - stalls[0]
    best = 0

    while left <= right:
        mid = (left + right) // 2
        if can_place_cows(stalls, cows, mid):
            best = mid
        else:
            right = mid - 1
    return best
