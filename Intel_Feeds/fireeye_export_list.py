import sys
import re
import datetime
import csv

############################ GLOBAL VARIABLES  ########################################

ipPattern = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')  # Match IP address RegEx
etpfile = "./alerts.csv"

############################ IMPORT FireEye ETC CVS alerts ##########################




######################## MAIN FUNCTIONA RETURN ETP IMPORTED INFO AS DICTIONARY #############################################
## Alert ID(0),Message ID(1),Date & Time(2),From(3),Recipients(4),Subject(5),Malware Type(6),Malware File Type(7),Malware Name(8),
## Malware MD5(9),Malware Analysis Application(10),Malware Analysis OS(11),Virus Total(12),Source IP(13),Source Country(14),
## Malware Comunication IP(15),Malware Communication Countries(16),Email Status(17),Threat Type(18),Risk Level(19)
############################################################################################################################

def readETP():
	etpalerts = {}
	info = []
	try: 
		with open(etpfile, 'r') as f:
			reader = csv.reader(f)
			for line in reader:
				if line[7] in ['doc','exe','zip','jar','htm','7zip','com','pdf','docx','xls','xlsx','js','vbs']:
					info = { 'Time' : line[2]}, { 'From' : line[3]}, { 'Recipients' : line[4]}, { 'Subject' : line[5]}, { 'Type' : line[7] }, { 'Name' : line[8] }, { 'MD5' : line[9] }, { 'evilips' : [line[15]] }
				else:
					info = { 'Time' : line[2]}, { 'From' : line[3]}, { 'Recipients' : line[4]}, { 'Subject' : line[5]}, { 'Type' : 'url' }, { 'Name' : line[8] }, { 'MD5' : 'Unknown' }, { 'evilips' : [line[15]] }
				etpalerts.update({line[0] : info})
	except Exception as e: print ("Can't open ETP alerts file\n", e)
	f.close()
	return (etpalerts)

if __name__ == '__main__':
	print (readETP())