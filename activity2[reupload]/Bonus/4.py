# Write your solution for algorithm 4 below
# Write an algorithm that takes in a string and sorts the words 
# in the string in alphabetical order. The comparison should be case-insensitive.
strg = "I love software engineering"
print(f"input: {strg}")
sortedStrings = sorted(strg.split(), key = str.lower)
print(f"alphabetical sort: {sortedStrings}")