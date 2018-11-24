# FingerSpellingRecognition

Pipeline  to implement baseline: Recognition based on SIFT 


1.


El archivo pre_procesamiento.py crea el test y train set

 
The pre_procesamineto.py script creates the test and train set (train_set.npy,test_set.npy)


2.


Se sacan los sift features utilizando el archivo sift_extractor.py y se obtiene los descriptores


SIFT features, along its descriptors, are extracted with the sift_extractor.py script 


3.

 	
Se construye diccionario de imagenes con el archivo bow_cluster.py


The visual word vocabulary ( 100 words) is created with the bow_cluster.py script


4.


Se configura el diccionario de bow con los descriptores y se entrena el clasificador SVM con train y evalua en test con el archivo bow_config.py


The dictionary is configured with the bow descriptors and a SVM classifier is trained with the train set and evaluates with the test set with the bow_config.py script

