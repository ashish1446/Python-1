# -*- coding: utf-8 -*-
"""w6ppa5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qDp_xCQFg55Y4auGSqR4U_y7leAamKVT
"""

def dict_to_list(D):
    L = []
    for x in D:
        L.append((x,D[x]))
    return L

    '''def dict_to_list(D):
    L = D.items()
    return L 
    '''


def list_to_dict(L):
    D= {}
    for x in L:
        D[x[0]] = x[1]
    return D

D ={'ashish':1446, 'aswin':1446}
dict_to_list(D)

L = [('ashish', 1446), ('aswin', 1446)]
list_to_dict(L)