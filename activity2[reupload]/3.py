# Write your solution for algorithm 3 below
# Write an algorithm that takes in an unsorted numerical list as an argument and 
# creates a new sorted list in descending order (use the sorted() function).
#The sorted() function sorts in ascending order, but it can sort in descending 
# order by adding a reverse parameter with a boolean value of True.
lst = [48,25,1,-1,25,47,65,32,12,11,13]
print(f"unsorted: {lst}")
lst = sorted(lst, reverse=True)
print(f"descending order: {lst}")