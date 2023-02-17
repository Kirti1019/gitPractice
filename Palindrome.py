# By  using split
# def palindrome(s):
#     new_s = s[::-1]
#     if s == new_s:
#         print("Yes, it's a Palindrome")
#     else:
#         print("It's Not a Palindrome")

# # by using loop
# def palindrome(s):
#     n = len(s)
#     for i in range(n):
#         if s[i] != s[n - i - 1]:
#             return False
#         return True

# By using reversed and join
# def palindrome(s):
#     temp = ''.join(reversed(s))
#     if s == temp:
#         return True
#     return False

# By using while loop
# def palindrome(s):
#     n = len(s)
#     first = 0
#     last = n - 1
#     while first < last:
#         if s[first] == s[last]:
#             first += 1
#             last -= 1
#         else:
#             return False
#         return True

# palindrome for number
def palindrome(n):
    temp = n  # 122
    rev_n = 0
    while (temp > 0):
        digit = temp % 10  # digit madhe remainder milel i.e 2
        rev_n = rev_n * 10 + digit  # 0*10+2 = 2
        temp = temp // 10   # ithe decimal point chya adhi chi divvision milte i.e. 12

    if n == rev_n:
        return True
    return False


# str = 'nitin'
# print(palindrome(str))

num = 122
print(palindrome(num))
