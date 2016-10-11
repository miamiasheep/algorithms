import random
from quicksort import my_qsort
def test_qsort():
    for i in range(10):
        input_list = random.sample(range(1000000), 10000)
        ans = sorted(input_list)
        my_qsort(input_list)
        # print 'input_list: {}'.format(input_list)
        # print 'ans: {}'.format(ans)
        assert input_list == ans 
    print 'complete!'

if __name__ == '__main__':
    test_qsort()
    
