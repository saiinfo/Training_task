#delete a file
import os
if os.path.exists("file.txt"):
  os.remove("file.txt")
else:
  print("The file does not exist")

 #compare
import filecmp
f1 = "abc"
f2 = "my data2"
result = filecmp.cmp(f1, f2)
print(result)

result = filecmp.cmp(f1, f2, shallow=False)
print(result)