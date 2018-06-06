from paramiko import SSHClient
from subprocess import check_output
from serverChecks import runServerChecks

#server list
servers = ["10.10.2.4", "10.10.2.6", "10.10.2.7", "10.10.2.9", "10.10.2.2", "10.10.2.19", "10.10.2.16", "10.10.2.18", "10.10.2.15", "10.10.2.5"]

#loop through all servers
for serverip in servers:
	out = check_output(["nmap", "-p", "22", serverip])
	
	if out.find("down") == -1:
	    print "" + serverip + " \033[92m OPEN\033[0m"
	    runServerChecks(serverip)
	else:
		print "" + serverip + " \033[91m CLOSED\033[0m"
		print "" #whitespace
		
