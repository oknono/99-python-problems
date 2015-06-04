# Find the last element of a list

def last_element(some_list):
    try:   
        return some_list[-1]
    except IndexError:
        return None

if __name__ == "__main__":
    print "Last element of [] is " + str(last_element([]))
    print "Last elememt of [1] is " + str(last_element([1]))
    print "Last element of ['a', 'b', 'c'] is " + str(last_element(['a', 'b', 'c']))
