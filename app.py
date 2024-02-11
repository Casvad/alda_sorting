import sys

from base.base import BaseSortingTimeGather
from heap.algorithm import heap_sort
from merge.algorithm import merge_sort
from quick.algorithm import quick_sort

if __name__ == "__main__":
    base_gather = BaseSortingTimeGather([merge_sort, quick_sort, heap_sort])
    table = base_gather.take_execution_time(1000, 10000, 50, 5)
    for row in table:
        print(row)
