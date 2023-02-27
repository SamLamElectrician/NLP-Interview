def palindrome(s):
    string=str(s)
    return s== s[::-1]


# considering the best use practical case for this
# This would be the best option as it would be a utility function and not use throughout the entire app. It is very simple to read but does not have the best time/space sitting at O(n).