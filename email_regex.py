import os
import re
s = input("String: ")
find = re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", s)

if find:
    print("Match")
else:
    print("Doesn't Match")


os.system("pause")