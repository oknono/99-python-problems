# Find last but one element from a list
def last_but_one(some_list):
    try:
        return some_list[-2] 
    except IndexError:
        return None

if __name__ == "__main__":
    print "last but one of [] is " +  str(last_but_one([]))
    print "last but one of [1] is " + str(last_but_one([1]))
    print "last but one of [1, 2, 'b', 3] is " +  str(last_but_one([1, 2, 'b', 3])) 
