# A palindromic number reads the same both ways. The largest palindrome made from the product of
# two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.



# 100*100 = 10000
# 999 * 999 = 998001
def is_palindrome(x):
    x = str(x)

    for i in range(len(x)//2):
        if x[i] == x[-i-1]:
            continue
        else:
            return False
    return True

print(is_palindrome(909))
print(is_palindrome(8008))
print(is_palindrome(11))
print(is_palindrome(111))
print(is_palindrome(202202))


def largest_palindrome(n):

        h = 10**n - 1
        l = 10**(n-1)
        s = []

        while len(s) < 3:
            for i in range(h, l, -1):
                for j in range(h, i -1, -1):
                    p = i * j

                    print(str(i) + " * " + str(j) + " = " + str(p) )

                    if is_palindrome(p):
                        s.append(p)

        return max(s)

print(largest_palindrome(2))




