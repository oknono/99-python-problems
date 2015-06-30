# Flatten a nested list 
# This method does not work for a singleton integer
# https://wiki.python.org/moin/ProblemSets/99%20Prolog%20Problems%20Solutions#Problem_7:_Flatten_a_nested_list_structure

def flatten(some_list):
    return [item for inner_list in some_list for item in inner_list]

if __name__ == "__main__":
    print "flatten([ [1,2], [1,2,3,4]]) : {0}".format(flatten([ [1,2], [1,2,3,4]]))
    print "flatten(['a', ['a', 'b'], 'c', [1]]): {0}".format(flatten(['a', ['a', 'b'], 'c', '1']))
    #print "flatten([ 1, [ 2, 3], 4, [1]]): {0}".format(flatten([ 1, [ 2, 3], 4, [1]]))