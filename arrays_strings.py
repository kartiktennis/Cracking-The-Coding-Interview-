#Solutions to Cracking the Coding Interview - Chapter 1 (Arrays & Strings)

#Implement algorithm to heck if a string has all unique characters - optimize to not use any additional data structures
def isUnique(string): 
    for i in range (0, len(string)):
        for j in range (i+1, len(string)):
            if string[i] is string[j]:
                return False
    return True


def checkPermutation(s1, s2):
    # 1) must be same length
    # 2) characters in strings must be same and same # of occurences of each
    # 3) order within string does not matter as long as 1) and 2) are met
    # NOTE: Key - this is pretty basic but I always forget - strings CAN BE SORTED just like normal


    s1_sorted = ''.join(sorted(s1))
    s2_sorted = ''.join(sorted(s2))
    print (s1_sorted)
    print (s2_sorted)
    if s1_sorted == s2_sorted:
        return True
    else:
        return False

def URLify(string, true_length):
    # "Mr John Smith      " - true length is 13 (non space chars)
    # Actual length of input string is true_length + (# of spaces*3)






