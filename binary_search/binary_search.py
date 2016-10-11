# implement python binary search

def binary_search(input_list, num):
    return binary_search_helper(input_list, 0, len(input_list) - 1, num)

def binary_search_helper(input_list, start, end, num):
    mid = (start + end) / 2
    if input_list[mid] == num:
	    return mid
    if num > mid:
        binary_search_helper(input_list, mid, end, num)
    else:
        binary_search_helper(input_list, start, mid, num)
        
if __name__ == '__main__':
    input_list = [1,3,5,7,9]
    num = 5
    print 'input_list: {}'.format(input_list)
    print 'num: {}'.format(num)
    print 'ans: {}'.format(binary_search(input_list, num))
	
