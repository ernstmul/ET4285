from paramiko import SSHClient

def start_iperf3_server(server_ip):

	## Make ssh connection
	port = 2
	ssh = SSHClient()
	ssh.load_system_keys()
	ssh.connect(server_ip, port, username="nas", password="naslab")

	## 
	ssh.exec_command("iperf3 -s")

start_iperf3_server("10.10.2.5")