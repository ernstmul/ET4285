from paramiko import SSHClient

def runServerChecks(serverip):

	#login to server	
	port = 22
	ssh = SSHClient()
	ssh.load_system_host_keys()
	ssh.connect(serverip, port, username="nas", password="naslab")

	#1. check current available congestion controls
	ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("sysctl net.ipv4.tcp_available_congestion_control")

	lines = ""
	while True:
	  line = ssh_stdout.readline()
	  lines = lines + line

	  if line == '':
	  	break

	print "Available algorithms:"
	algorithms = ""
	  
	if lines.find("bbr") != -1:
	    algorithms = algorithms + "\033[96m BBR \033[0m"
	if lines.find("cubic") != -1:
	    algorithms = algorithms + "\033[96m Cubic \033[0m"
	if lines.find("reno") != -1:
	    algorithms = algorithms + "\033[96m Reno \033[0m"

	print algorithms
	print "" #add white space


	#2. check set congestion controls
	ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("sysctl net.ipv4.tcp_congestion_control")

	lines = ""
	while True:
	  line = ssh_stdout.readline()
	  lines = lines + line

	  if line == '':
	  	break

	print "Set algorithm:"
	  
	if lines.find("bbr") != -1:
	    print "\033[96m BBR \033[0m"
	if lines.find("cubic") != -1:
	    print "\033[96m Cubic \033[0m"
	if lines.find("reno") != -1:
	    print "\033[96m Reno \033[0m"

	#3. check if the servers no eachother
	routes = ["172.16.1.0", "172.16.2.0", "172.16.3.0", "172.16.4.0", "172.16.5.0", "172.16.6.0", "172.16.7.0", "172.16.8.0", "172.16.9.0"]
	ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("netstat -rn")

	lines = ""
	while True:
	  line = ssh_stdout.readline()
	  lines = lines + line

	  if line == '':
	  	break

	print lines
	for route in routes:	
		if lines.find(route) == -1:
			print "" + route + " \033[91m NOT FOUND\033[0m"


	print "" #add white space

