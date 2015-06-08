#08 Eliminate consecutive duplicates of list elements
def eliminate_cons(some_list):
	check = None
	new_list = []
	for element in some_list:
		if element != check:
			new_list.append(element)
		check = element
	return new_list

if __name__ == "__main__":
    l = ['a', 'a', 'b', 'c', 'c', 'c', 'c', 'a']
    print l 
    print eliminate_cons(l)

