import os
import sys
import re
import matplotlib.pyplot as plt


def search_directory(root_dir, keyword):
    '''performs dfs search on a directory searching for files
       that contain a keyword and returns the count'''
    res = {}
    for root, dirs, files in os.walk(root_dir):
        count = 0
        for f in files:
            if re.compile(keyword).search(f):
                count += 1
        res[root] = count

    return res


def barplot(d):
    '''plots a bar graph, input is a dictionary'''
    plt.bar(range(len(d)), d.values(), align="center")
    plt.xticks(range(len(d)), list(d.keys()))
    plt.show()


def main():
    data = search_directory(sys.argv[1], sys.argv[2])
    print(data)
    barplot(data)


if __name__ == '__main__':
    main()
