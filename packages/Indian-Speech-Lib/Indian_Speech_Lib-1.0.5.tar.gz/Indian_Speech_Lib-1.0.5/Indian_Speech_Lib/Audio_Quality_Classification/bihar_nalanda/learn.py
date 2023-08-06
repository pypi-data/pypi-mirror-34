import numpy as np
import csv
import soundfile as sf
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
from statistics import mean, stdev

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
import pickle


def train_model(train_file, test_file):
	'''
	train_file is csv for training, test_file is unseen csv data
	'''	
	rows = []
	with open(train_file, 'r') as csvfile:
		csvreader = csv.reader(csvfile)
		fields = csvreader.next()
		for row in csvreader:
			if int(row[137])<3:
				rows.append(row)

	rows1=[]
	with open(test_file, 'r') as csvfile:
		csvreader = csv.reader(csvfile)
		fields = csvreader.next()
		for row in csvreader:
			if  int(row[137])<3:
				rows1.append(row)

	rows = np.array(rows)
	rows1 = np.array(rows1)
	X_train1, X_val, y_train1, y_val = train_test_split(rows[:,0:137],rows[:,137], random_state=0, test_size=0.2)
	X_train, X1, y_train, y1 = train_test_split(X_train1,y_train1, random_state=0, test_size=0.25)
	scaler = StandardScaler()
	scaler.fit(X_train)
	X_train = scaler.transform(X_train)
	X_val = scaler.transform(X_val)
	
	X1 = scaler.transform(X1)
	X3 = scaler.transform(rows1[:,0:137])

	#Train support vector machine model

	svm = SVC(C=2, gamma = 0.03).fit(X_train, y_train) 
	#print("Support Vector Machine")
	print("Accuracy on training set: {:.3f}".format(svm.score(X_train, y_train)))
	print("Accuracy on test set: {:.3f}".format(svm.score(X_val, y_val)))
	print("Accuracy on test set: {:.3f}".format(svm.score(X1, y1)))
	print("Accuracy on test set: {:.3f}".format(svm.score(X3, rows1[:,137])))
	#x1 = svm.predict(X_test)
	#x2 = svm.predict(X1)
	#x3 = svm.predict(X3)
	#results1 = confusion_matrix(y_test,x1)
	#results2 = confusion_matrix(y1,x2)
	#results3 = confusion_matrix(rows1[:,137],x3)
	#print(results1)
	#print(results2)
	#print(results3)
	
	#save model now
	filename = 'accept_reject'
	pickle.dump(svm, open(filename, 'wb'))	
#***************************************************************------------------------------------------------------------****************************************************
