"""
april 29th 2023

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, 
return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""
def autocomplete(set, string):
    new_set = []
    for word in set:
        if word[:len(string)] == string:
            new_set.append(word)
    
    return new_set

set = ["dog", "deer", "deal"]
string = "de"
print(autocomplete(set, string))