import re
import os 
import glob
import csv

path=os.getcwd()
target = 'Training-Set-2018/'

entries = os.listdir(target)

for entry in entries:
	if entry == 'FilterSent':
		continue
	temPath = path+'/'+target+entry+'/annotation/'
	print(temPath)
	temPath2 = glob.glob(temPath+'*ann*.txt')[0]
	print(temPath2)
	filename = temPath2.split('/')[-1]
	print(temPath2)
	print(filename)

	# print(inputFile)
	outpath = temPath+filename.rstrip(".txt") + ".csv"
	print(outpath)
	lst = open(temPath2).readlines()

	# for line in lst:
	# 	out=''
	# 	if line !='\n':
	# 		element=line.split('|')
	# 		value = element[6].split('</S><S')

	# 		for sent in value:
	# 			if sent != '':
	# 				finalSent = sent.split('>')[1].rstrip('</S>')
	# 				out=out+finalSent

	# 	print(out)


	cnt=1
	with open(outpath,'w', newline = '')as f:
		thewriter = csv.writer(f)
		listRow = ['id', 'sentence']
		thewriter.writerow(listRow)
		for line in lst:
			out=''
			if line =='\n':
				continue

			element=line.split('|')
			value = element[6].split('</S><S')

			for sent in value:
				if sent != '':
					finalSent = sent.split('>')[1].rstrip('</S>')
					out=out+finalSent

			print(out)
			thewriter.writerow([cnt,out])
			cnt=cnt+1