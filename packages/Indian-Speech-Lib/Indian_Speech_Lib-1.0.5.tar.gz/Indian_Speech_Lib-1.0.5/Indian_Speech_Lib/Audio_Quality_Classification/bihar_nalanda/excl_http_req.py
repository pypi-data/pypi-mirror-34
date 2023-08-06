import urllib2
import xlrd
import os
from subprocess import Popen

def get_audio_from_url(input_url, output_file):
	'''
	Given an audio url, this function will fetch it and generate an mp3 file for it;
	output_file should be a proper name for an mp3, i.e. ending with .mp3
	'''
	mp3file = urllib2.urlopen(input_url)
	FP = open(output_file, 'wb')
	FP.write(mp3file.read())
	FP.close()
#*****************************------------------------------------*******************************	

def get_audio_from_excel(input_file = 'bihar_nalanda_Item_data-all.xlsx'):
	ExcelFileName = input_file
	workbook = xlrd.open_workbook(ExcelFileName)
	worksheet = workbook.sheet_by_name("bmgf_item_data_v5")
	num_rows = worksheet.nrows #Number of Rows
	num_cols = worksheet.ncols #Number of Columns
	c=0
	for curr_row in range(0,num_rows, 1):
		state = worksheet.cell_value(curr_row, 2)
		tag = worksheet.cell_value(curr_row, 9)
		if state!='REJ':
			c+=1
		if c==1501:
			break
		if state!='REJ':
			s1 = worksheet.cell_value(curr_row,3)
			print(s1)
			if not s1.endswith('.mp3'):
				c = c-1
				continue
			mp3file = urllib2.urlopen(s1)
			with open('acc_'+str(c)+'.mp3','wb') as output:
				output.write(mp3file.read())
			filename = 'acc_'+str(c)+'.mp3'
			[idn,idn1] = filename.split('.')
			p = Popen(['ffmpeg -i '+filename+' -acodec pcm_s16le -ac 1 -ar 16000 '+idn+'.wav'.format(filename)], shell = 'True')
			p.wait()
	c=0
	for curr_row in range(0,num_rows, 1):
		state = worksheet.cell_value(curr_row, 2)
		tag = worksheet.cell_value(curr_row, 9)
		if state=='REJ':
			c+=1
		if c==1501:
			break
		if state=='REJ':
			s1 = worksheet.cell_value(curr_row,3)
			print(s1)
			if not s1.endswith('.mp3'):
				c = c-1
				continue
			mp3file = urllib2.urlopen(s1)
			with open('rej_'+str(c)+'.mp3','wb') as output:
				output.write(mp3file.read())
			filename = 'rej_'+str(c)+'.mp3'
			[idn,idn1] = filename.split('.')
			p = Popen(['ffmpeg -i '+filename+' -acodec pcm_s16le -ac 1 -ar 16000 '+idn+'.wav'.format(filename)], shell = 'True')
			p.wait()
#*****************************------------------------------------*******************************	
