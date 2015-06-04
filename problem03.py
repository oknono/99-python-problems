# Find the kth element of a list

def find_k_element(some_list, index):
    try:
        return some_list[index - 1]
    except IndexError:
        return None

if __name__ == "__main__":
   print "1th element of [1,2,3,4] is " + str(find_k_element([1, 2, 3, 4], 1))
   print "2nd element of [1,2,3,4] is " + str(find_k_element([1, 2, 3, 4], 2))  
   print "5th element of [1,2,3,4] is " + str(find_k_element([1, 2, 3, 4], 5))   
