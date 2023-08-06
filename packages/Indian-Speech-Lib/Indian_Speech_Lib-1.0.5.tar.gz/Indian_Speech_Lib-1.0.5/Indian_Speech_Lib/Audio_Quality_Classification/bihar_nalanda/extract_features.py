from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
from statistics import mean, stdev
import numpy as np
import csv
import timeit
import soundfile as sf


def get_features(input_file):
	'''
	Given an input .wav file, this function will return a list of lists corresponding to features of each of its chunks
	reject is 1
	accept is 2;
	we will not append any target label and just use svm_score to get accept(2) or reject(1)
	here there is no need to break into chunks; this was required when time was a priority
	'''
	data, samplerate = sf.read(input_file)
	l1 = []
	[Fs, x] = audioBasicIO.readAudioFile(input_file)
	F = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.05*Fs, 0.025*Fs)
	k = 0
	while k < len(F[0]):
		l = []
		for j in range(34):
			l.append(np.percentile(F[j, k:k+399], 25))
			l.append(np.percentile(F[j, k:k+399], 50))
			l.append(np.percentile(F[j, k:k+399], 75))
			l.append(np.percentile(F[j, k:k+399], 95))
		l.append(len(F[j])/399)
		l.append(1)	#default label is reject
		l1.append(l)
		k = k + 399
	return l1
#******************************************************-----------------------------------------------------------------------*************************************************
	
def generate_data(output_csv):
	'''
	This function will read in the entire liste of audio files and extract features from them and append to output_csv
	'''
	l1=[]
	for i in range(501, 1501, 1):
		try:
			[Fs, x] = audioBasicIO.readAudioFile("rej_" + str(i) + ".wav")
			F = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.05*Fs, 0.025*Fs)
		except:
			continue
		k = 0
		while k<len(F[0]):
			l = []
			for j in range(34):
				l.append(np.percentile(F[j, k:k+399], 25))
				l.append(np.percentile(F[j, k:k+399], 50))
				l.append(np.percentile(F[j, k:k+399], 75))
				l.append(np.percentile(F[j, k:k+399], 95))
			
			l.append(len(F[j])/399)
			l.append(1)
			l1.append(l)
			k = k + 399
	for i in range(501, 1501, 1):
		try:
			[Fs, x] = audioBasicIO.readAudioFile("acc_" + str(i) + ".wav")
			F = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.05*Fs, 0.025*Fs)
		except:
			continue
		k = 0
		while k < len(F[0]):
			l = []
			for j in range(34):
				l.append(np.percentile(F[j, k:k+399], 25))
				l.append(np.percentile(F[j, k:k+399], 50))
				l.append(np.percentile(F[j, k:k+399], 75))
				l.append(np.percentile(F[j, k:k+399], 95))
			
			l.append(len(F[j])/399)
			l.append(2)
			l1.append(l)
			k = k + 399

	with open(output_csv, "w") as f:
		writer = csv.writer(f)
		writer.writerows(l1)
#******************************************************-----------------------------------------------------------------------**************************************************
