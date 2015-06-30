# Find the number of elements in a list

def num_elem(some_list):
    return len(some_list)

if __name__ == "__main__":
    print "len of [] is {0}".format(num_elem([]))
    print "len of [1, 'a'] is {0}".format(num_elem([1, 'a']))
    print "len of [[1, 2, 3, 4], 'a'] is {0}".format(num_elem([[1, 2, 3, 4], 'a']))
