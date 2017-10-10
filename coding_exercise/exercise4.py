# Here is a tricky exercise.Then create a script that merges the three text files into a new text file containing the text of       all three files. The filename of the merged text file should contain the current timestamp down to the millisecond level.   E.g. "2016-06-01-13-57-39-170965.txt".
# You have some tips in the next lecture and the solution in the lecture after that.

import glob2
import datetime

file_list = ['file1.txt', 'file2.txt', 'file3.txt']
file_name = datetime.datetime.now();

print(file_name)