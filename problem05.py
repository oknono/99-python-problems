# Reverse a list 
def reverse(some_list):
    return list(reversed(some_list))

if __name__ == "__main__":
    print "reverse [1, 2, 3, 4] : {0}".format(reverse([1, 2, 3, 4]))
    print "reverse [] : {0}".format(reverse([]))
    print "reverse [[1, 2], [3, 4]] : {0}".format(reverse([[1, 2], [3, 4]]))