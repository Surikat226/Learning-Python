# Не дописал

sorted_numbers = [-97, -56, -34.6, -4, -1, 0, 1, 13, 15, 26, 43, 67, 79, 94]

def search_for_elem(lst, elem):
    low = 0
    high = len(sorted_numbers) - 1

    while low < high:
        middle = (low + high) // 2
        if lst[middle] < elem:
            low = middle + 1
        else:
