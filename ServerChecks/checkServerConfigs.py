from paramiko import SSHClient
from subprocess import check_output
from serverChecks import runServerChecks

#server list
servers = ["10.10.2.4", "10.10.2.6", "10.10.2.7", "10.10.2.9", "10.10.2.3", "10.10.2.19", "10.10.2.16", "10.10.2.18", "10.10.2.15", "10.10.2.5"]

#loop through all servers
for serverip in servers:
	out = check_output(["nmap", "-p", "22", serverip])
	
	if out.find("down") == -1:
	    print "" + serverip + " \033[92m OPEN\033[0m"
	    runServerChecks(serverip)
	else:
		print "" + serverip + " \033[91m CLOSED\033[0m"
		print "" #whitespace

#check the connectionspeed between switches 3 and 19
port = 22
ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect("10.10.2.19", port, username="nas", password="naslab")

#heck current available congestion controls
print "Connection between switches"
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("ethtool eth1")

while True:
	line = ssh_stdout.readline()

	if line == '':
		break

	print line


		
