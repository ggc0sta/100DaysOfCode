import pandas as pd
file1 = pd.read_table("file1.txt", header=None, names=["n"])
list1 = file1["n"].to_list()
file2 = pd.read_table("file2.txt", header=None, names=["n"])
list2 = file2["n"].to_list()

result = [num for num in list1 if num in list2]

print(list1)
print(list2)

print(result)


