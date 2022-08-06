import re
s = input("String: ")
find = re.search("[A-Z0-9]{5}[-]{1}[A-Z0-9]{5}[-]{1}[A-Z0-9]{5}[-]{1}[A-Z0-9]{5}", s)
if find:
    print("Match")
else:
    print("Doesn't Match")