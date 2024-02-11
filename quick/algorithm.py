def quick_sort(l):
    _quicksort(l, low=0, hi=len(l) - 1)
    return l


def _partition(l, low, hi):
    pivot = l[hi]
    i = low - 1
    for j in range(low, hi - 1):
        if l[j] <= pivot:
            i = i + 1
            l[i], l[j] = l[j], l[i]
    i = i + 1
    l[i], l[hi] = l[hi], l[i]
    return i


def _quicksort(l, low, hi):
    if low >= hi or low < 0:
        return
    p = _partition(l, low, hi)
    _quicksort(l, low, p - 1)
    _quicksort(l, p + 1, hi)
