# asc
list = ['Max', 'Temel', 'Erik', 'Necmettin']
list.sort()
print(list)

# desc
list = ['Max', 'Temel', 'Erik', 'Necmettin']
list.sort(reverse=True)
print(list)

# Sorting key invidual putting
def get_length(item):
    return len(item)

list.sort(key=get_length)
print(list)

# Making sorting example even more simple..
list.sort(key=len)
print(list)


# Sorting dictionary
d = {'Köln': '1', 'Budapest': '2', 'Istanbul': '3'}
print(sorted(d)) # <-- This sorted create new List, if you before this printing wants


# Sorting dictionary anotherwise
d = {'Köln': '1', 'Budapest': '2', 'Istanbul': '3'}
print(sorted(d, reverse=True))  # <-- This sorted create new List, if you before this printing wants