# Problems taken from https://sites.google.com/site/prologsite/prolog-problems/1
# Second round - Add exceptions

#01 Find the last element of a list
def last_element(some_list):
	return some_list[-1]

#02 Find the last but one element of a list
def last_but_one(some_list):
	return some_list[-2]

#03 Find the k'th element of a list (0 index)
def k_element(some_list, k):
	return some_list[k]

#04 Find the number of elements in a list
def length_list(some_list):
	return len(some_list)

#05 Reverse a list
def reverse_list(some_list):
	return list(reversed(some_list))

#06 Find out if a list is a palindrome
def palindrome(some_list):
	return reverse_list(some_list) == some_list

#07 Flatten a nested list - doesn't work for ints not in a list
def flatten(some_list):
	return [item for inner_list in some_list for item in inner_list]

#08 Eliminate consecutive duplicates of list elements
#09 Pack consecutive duplicates of list elements into sublists
#10 Run Length encoding of a list 
#11 Modified run length encoding
#12 Decode a run length encoded list
#13 Run Length encoding of a list (direct solution)
#14 Duplicate the elements of a list
#15 Duplicate the elements in a list a given number of times
#16 Drop every Nth element from a list
#17 Split a list into two parts, the length of the first part is given
#18 Extract a slice from a list
#19 Rotate a list N places to the left
#20 Remove the Kth element from a list
#21 Inset an element at a given position into a list
#22 Create a list containing all integers within a given range
#23 Extract a number of randomly selected elements from a list
#24 Lotto: Draw N different random numbers from the set 1..M
#25 Generate a random permutation of the elements of a list
#26 Generate the combinations of K distinct objects chosen from the N elements of a list
#27 Group the elements of a set into disjoint subsets
#28 Sorting a list of lists according to length of sublists

test_list = [1, 2, 3, 4]
palindrome_list = ['a', 'n', 'n', 'a']
nested_list = [[1, 2], 'z', test_list, palindrome_list]

if __name__ == "__main__":
    print "Exercise #01:" ,
    print last_element(test_list) == 4
    print "Exercise #02:" ,
    print last_but_one(test_list) == 3
    print "Exercise #03:" ,
    print k_element(test_list, 0) == 1
    print "Exercise #04:" ,
    print length_list(test_list) == 4
    print "Exercise #05:" ,
    print reverse_list(test_list) == [4, 3, 2, 1]
    print "Exercise #06:" ,
    print palindrome(palindrome_list)
    print "Exercise #07:" ,
    print flatten(nested_list) == [1, 2, 'z', 1, 2, 3, 4, 'a', 'n', 'n', 'a']
    #print "Exercise #08:" ,
    #print "Exercise #09:" ,
    #print "Exercise #10:" ,
    #print "Exercise #11:" ,
    #print "Exercise #12:" ,
    #print "Exercise #13:" ,
    #print "Exercise #14:" ,
    #print "Exercise #15:" ,
    #print "Exercise #16:" ,
    #print "Exercise #17:" ,
    #print "Exercise #18:" ,
    #print "Exercise #19:" ,
    #print "Exercise #20:" ,
    #print "Exercise #21:" ,
    #print "Exercise #22:" ,
    #print "Exercise #23:" ,
    #print "Exercise #24:" ,
    #print "Exercise #25:" ,
    #print "Exercise #26:" ,
    #print "Exercise #27:" ,
    #print "Exercise #28:" ,
