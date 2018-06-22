from paramiko import SSHClient
import threading
import time
import sys

#get the arguments
args = sys.argv

if len(args) < 5:
	print "\033[91m Not all arguments set\033[0m nodeId runtime, interval, boundedIp"
	exit()

serverid = args[1]
runtime = float(args[2])
interval = float(args[3])
bindip = args[4]

print "Server:" + serverid
print "Run time:" + str(runtime)
print "Interval:" + str(interval)
print "Bounded IP:" + str(bindip)

#init variables
completeList = []
start_time = time.time()

#elapsed: seconds since start of running the script
#cwnd
#ssthresh
#rtt
variables = ['elapsed', 'portnumber', 'cwnd', 'ssthresh', 'rtt']

#create the csv
def createCsv():

	csvTotalText = ""
	headers = ""
	#create the headers
	for key in variables:
		headers = headers + key + ","

	csvTotalText = headers[:-1] + "\n"

	#Process the list
	for dataPoints in completeList:
		#start an empty csv line
		csvLine = ""

		for key in variables:
			if key in dataPoints:
				csvLine = csvLine + str(dataPoints[key]) + ","
			else:
				#the variable wasn't found in this dataset
				csvLine = csvLine + "-" + ","


		#the [:-1] removes the last comma
		csvTotalText = csvTotalText + csvLine[:-1] + "\n" 

	#create the csv
	filename = "results-" + str(time.time()) +".csv"

	csv_file = open(filename, "w")
	csv_file.write(csvTotalText)
	csv_file.close()

	print "Saved as:" + filename

#parse the terminal output to the values we want
def processDataStream(terminalLine, portnumber):
	#split the dataset into the seperate elements
	items = terminalLine.split(" ")

	resultList = {}

	for item in items:
		#split the item on :, it the item has it
		if item.find(":") != -1:
			key,value = item.split(":")
			resultList[key] = value
			#print "key:" + key + " value:"+value

	resultList['elapsed'] = (time.time() - start_time)
	resultList['portnumber'] = portnumber

	#add the list to the definitive list we use to later create the csv
	completeList.append(resultList)

#parse the line with portnumber to only the portnumber
def getPortNumberFromLine(terminalLine):
	#split the dataset into the seperate elements
	items = terminalLine.split(" ")

	for item in items:
		#split the item on :, it the item has it
		if item.find(":") != -1:
			key,value = item.split(":")
			if key == bindip:
				return value
	return "-"

#obtaining the ss results
def getSSresult(ssh):
	#obtain the result
	ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("ss -i")
	shouldAddNextLine = 0
	portnumber = ""

	#loop through the terminal results
	for line in ssh_stdout:

		#check for the correct port number
		if line.find(bindip) != -1:
			portnumber = getPortNumberFromLine(line)
			shouldAddNextLine = 1
		
		#check if it's the line we are interested in
		if line.find("rtt") != -1 and shouldAddNextLine == 1:
			shouldAddNextLine = 0
			processDataStream(line.rstrip(), portnumber)

		#print line

		#cancel the while loop when needed
		#if line == '':
	  		#break

	#call the function again if within the time setting
	if (time.time() - start_time) < runtime:
		print "Measurement performed. Time elapsed:" + str(time.time() - start_time)
		threading.Timer(interval, getSSresult, [ssh]).start()
	else:	
		#close the SSH connection, and proceed with creating the csv
		ssh.close()
		print '\033[0m Connection closed'

		createCsv()
		#print completeList



#SSH to main server
port = 22
ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect("10.10.2."+serverid, port, username="nas", password="naslab")

getSSresult(ssh)


#ssh.close()
