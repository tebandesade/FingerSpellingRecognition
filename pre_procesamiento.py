import sklearn as sk
import os
import numpy as np


def create_dictionary(datadir,letter,data):
    rta = os.path.join(datadir,data)
    if ('color') in data:
        if letter in dictionary_alfabet_nd.keys():
            dictionary_alfabet_nd[letter].append(rta)
            input_data.append(rta)
            label_data.append(letter)
        else:
            dictionary_alfabet_nd[letter] = []
            dictionary_alfabet_nd[letter].append(rta)
            input_data.append(rta)
            label_data.append(letter)
    if ('depth') in data:
        if letter in dictionary_alfabet_depth.keys():
            dictionary_alfabet_depth[letter].append(rta)
            input_data_depth.append(rta)
            label_data_depth.append(letter)
        else:
            dictionary_alfabet_depth[letter] = []
            dictionary_alfabet_depth[letter].append(data)
            input_data_depth.append(rta)
            label_data_depth.append(letter)
            
def run_letter_path(datadir,letter, directory):
    for data in directory:
        create_dictionary(datadir,letter,data)


head = '../secondtakeasl/fingerspelling5/dataset5'
dataset = os.listdir(head)
dictionary_alfabet_nd = {}
dictionary_alfabet_depth = {}
input_data =[]  atadir,line,letter_files)

valores_color = []
for k, v in dictionary_alfabet_nd.items():
    tam = len(v)
    valores_color.append(tam)

min_valores = np.min(valores_color)
test_set_size = int(min_valores* 0.3)
np.random.seed(42)

train_indexes_color = {}
test_indexes_color = {}
train_set = []
test_set  = []

for k,v in dictionary_alfabet_nd.items():
    indices_aleatorios = np.random.permutation(min_valores)
    train_indexs = indices_aleatorios[test_set_size:]
    test_indexs  =indices_aleatorios[:test_set_size]
    train_indexes_color[k] = train_indexs
    test_indexes_color[k] = test_indexs
    for index in train_indexs:
        train_set.append((v[index],k))
    for index in test_indexs:
        test_set.append((v[index],k))

np.save('train_set',train_set)
np.save('test_set',test_set)