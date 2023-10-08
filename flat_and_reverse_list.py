# 1. Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir.

list1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flatten_list = []
def flat_list(x):
    for i in x:
        if type(i) == list:
            flat_list(i)
        else:
            flatten_list.append(i)
    return flatten_list

print(flat_list(list1))


# 2. Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.

list3 = [[1, 2], [3, 4], [5, 6, 7]]

flatten_list = []
def flat_list(x):
    for i in x:
        if type(i) == list:
            flat_list(i)
        else:
            flatten_list.append(i)
    return flatten_list

list3 = flat_list(list3)
list3.reverse()
print(list3)