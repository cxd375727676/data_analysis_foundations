#读取多个文本文件，如files文件夹中的文件
import sys
import os
import glob

filespath=sys.argv[1]
for filepath in glob.glob(os.path.join(filespath, "*.txt")):
    with open(filepath,"r") as f:
        for row in f:
            print(row.strip())