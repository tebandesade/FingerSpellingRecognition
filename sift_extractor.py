import sklearn as sk
import os
import numpy as np
import cv2
import matplotlib.pyplot as plt


def generate_descriptors(set_):
    descriptors = []
    descriptors_labels = []
    for im in set_:
        path_img = im[0]
        label    = im[1]
        im_load  = cv2.imread(path_img)
        key_p, descrip =sift.detectAndCompute(im_load,None)
        descriptors.append(descrip)
        descriptors_labels.append(label)
        
    return descriptors, descriptors_labels

def getSetDescriptors(set_):
	descriptores, etiquetas = generate_descriptors(set_)
	#descriptores_concatenados = [ele for sub in descriptores for ele in sub]
	return descriptores, etiquetas
	
train_set = np.load('train_set.npy')
test_set = np.load('test_set.npy')

sift = cv2.xfeatures2d.SIFT_create()

descriptores_train , etiquetas_train = getSetDescriptors(train_set)

descriptores_test , etiquetas_test = getSetDescriptors(test_set)

np.save('train_descriptors',descriptores_train)
np.save('trainlabel_descriptors',etiquetas_train)

np.save('test_descriptors',descriptores_test)
np.save('testlabel_descriptors',etiquetas_test)