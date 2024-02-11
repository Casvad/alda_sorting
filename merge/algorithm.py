def merge_sort(l):
    if len(l) <= 1:
        return l
    mid = len(l) // 2
    init_list = l[:mid]
    end_list = l[mid:]

    merge_sort(init_list)
    merge_sort(end_list)
    i, j, k = 0, 0, 0

    while i < len(init_list) and j < len(end_list):
        if init_list[i] <= end_list[j]:
            l[k] = init_list[i]
            i += 1
        else:
            l[k] = end_list[j]
            j += 1
        k += 1
    for i in range(i, len(init_list)):
        l[k] = init_list[i]
        k += 1
    for j in range(j, len(end_list)):
        l[k] = end_list[j]
        k += 1

    return l
