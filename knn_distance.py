import random


def knn_distance(arr, q, k):
    target = k - 1

    def dist(x):
        return abs(x - q)

    def quickselect(left, right):
        if left >= right:
            return

        pivot_idx = random.randint(left, right)
        arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
        pivot_dist = dist(arr[right])

        store = left
        for i in range(left, right):
            if dist(arr[i]) < pivot_dist:
                arr[store], arr[i] = arr[i], arr[store]
                store += 1

        arr[store], arr[right] = arr[right], arr[store]

        if store == target:
            return
        elif store < target:
            quickselect(store + 1, right)
        else:
            quickselect(left, store - 1)

    quickselect(0, len(arr) - 1)

    kth_point = arr[target]
    return (dist(kth_point), kth_point)
