# Find the last element of a list

def last_element(some_list):
    try:   
        return some_list[-1]
    except IndexError:
        return None

if __name__ == "__main__":
    print "Last element of [] is {0} ".format(last_element([]))
    print "Last element of [1, 2, 3, 4] is {0} ".format(last_element([1, 2, 3, 4]))
    print "Last element of ['a', 'b', 'c'] is {0} ".format(last_element(['a', 'b', 'c']))
