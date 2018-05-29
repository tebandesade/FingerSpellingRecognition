import cv2
import numpy as np
from sklearn import svm as Support
x = np.load('cluster100dict.npy')
sift = cv2.xfeatures2d.SIFT_create()
sift2 = cv2.xfeatures2d.SIFT_create()
train_set = np.load('train_set.npy')

bowDiction = cv2.BOWImgDescriptorExtractor(sift2, cv2.BFMatcher(cv2.NORM_L2))
bowDiction.setVocabulary(x)

bow_train = []
bow_label = []
for (t, l)in (train_set):
    im_load  = cv2.imread(t)
    ret = bowDiction.compute(im_load, sift.detect(im_load))
    bow_train.append(ret)
    bow_label.append(l)

np.save( 'bow_train_100', np.array(bow_train))
np.save('bow_label_100', np.array(bow_label))
copy_reshape = np.array(bow_train).reshape(len(bow_label),100)
svm = Support.LinearSVC(C=4)
svm.fit(copy_reshape,bow_label)

test_set = np.load('test_set.npy')	
train_set = np.load('train_set.npy')

predicted_test= []
real_test = [] 

for (i, et) in (test_set):
    im_load  = cv2.imread(i)
    ret = bowDiction.compute(im_load, sift.detect(im_load))
    p = svm.predict(ret)
    predicted_test.append(p)
    real_test.append(et)

predicted_train= []
real_train = [] 

for (i, et) in (train_set):
    im_load  = cv2.imread(i)
    ret = bowDiction.compute(im_load, sift.detect(im_load))
    p = svm.predict(ret)
    predicted_train.append(p)
    real_train.append(et)

def get_score(real,pred):
	correct = 0 
	for (r,f) in zip(real,pred):
		if r==f:
			correct +=1 
	acc = correct/len(real)
	print(acc)


print("test score")
get_score(real_test,predicted_test)

print("train score")
get_score(real_train,predicted_train)


