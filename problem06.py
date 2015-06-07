# Found out if a list is a palindrome

import problem05

def palindrome(some_list):
    return problem05.reverse(some_list) == some_list

if __name__ == "__main__":
    print "anana is a palindrome: ",
    print palindrome(['a', 'n', 'a', 'n', 'a'])
    print "banana is a palindrome: ",
    print palindrome(['b', 'a', 'n', 'a', 'n', 'a'])

