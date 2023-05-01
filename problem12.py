"""
may 1st 2023

This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""
def longest_substring(string, k):
    longest = ""
    for x in range(len(string)):
        current = ""
        characters = {}
        for n in range(x, len(string)):
            if string[n] in characters or len(characters) < k:
                current += string[n]
                characters[string[n]] = characters.get(string[n], 0) + 1
            else:
                break
            if len(current) > len(longest):
                longest = current
               
    return len(longest), longest

s = "abcba"
k = 2
print(longest_substring(s, k))

s = "ajsuiqgriuibwefjkhvbndhfbveiurfnhjebfhiwebgheqrbgfqhecjkdsbfvhwergiuebvwher"
k = 5
print(longest_substring(s, k))