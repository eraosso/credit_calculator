# the variable "args" is already defined
from typing import List

my_list = []  # your code here
import sys
# arg = sys.argv
arg = args
for i in range(len(arg) - 1):
    my_list.append(int(arg[i+1]))
print(my_list)

# further code of the script "process_four_numbers.py"