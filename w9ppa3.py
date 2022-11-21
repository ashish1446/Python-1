# -*- coding: utf-8 -*-
"""w9ppa3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eTf40H_w8PbZPLGnuNFsmXYe68Q_fzN0
"""

def get_max_line(filename):
    """
    Get the line that houses the maximum value

    Argument:
        filename: string, path to the file
    Return:
        result: integer
    """

    f = open(filename,'r')
    line_no = 0
    count  = 0 
    max = -9999


    for line in f:
        #print('a', end = ',')

        line = line.strip()
        if line.isnumeric():
            n = int(line)
            if n > max:
                max = n
    #print('ashish')
    f.close()

    f = open(filename,'r')

    for b in f:
        #print('b', end = ',')
        line_no += 1 
        b = b.strip()
        if b.isnumeric():
            if int(b) == max:
                break
    f.close()

    return line_no
print(get_max_line('new.txt'))

