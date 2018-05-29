import numpy as np 
import cv2 

np_descriptros = 'train_descriptors.npy'

descriptors = np.load(np_descriptros)
dictionarySize = 100	
BOW = cv2.BOWKMeansTrainer(dictionarySize)

for i in  descriptors:
	BOW.add(i)

dictionary = BOW.cluster()

out = 'cluster'+ str(dictionarySize)+'dict'
np.save(out,dictionary)
	