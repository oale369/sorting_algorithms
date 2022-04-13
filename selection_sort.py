# @author Alexandre Oliveira
# Exemplo de uso do selection_sort

from timing import timed_func
import random


@timed_func
def selection_sort(items):
    for i in range(len(items)):
        min_idx = i
        for j in range(i + 1, len(items)):
            if items[min_idx] > items[j]:
                min_idx = j
                items[i], items[min_idx] = items[min_idx], items[i]

    return items


if '__main__' == __name__:
    items = [15, 21, 13, 9, 7, 1]

    print(items)
    selection_sort(items)
    print(items)