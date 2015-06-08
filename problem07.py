# Flatten a nested list 
# This method does not work for a singleton integer

def flatten(some_list):
    return [item for inner_list in some_list for item in inner_list]

if __name__ == "__main__":
    print "flatten([ [1,2], [1,2,3,4]]) :",
    print flatten([ [1,2], [1,2,3,4]])
    print "flatten(['a', ['a', 'b'], 'c', [1]]):",
    print flatten(['a', ['a', 'b'], 'c', '1'])