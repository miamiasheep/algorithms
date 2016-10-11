def swap(l, i, j):
    l[i], l[j] = l[j], l[i]

    
def my_qsort(input_list):
    my_qsort_helper(input_list, 0, len(input_list) - 1)


def my_qsort_helper(in_list, left, right):
    if right - left < 1:
        return
    pv_index = left 
    pivot = in_list[pv_index]
    swap(in_list, pv_index, right)
    l = left
    for i in range(left, right):
        if in_list[i] < pivot:
            swap(in_list, i, l)
            l += 1
    swap(in_list, l, right)
    my_qsort_helper(in_list, left, l - 1)
    my_qsort_helper(in_list, l + 1, right)


if __name__ == '__main__':
    input_list = [3, 2, 5, 1, 4]
    print 'before sort: {}'.format(input_list)
    my_qsort(input_list)
    print 'after sort: {}'.format(input_list)
